import bpy

bl_info = {
    "name": "FBX Type Manager",
    "description": "Add or remove FBX type property for LOD groups",
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

class BP_OT_AddFbxType(bpy.types.Operator):
    """Add FBX LodGroup property to selected objects"""
    bl_idname = "object.bp_add_fbx_type"
    bl_label = "Add LOD Group Property"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return len(context.selected_objects) > 0

    def execute(self, context):
        for obj in context.selected_objects:
            obj["fbx_type"] = "LodGroup"
            print(f"Added FBX type to {obj.name}")
        return {'FINISHED'}

class BP_OT_RemoveFbxType(bpy.types.Operator):
    """Remove FBX LodGroup property from selected objects"""
    bl_idname = "object.bp_remove_fbx_type"
    bl_label = "Remove LOD Group Property"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return len(context.selected_objects) > 0

    def execute(self, context):
        for obj in context.selected_objects:
            if "fbx_type" in obj:
                del obj["fbx_type"]
                print(f"Removed FBX type from {obj.name}")
        return {'FINISHED'}

class VIEW3D_MT_bp_lod_tools(bpy.types.Menu):
    bl_label = "LOD Tools"
    bl_idname = "VIEW3D_MT_bp_lod_tools"

    def draw(self, context):
        layout = self.layout
        layout.operator(BP_OT_AddFbxType.bl_idname)
        layout.operator(BP_OT_RemoveFbxType.bl_idname)

def menu_func(self, context):
    self.layout.menu(VIEW3D_MT_bp_lod_tools.bl_idname)

def register():
    bpy.utils.register_class(BP_OT_AddFbxType)
    bpy.utils.register_class(BP_OT_RemoveFbxType)
    bpy.utils.register_class(VIEW3D_MT_bp_lod_tools)
    bpy.types.VIEW3D_MT_object.append(menu_func)

def unregister():
    bpy.utils.unregister_class(BP_OT_AddFbxType)
    bpy.utils.unregister_class(BP_OT_RemoveFbxType)
    bpy.utils.unregister_class(VIEW3D_MT_bp_lod_tools)
    bpy.types.VIEW3D_MT_object.remove(menu_func)

if __name__ == "__main__":
    register()
