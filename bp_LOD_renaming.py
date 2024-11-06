import bpy
import re

bl_info = {
	"name": "Burnout Paradise LODs renaming tool",
	"description": "Rename all Burnout Paradise LODs to a more understandable name, that can help with importing those LODs as LODs of the correct mesh in a game engine.",
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

def is_hex_named(name):
    # Remove any suffix after a dot (.)
    base_name = name.split('.')[0]
    # Check if the base name follows the hex pattern XX_XX_XX_XX
    return re.match(r"^[A-F0-9]{2}(?:_[A-F0-9]{2}){3}$", base_name) is not None

def rename_lods():
    # Collect all mesh objects
    mesh_objs = [obj for obj in bpy.context.scene.objects if obj.type == 'MESH']
    # Group objects by parent
    parent_groups = {}
    for obj in mesh_objs:
        parent = obj.parent if obj.parent else obj
        if parent.name not in parent_groups:
            parent_groups[parent.name] = []
        parent_groups[parent.name].append(obj)
    # Process each group
    for parent_name, children in parent_groups.items():
        # Sort children by vertex count (highest to lowest)
        children.sort(key=lambda obj: len(obj.data.vertices), reverse=True)
        # Rename each child
        for i, child in enumerate(children):
            # Check if the child's name is hexadecimal
            if is_hex_named(child.name):
                # Rename to parent name with LOD index
                lod_name = f"{parent_name}_LOD{i}"
                child.name = lod_name
                print(f"Renamed {child.name} (vertices: {len(child.data.vertices)}, polygons: {len(child.data.polygons)})")
            else:
                print(f"Skipped {child.name}, does not have hexadecimal name.")

class BP_OT_RenameAllLODs(bpy.types.Operator):
    bl_idname = "object.bp_rename_all_lods"
    bl_label = "BP - Rename All LODs"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        rename_lods()
        return {'FINISHED'}

def menu_func(self, context):
    self.layout.operator(BP_OT_RenameAllLODs.bl_idname)

def register():
    bpy.utils.register_class(BP_OT_RenameAllLODs)
    bpy.types.VIEW3D_MT_object.append(menu_func)

def unregister():
    bpy.utils.unregister_class(BP_OT_RenameAllLODs)
    bpy.types.VIEW3D_MT_object.remove(menu_func)