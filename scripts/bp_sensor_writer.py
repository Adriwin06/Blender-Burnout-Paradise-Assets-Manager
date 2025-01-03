import bpy
import struct

bl_info = {
    "name": "Burnout Paradise Sensor Writer",
    "description": "Write sensor data from Blender objects into a .dat file.",
    "author": "Adriwin",
    "version": (1, 2),
    "blender": (3, 0, 0),
    "location": "3D View > Object",
    "category": "Import-Export",
}

def gather_sensor_data():
    """
    Gathers sensor data from Blender objects based on their names.
    Returns a list of arrays containing sensor data.
    """
    sensors = []

    for obj in bpy.context.scene.objects:
        if obj.name.startswith("SensorSpec_") and "DirectionParams" in obj:
            params = obj["DirectionParams"]
            sensors.append(params)  # Append the full array as-is
    return sensors

def calculate_offsets(start_offset, num_sensors, step):
    """
    Calculate offsets for all sensors based on the start offset and step size.

    Args:
        start_offset: The starting offset for the first sensor.
        num_sensors: The number of sensors.
        step: The byte gap between consecutive sensors.

    Returns:
        A list of calculated offsets.
    """
    return [start_offset + i * (step + 0x10) for i in range(num_sensors)]  # Corrected step size

def update_file(filepath, sensors, offsets):
    """
    Updates the sensor data in the file at the given offsets.

    Args:
        filepath: Path to the .dat file to update.
        sensors: List of arrays containing sensor data.
        offsets: List of offsets to update sensor data.
    """
    try:
        with open(filepath, "r+b") as f:
            for sensor, offset in zip(sensors, offsets):
                # Pack all 6 values in big-endian
                packed_data = b"".join(struct.pack(">f", val) for val in sensor)
                # Seek to the offset and write the values
                f.seek(offset)
                f.write(packed_data)
        print(f"Updated sensor data in {filepath}")
    except Exception as e:
        print(f"Error updating file: {e}")

class BP_OT_WriteSensorData(bpy.types.Operator):
    """Write sensor data from Blender objects into a .dat file"""
    bl_idname = "object.bp_write_sensor_data"
    bl_label = "BP - Write Sensor Data"
    bl_options = {'REGISTER', 'UNDO'}

    filepath: bpy.props.StringProperty(
        name="File Path",
        description="Path to the .dat file to write",
        maxlen=1024,
        subtype='FILE_PATH',
    )

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        # Starting offset for the first sensor and step size
        start_offset = 0x120  # Starting offset for the first sensor
        step = 0x30           # 48 bytes (hex 30) between each sensor

        # Gather sensor data
        sensors = gather_sensor_data()

        # Calculate offsets dynamically
        offsets = calculate_offsets(start_offset, len(sensors), step)

        # Update the file
        update_file(self.filepath, sensors, offsets)

        return {'FINISHED'}

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

def menu_func(self, context):
    self.layout.operator(BP_OT_WriteSensorData.bl_idname)

def register():
    bpy.utils.register_class(BP_OT_WriteSensorData)
    bpy.types.VIEW3D_MT_object.append(menu_func)

def unregister():
    bpy.utils.unregister_class(BP_OT_WriteSensorData)
    bpy.types.VIEW3D_MT_object.remove(menu_func)

if __name__ == "__main__":
    register()
