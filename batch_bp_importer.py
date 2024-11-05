import bpy
import os
from bpy_extras.io_utils import ImportHelper
from bpy.props import (
    StringProperty,
    BoolProperty,
    EnumProperty,
    CollectionProperty,
)
from bpy.types import Operator
import import_bpr_models


bl_info = {
    "name": "Batch Import Burnout Paradise models format (.dat, .BIN, .BNDL)",
    "description": "Batch Import meshes files from Burnout Paradise Remastered PC, Burnout Paradise X360 and PS3, Burnout 5 X360 using DGIorio's import script",
    "author": "Adriwin",
    "version": (1, 0),
    "blender": (2, 65, 0),
    "location": "File > Import > Batch Import Burnout Paradise (.dat, .BIN, .BNDL)",
    "warning": "You need to have DGIorio's import script installed", 
    "doc_url": "",
    "tracker_url": "",
    "support": "COMMUNITY",
    "category": "Import-Export",
}

class ImportBatchBPR(Operator, ImportHelper):
    """Import multiple Burnout Paradise model files"""
    bl_idname = "import_scene.batch_bpr"
    bl_label = "Batch Import"
    bl_options = {'PRESET', 'UNDO'}

    # Update the filename extension and filter to include .dat and .BNDL files
    filename_ext = ".dat;.BIN;.BNDL"
    filter_glob: StringProperty(
        default="*.dat;*.BIN;*.BNDL",
        options={'HIDDEN'},
    )

    # Enable multiple file selection
    files: CollectionProperty(
        name="File Path",
        type=bpy.types.OperatorFileListElement,
    )

    # Options from the default single importer
    resource_version: EnumProperty(
        name="Resource Version",
        description="Select the game version",
        items=[
            ('BPR_PC', "PC - BPR", ""),
            ('BP_PC', "PC - BP", ""),
            ('BP_PS3', "PS3 - BP", ""),
            ('BP_X360', "X360 - BP", ""),
            ('B5_X360_2006_nov', "X360 - B5 (2006-nov)", ""),
            ('B5_X360_2007_jan', "X360 - B5 (2007-jan)", ""),
            ('B5_X360_2007_feb', "X360 - B5 (2007-feb)", ""),
        ],
        default='BPR_PC',
    )

    resource_type: EnumProperty(
        name="Resource Type",
        description="Select the type of resource",
        items=[
            ('GraphicsSpec', "GraphicsSpec", ""),
            ('GraphicsStub', "GraphicsStub", ""),
            ('WheelGraphicsSpec', "WheelGraphicsSpec", ""),
            ('InstanceList', "InstanceList", ""),
            ('StreamedDeformationSpec', "StreamedDeformationSpec", ""),
            ('PolygonSoupList', "PolygonSoupList", ""),
        ],
        default='InstanceList',
    )

    is_bundle: BoolProperty(
        name="Is Bundle File",
        description="Check if importing from a bundle file",
        default=True,
    )

    clear_scene: BoolProperty(
        name="Clear Scene",
        description="Clear the scene before importing",
        default=False,
    )

    def execute(self, context):
        # Use the clear_scene option
        if self.clear_scene:
            # Clear the scene if the option is enabled
            bpy.ops.wm.read_homefile(use_empty=True)

        # Get the directory of the selected files
        folder = os.path.dirname(self.filepath)

        # Loop through the selected files
        for file_elem in self.files:
            path_to_file = os.path.join(folder, file_elem.name)

            # Determine if the file is a bundle based on its extension
            file_ext = os.path.splitext(path_to_file)[1].lower()
            is_bundle = self.is_bundle or file_ext == ".bndl"

            # Import each model file with the selected options
            status = import_bpr_models.main(
                context,
                path_to_file,
                self.resource_version,
                self.resource_type,
                is_bundle,
                False,  # clear_scene is already handled
                False   # Pass False for debug_prefer_shared_asset
            )

            if status != {'FINISHED'}:
                self.report({'WARNING'}, f"Failed to import {file_elem.name}")

        return {'FINISHED'}

def menu_func_import(self, context):
    self.layout.operator(ImportBatchBPR.bl_idname, text="Batch Import Burnout Paradise (.dat, .BIN, .BNDL)")

def register():
    bpy.utils.register_class(ImportBatchBPR)
    bpy.types.TOPBAR_MT_file_import.append(menu_func_import)

def unregister():
    bpy.utils.unregister_class(ImportBatchBPR)
    bpy.types.TOPBAR_MT_file_import.remove(menu_func_import)

if __name__ == "__main__":
    register()