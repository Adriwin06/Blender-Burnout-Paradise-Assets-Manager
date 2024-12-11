import bpy

bl_info = {
    "name": "Burnout Paradise Wheels Collections Remover",
    "author": "Adriwin",
    "version": (1, 0),
    "blender": (3, 0, 0),
    "location": "3D View > Object",
    "description": "Renames empty and object based on parent collection, then removes collections",
    "warning": "",
    "wiki_url": "",
    "support": "COMMUNITY",
    "category": "Object"
}

# Define the operator
def get_parent_collection(collection):
    for coll in bpy.data.collections:
        if collection.name in [child.name for child in coll.children]:
            return coll
    return None

class OBJECT_OT_bp_wheels_collections_remover(bpy.types.Operator):
    bl_idname = "object.bp_wheels_collections_remover"
    bl_label = "BP Wheels Collections Remover"
    bl_description = "Renames empty and object based on parent collection, then removes collections"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        collections_to_remove = []
        for collection in bpy.data.collections:
            parent_collection = get_parent_collection(collection)
            if not parent_collection:
                continue

            if len(collection.objects) == 0:
                continue

            empty_object = None
            child_object = None

            # Find the empty and the object
            for obj in collection.objects:
                if obj.type == 'EMPTY':
                    empty_object = obj
                else:
                    child_object = obj

            if empty_object and child_object:
                # Rename objects based on parent collection
                parent_name = parent_collection.name
                empty_object.name = f"{parent_name}_empty"
                child_object.name = parent_name

                # Unlink objects from collections
                collection.objects.unlink(empty_object)
                collection.objects.unlink(child_object)

                # Link objects to the scene collection
                context.scene.collection.objects.link(empty_object)
                context.scene.collection.objects.link(child_object)

                # Mark collections for removal
                collections_to_remove.append(collection)
                collections_to_remove.append(parent_collection)

        # Remove marked collections
        for collection in collections_to_remove:
            bpy.data.collections.remove(collection, do_unlink=True)

        return {'FINISHED'}

# Add the button to the Object menu
def menu_func(self, context):
    self.layout.operator(OBJECT_OT_bp_wheels_collections_remover.bl_idname, icon="GROUP")

# Register and unregister the operator and menu
def register():
    bpy.utils.register_class(OBJECT_OT_bp_wheels_collections_remover)
    bpy.types.VIEW3D_MT_object.append(menu_func)

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_bp_wheels_collections_remover)
    bpy.types.VIEW3D_MT_object.remove(menu_func)

if __name__ == "__main__":
    register()
