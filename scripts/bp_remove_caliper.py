import bpy

bl_info = {
    "name": "Burnout Paradise Remove Caliper Objects",
    "author": "Adriwin",
    "version": (1, 0),
    "blender": (3, 0, 0),
    "location": "3D View > Object",
    "description": "Removes the caliper to only keep the wheel mesh",
    "warning": "",
    "wiki_url": "",
    "support": "COMMUNITY",
    "category": "Object"
}

def count_polygons(obj):
    """
    Count the total number of polygons in an object.
    
    Args:
        obj (bpy.types.Object): Blender object to count polygons for
    
    Returns:
        int: Total number of polygons
    """
    if obj.type != 'MESH':
        return 0
    
    return len(obj.data.polygons)

def get_all_collections(collection):
    yield collection
    for child in collection.children:
        yield from get_all_collections(child)

def remove_caliper_with_fewer_polygons():
    """
    Remove the caliper empty and its child mesh with fewer polygons when there are exactly two empties under the same collection.
    """
    # Collect all collections in the scene recursively
    collections = set()
    def recurse_collection(col):
        collections.add(col)
        for child_col in col.children:
            recurse_collection(child_col)
    for col in bpy.data.collections:
        recurse_collection(col)
    
    # Process each collection
    for collection in collections:
        # List of empties with one child mesh in this collection
        empties = []
        for obj in collection.objects:
            if obj.type == 'EMPTY':
                # Get the mesh child of the empty
                children = [child for child in obj.children if child.type == 'MESH']
                if len(children) == 1:
                    empties.append((obj, children[0]))

        # Only process if there are exactly two such empties
        if len(empties) == 2:
            # Count polygons for each child mesh
            polygon_counts = [count_polygons(child_mesh) for _, child_mesh in empties]

            # Determine which empty and mesh to remove
            if polygon_counts[0] < polygon_counts[1]:
                index_to_remove = 0
            else:
                index_to_remove = 1

            empty_to_remove, child_to_remove = empties[index_to_remove]

            # Capture names before removal
            mesh_name = child_to_remove.name
            mesh_polygons = polygon_counts[index_to_remove]
            empty_name = empty_to_remove.name

            # Remove the child mesh
            for col in child_to_remove.users_collection:
                col.objects.unlink(child_to_remove)
            bpy.data.objects.remove(child_to_remove, do_unlink=True)
            print(f"Removed caliper mesh: {mesh_name} ({mesh_polygons} polygons)")

            # Remove the empty parent
            for col in empty_to_remove.users_collection:
                col.objects.unlink(empty_to_remove)
            bpy.data.objects.remove(empty_to_remove, do_unlink=True)
            print(f"Removed caliper empty: {empty_name}")

class OBJECT_OT_RemoveCaliperWithFewerPolygons(bpy.types.Operator):
    bl_idname = "object.remove_caliper_with_fewer_polygons"
    bl_label = "BP - Remove Caliper with Fewer Polygons"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return True  # Always available

    def execute(self, context):
        remove_caliper_with_fewer_polygons()
        return {'FINISHED'}

def menu_func(self, context):
    self.layout.operator(OBJECT_OT_RemoveCaliperWithFewerPolygons.bl_idname)

def register():
    bpy.utils.register_class(OBJECT_OT_RemoveCaliperWithFewerPolygons)
    bpy.types.VIEW3D_MT_object.append(menu_func)

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_RemoveCaliperWithFewerPolygons)
    bpy.types.VIEW3D_MT_object.remove(menu_func)

if __name__ == "__main__":
    register()