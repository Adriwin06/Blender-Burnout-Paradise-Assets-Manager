import json
import os
import bpy

def load_json(json_path):
    """Load a JSON file and return its content."""
    try:
        with open(json_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"JSON file not found: {json_path}")
    except json.JSONDecodeError:
        print(f"Invalid JSON format in file: {json_path}")
    return {}

def rename_textures(json_paths):
    """Rename Blender images based on combined JSON mappings."""
    # Combine all mappings from provided JSON files
    combined_mapping = {}
    for path in json_paths:
        mapping = load_json(path)
        combined_mapping.update(mapping)
    
    # Iterate through all images in the Blender scene
    for img in bpy.data.images:
        image_id = img.name
        if image_id in combined_mapping:
            new_name = combined_mapping[image_id].split('/')[-1].split('?')[0]  # Extract the new name
            old_name = img.name
            img.name = new_name
            print(f"Renamed image '{old_name}' to '{new_name}'")
        else:
            print(f"No mapping found for image '{image_id}'")

class RenameTexturesOperator(bpy.types.Operator):
    bl_idname = "object.rename_textures"
    bl_label = "Rename Textures"

    json_files: bpy.props.StringProperty(
        name="JSON Files",
        description="Select one or more JSON files for texture mappings",
        subtype="FILE_PATH"
    )

    def execute(self, context):
        # Support multiple file selections separated by semicolons
        json_paths = self.json_files.split(';')
        rename_textures(json_paths)
        return {'FINISHED'}

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

class BP_MT_RenameTexturesMenu(bpy.types.Menu):
    bl_label = "BP"
    bl_idname = "OBJECT_MT_bp_rename_textures_menu"

    def draw(self, context):
        layout = self.layout
        layout.operator(RenameTexturesOperator.bl_idname, text="Rename Textures")

def menu_func(self, context):
    self.layout.menu(BP_MT_RenameTexturesMenu.bl_idname)

def register():
    bpy.utils.register_class(RenameTexturesOperator)
    bpy.utils.register_class(BP_MT_RenameTexturesMenu)
    bpy.types.VIEW3D_MT_object.append(menu_func)

def unregister():
    bpy.utils.unregister_class(RenameTexturesOperator)
    bpy.types.VIEW3D_MT_object.remove(menu_func)
    bpy.utils.unregister_class(BP_MT_RenameTexturesMenu)

if __name__ == "__main__":
    register()
    print("Rename Textures addon registered. Use the operator 'Rename Textures' to select JSON file(s) and rename textures.")
