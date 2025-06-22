import bpy

bl_info = {
    "name": "Burnout Paradise Remove Duplicate Objects",
    "description": "Remove duplicate objects in the scene based on their GameExplorerIndex property value.",
    "author": "Adriwin",
    "version": (1, 0),
    "blender": (3, 0, 0),
    "location": "3D View > Object",
    "warning": "",
    "wiki_url": "",
    "support": "COMMUNITY",
    "category": "Workflow"
}

def remove_duplicate():
    objects = [obj for obj in bpy.context.scene.objects]
    seen_exporer_index = []
    deleted_objects = []
    explorerID = 0
    child_to_delete = []

    for obj in objects:
        if "GameExplorerIndex" in obj:
            explorerID = bpy.data.objects[obj.name]["GameExplorerIndex"]
            if explorerID not in seen_exporer_index:
                print("Keeping ", obj.name)
                seen_exporer_index.append(explorerID)
            else:
                print("Removing ", obj.name)
                deleted_objects.append(obj.name)
                for child in obj.children:
                    child_to_delete.append(child)
                bpy.data.objects.remove(obj)
    
    for child in child_to_delete:
        print(f"Removing child {child.name}")
        bpy.data.objects.remove(child)

    print(f"Deleted {len(deleted_objects)} objects")
    print(f"New number of objects {len(seen_exporer_index)}")

class BP_OT_remove_duplicate_objects(bpy.types.Operator):
    """Remove duplicate objects in the scene based on their GameExplorerIndex property value."""
    bl_idname = "object.bp_remove_duplicate"
    bl_label = "BP - Remove Duplicate"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return True
    
    def execute(self, context):
        remove_duplicate()
        return {"FINISHED"}
    

def menu_func(self, context):
    self.layout.operator(BP_OT_remove_duplicate_objects.bl_idname)

def register():
    bpy.utils.register_class(BP_OT_remove_duplicate_objects)
    bpy.types.VIEW3D_MT_object.append(menu_func)

def unregister():
    bpy.utils.unregister_class(BP_OT_remove_duplicate_objects)
    bpy.types.VIEW3D_MT_object.remove(menu_func)