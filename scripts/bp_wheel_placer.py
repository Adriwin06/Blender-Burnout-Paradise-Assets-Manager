import bpy

bl_info = {
	"name": "Burnout Paradise Wheels placer tool",
	"description": "Place all the wheels based on the WheelSpec objects",
	"author": "Adriwin",
	"version": (1, 0),
	"blender": (3, 0, 0),
	"location": "3D View or Search",
	"warning": "",
	"wiki_url": "",
	"tracker_url": "",
	"support": "COMMUNITY",
	"category": "Workflow"
	}

def duplicate_and_adjust_wheels():
    context = bpy.context
    # Ensure the active object is an empty (parent) for the wheel mesh
    selected_empty = context.active_object if context.active_object and context.active_object.type == 'EMPTY' else None
    if not selected_empty:
        print("No valid empty selected. Please select the empty controlling the wheel mesh and try again.")
        return
    
    # Ensure the empty has a mesh child
    wheel_mesh = None
    for child in selected_empty.children:
        if child.type == 'MESH':
            wheel_mesh = child
            break
    if not wheel_mesh:
        print("The selected empty does not have a mesh child. Please check your selection.")
        return
    
    # Find all WheelSpec objects
    wheel_specs = [obj for obj in context.scene.objects if obj.name.startswith("WheelSpec_")]
    if len(wheel_specs) != 4:
        print("Exactly 4 WheelSpec objects are required. Please check your scene.")
        return
    
    # Move the selected wheel to the first WheelSpec
    selected_empty.location = wheel_specs[0].location
    selected_empty.rotation_euler = wheel_specs[0].rotation_euler
    selected_empty.scale = wheel_specs[0].scale
    
    # Create three additional wheels
    for i, spec in enumerate(wheel_specs[1:], start=1):
        # Duplicate the empty
        new_empty = selected_empty.copy()
        # Link to the same collection as the selected empty
        selected_collection = selected_empty.users_collection[0]
        selected_collection.objects.link(new_empty)
        
        # Adjust the new empty location, rotation, and scale to match the WheelSpec
        new_empty.location = spec.location
        new_empty.rotation_euler = spec.rotation_euler
        new_empty.scale = spec.scale
        
        # Remove rotation adjustment
        # if spec.name.startswith("WheelSpec_0.") or spec.name == "WheelSpec_2":
        #     new_empty.rotation_euler[2] += -1.5708  # Rotate -90 degrees
        
        # Parent the duplicated empty to the same hierarchy if needed
        new_empty.parent = selected_empty.parent
        
        # Duplicate the wheel mesh and parent it to the new empty
        new_wheel_mesh = wheel_mesh.copy()
        # Link to the same collection as the selected empty
        selected_collection.objects.link(new_wheel_mesh)
        new_wheel_mesh.parent = new_empty
        
        print(f"Adjusted empty and duplicated mesh for {spec.name}.")

class BP_OT_DuplicateAndAdjustWheels(bpy.types.Operator):
    bl_idname = "object.bp_duplicate_adjust_wheels"
    bl_label = "BP - Duplicate and Adjust Wheels"
    bl_options = {'REGISTER', 'UNDO'}
    
    @classmethod
    def poll(cls, context):
        return True
    
    def execute(self, context):
        duplicate_and_adjust_wheels()
        return {'FINISHED'}

def menu_func(self, context):
    self.layout.operator(BP_OT_DuplicateAndAdjustWheels.bl_idname)

def register():
    bpy.utils.register_class(BP_OT_DuplicateAndAdjustWheels)
    bpy.types.VIEW3D_MT_object.append(menu_func)

def unregister():
    bpy.utils.unregister_class(BP_OT_DuplicateAndAdjustWheels)
    bpy.types.VIEW3D_MT_object.remove(menu_func)

if __name__ == "__main__":
    register()