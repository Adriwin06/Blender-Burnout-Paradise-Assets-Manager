import bpy
import JeBobs_BP_BlenderTools
import bp_LOD_renaming

bl_info = {
    "name": "Menu Organizer for various Burnout Paradise tools",
    "description": "Organize Burnout Paradise tools into a submenu",
    "author": "Adriwin",
    "version": (1, 0),
    "blender": (3, 0, 0),
    "location": "3D View > Object",
    "warning": "",
    "doc_url": "",
    "tracker_url": "",
    "support": "COMMUNITY",
    "category": "Misc",
}

# Define the submenus
class OBJECT_MT_bp_lod_menu(bpy.types.Menu):
    bl_label = "LOD"
    bl_idname = "OBJECT_MT_bp_lod_menu"

    def draw(self, context):
        layout = self.layout
        layout.operator("object.bp_delete_lod_renderables", text="Delete LOD Renderables")
        layout.operator("object.bp_rename_all_lods", text="Rename All LODs")

class OBJECT_MT_bp_delete_menu(bpy.types.Menu):
    bl_label = "Delete"
    bl_idname = "OBJECT_MT_bp_delete_menu"

    def draw(self, context):
        layout = self.layout
        layout.operator("object.delete_backdrop_objects", text="Delete Backdrops")
        layout.operator("object.bp_delete_shared_assets", text="Delete Shared Assets")
        layout.operator("object.delete_prop_parts", text="Delete Prop Parts")
        layout.operator("object.delete_prop_alternatives", text="Delete Prop Alternatives")

class OBJECT_MT_bp_other_menu(bpy.types.Menu):
    bl_label = "Other"
    bl_idname = "OBJECT_MT_bp_other_menu"

    def draw(self, context):
        layout = self.layout
        layout.operator("object.name_from_resource_db", text="Name from Resource DB")
        layout.operator("object.create_car_empties", text="Create Car Empties")  # Corrected bl_idname

class OBJECT_MT_bp_import_tools(bpy.types.Menu):
    bl_label = "Import Tools"
    bl_idname = "OBJECT_MT_bp_import_tools"

    def draw(self, context):
        layout = self.layout
        layout.operator("import_scene.bpr", text="Import BPR Model")

# Update the main menu to include the new submenus
class OBJECT_MT_burnout_paradise(bpy.types.Menu):
    bl_label = "Burnout Paradise"
    bl_idname = "OBJECT_MT_burnout_paradise"

    def draw(self, context):
        layout = self.layout
        layout.menu(OBJECT_MT_bp_lod_menu.bl_idname)
        layout.menu(OBJECT_MT_bp_delete_menu.bl_idname)
        layout.menu(OBJECT_MT_bp_other_menu.bl_idname)


def menu_func(self, context):
    self.layout.menu(OBJECT_MT_burnout_paradise.bl_idname)

def register():
    bpy.utils.register_class(OBJECT_MT_burnout_paradise)
    bpy.utils.register_class(OBJECT_MT_bp_lod_menu)
    bpy.utils.register_class(OBJECT_MT_bp_delete_menu)
    bpy.utils.register_class(OBJECT_MT_bp_other_menu)
    bpy.utils.register_class(OBJECT_MT_bp_import_tools)
    # Remove menu functions from JeBobs_BP_BlenderTools
    bpy.types.VIEW3D_MT_object.remove(JeBobs_BP_BlenderTools.object_menu_func)
    bpy.types.VIEW3D_MT_add.remove(JeBobs_BP_BlenderTools.add_menu_func)
    # Remove menu from LOD renaming script
    bpy.types.VIEW3D_MT_object.remove(bp_LOD_renaming.menu_func)
    # Add the Burnout Paradise menu
    bpy.types.VIEW3D_MT_object.append(menu_func)

def unregister():
    # Restore menu functions from JeBobs_BP_BlenderTools
    bpy.types.VIEW3D_MT_object.append(JeBobs_BP_BlenderTools.object_menu_func)
    bpy.types.VIEW3D_MT_add.append(JeBobs_BP_BlenderTools.add_menu_func)
    # Restore menu from LOD renaming script
    bpy.types.VIEW3D_MT_object.append(bp_LOD_renaming.menu_func)
    # Remove the Burnout Paradise menu
    bpy.types.VIEW3D_MT_object.remove(menu_func)
    bpy.utils.unregister_class(OBJECT_MT_burnout_paradise)
    bpy.utils.unregister_class(OBJECT_MT_bp_import_tools)
    bpy.utils.unregister_class(OBJECT_MT_bp_other_menu)
    bpy.utils.unregister_class(OBJECT_MT_bp_delete_menu)
    bpy.utils.unregister_class(OBJECT_MT_bp_lod_menu)

if __name__ == "__main__":
    register()