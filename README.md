# Blender Burnout Batch Assets Import

A simple Blender script to batch import different Burnout Paradise assets into Blender using DGIorio's Burnout Paradise Blender tools.
### Additional tool
- Another simple Blender script to rename all LODs to a more understandable name, that can help with importing those LODs as LODs of the correct mesh in a game engine.
- Another script to organize the added buttons from JeBobs' Burnout Paradise Blender Helpers as well as buttons added by my srcipts. They will now all be under a `Burnout Paradise` menu in `Object` > `Burnout Paradise`.

## Prerequisites

- [Blender](https://www.blender.org/) (version 2.65 or later)
- [DGIorio's Burnout Paradise Blender tools](https://drive.google.com/file/d/14rUHXb6-Pvbi-Bxcg-CWJaEEjGtFpV-4/view)
- [JeBobs' Burnout Paradise Blender Helpers](https://github.com/JeBobs/blender_burnout_paradise_helpers) for the menu organizer

## Installation

1. Download the script from this repository.
2. Open Blender and go to `Edit > Preferences > Add-ons`.
3. Click on `Install...` and select the downloaded script file.
4. Enable the add-on by checking the box next to `Batch Import Burnout Paradise models format (.dat, .BIN, .BNDL)`.

## How to Use
### Batch importer
1. Go to `File > Import > Batch Import Burnout Paradise (.dat, .BIN, .BNDL)`.
2. If you don't see the option despite having the script installed and enabled, copy-paste the content of the script into the `Scripting` tab in Blender and run it. The option should appear now.
3. Select the files you want to import. You can select multiple files at once.
4. Configure the import options:
   - **Resource Version**: Select the game version.
   - **Resource Type**: Select the type of resource.
   - **Is Bundle File**: Check if importing from a bundle file.
   - **Clear Scene**: Check to clear the scene before importing.
### LOD renaming
1. Go to `Object` > `BP - Rename All LODs`.
2. The script will rename all LOD meshes based on their parent objects, mostly for for exporting and importing in Unreal Engine 5.

## Troubleshooting

- Ensure you have [DGIorio's Burnout Paradise Blender tools](https://drive.google.com/file/d/14rUHXb6-Pvbi-Bxcg-CWJaEEjGtFpV-4/view) installed.
- If the import fails, check the console for error messages and ensure the selected files are compatible with the script.
- If you have any issue or suggestion, feel free to open an issue or create a discussion.
