# Blender Burnout Batch Assets Import

A comprehensive Blender add-on to batch import and manage various Burnout Paradise assets using DGIorio's Burnout Paradise Blender tools and JeBobs' Burnout Paradise Blender Helpers.

## Features

- **Batch Importer**: Import multiple Burnout Paradise model files (`.dat`, `.BIN`, `.BNDL`) efficiently.
- **LOD Renaming**: Automatically rename all Level of Detail (LOD) meshes for better organization and compatibility with game engines like Unreal Engine 5.
- **Remove Caliper Objects**: Clean up your scene by removing unnecessary caliper objects, keeping only the essential wheel meshes.
- **FBX Type Manager**: Add or remove FBX LOD group properties to manage LODs effectively.
- **Wheels Collections Remover**: Rename and reorganize wheel collections based on their parent collections, then remove unnecessary collections.
- **Wheels Placer Tool**: Duplicate and adjust wheel placements based on `WheelSpec` objects for accurate positioning.
- **Menu Organizer**: Organize all tool buttons into a dedicated `Burnout Paradise` submenu for streamlined access.

## Prerequisites

- [Blender](https://www.blender.org/) (version 3.0 or later)
- [DGIorio's Burnout Paradise Blender tools](https://drive.google.com/file/d/14rUHXb6-Pvbi-Bxcg-CWJaEEjGtFpV-4/view)
- [JeBobs' Burnout Paradise Blender Helpers](https://github.com/JeBobs/blender_burnout_paradise_helpers) (required for menu organization)

## Installation

1. **Download the Add-on:**
   - Clone the repository or download the ZIP file from [GitHub](https://github.com/your-repo/blender_burnout_batch_assets_import).

2. **Install the Add-on in Blender:**
   - Open Blender and go to `Edit > Preferences > Add-ons`.
   - Click on `Install...` and select the downloaded ZIP file or the specific script files.
   - Enable the add-on by checking the box next to `Batch Import Burnout Paradise`.

3. **Ensure Dependencies are Installed:**
   - Make sure [DGIorio's Burnout Paradise Blender tools](https://drive.google.com/file/d/14rUHXb6-Pvbi-Bxcg-CWJaEEjGtFpV-4/view) and [JeBobs' Burnout Paradise Blender Helpers](https://github.com/JeBobs/blender_burnout_paradise_helpers) are installed and enabled.

## How to Use

### 1. Batch Importer

**Purpose:** Import multiple Burnout Paradise model files (`.dat`, `.BIN`, `.BNDL`) into Blender.

**Steps:**

1. Go to `File > Import > Batch Import Burnout Paradise (.dat, .BIN, .BNDL)`.
2. If the option doesn't appear, copy-paste the script content into Blender's `Scripting` tab and run it.
3. Select the files you want to import.
4. Configure the import options:
   - **Resource Version**: Select the game version.
   - **Resource Type**: Select the type of resource.
   - **Is Bundle File**: Check if importing from a bundle file.
   - **Clear Scene**: Check to clear the scene before importing.
5. Click `Batch Import` to start the process.

### 2. LOD Renaming

**Purpose:** Rename all LOD meshes based on their parent objects for better organization and compatibility with game engines.

**Steps:**

1. Go to `Object > BP - Rename All LODs`.
2. The script will automatically rename all LOD meshes based on their `renderable_index` property.

### 3. Remove Caliper Objects

**Purpose:** Remove caliper empties and their child meshes that have fewer polygons, keeping only the essential wheel meshes.

**Steps:**

1. Go to `Object > BP - Remove Caliper with Fewer Polygons`.
2. The script will scan the scene and remove the specified caliper objects.

### 4. FBX Type Manager

**Purpose:** Add or remove the `fbx_type` property (`LodGroup`) to selected objects for better LOD management.

**Steps:**

1. Go to `Object > LOD Tools > Add LOD Group Property` or `Remove LOD Group Property`.
2. Select the objects you want to modify and choose the appropriate option.

### 5. Wheels Collections Remover

**Purpose:** Rename empty objects and their child meshes based on their parent collections, then remove the unnecessary collections.

**Steps:**

1. Go to `Object > Vehicle > Wheels Collections Remover`.
2. The script will process the collections and perform the renaming and removal.

### 6. Wheels Placer Tool

**Purpose:** Duplicate and adjust wheel placements based on `WheelSpec` objects for accurate positioning.

**Steps:**

1. Select an empty object that controls the wheel mesh.
2. Go to `Object > Vehicle > Wheels Placer Tool`.
3. The script will duplicate and adjust the wheels based on the `WheelSpec` objects in the scene.

### 7. Menu Organizer

**Purpose:** Organize all Burnout Paradise tools into a dedicated `Burnout Paradise` submenu for easier access.

**Features Organized Under the Menu:**

- **LOD**
  - Delete LOD Renderables
  - Rename All LODs
- **Vehicle**
  - Wheels Collections Remover
  - Remove Caliper Objects
  - Wheels Placer Tool
- **Delete**
  - Delete Backdrops
  - Delete Shared Assets
  - Delete Prop Parts
  - Delete Prop Alternatives
- **Other**
  - Name from Resource DB
  - Create Car Empties

**Steps:**

1. The menu is automatically added under `Object > Burnout Paradise` after installation.
2. Access all tools through this centralized menu for streamlined workflow.

## Troubleshooting

- **Missing Tools:**
  - Ensure all dependencies ([DGIorio's Tools](https://drive.google.com/file/d/14rUHXb6-Pvbi-Bxcg-CWJaEEjGtFpV-4/view) and [JeBobs' Helpers](https://github.com/JeBobs/blender_burnout_paradise_helpers)) are installed and enabled.
  
- **Import Failures:**
  - Check the console for error messages.
  - Ensure the selected files are compatible and not corrupted.
  
- **Menu Not Appearing:**
  - Run the script manually in Blender's `Scripting` tab.
  - Restart Blender after installation.

- **General Issues:**
  - Ensure you are using a compatible Blender version (3.0 or later).
  - Verify that all scripts are properly registered and there are no conflicts with other add-ons.


## Acknowledgements

- [DGIorio's Burnout Paradise Blender tools](https://drive.google.com/file/d/14rUHXb6-Pvbi-Bxcg-CWJaEEjGtFpV-4/view)
- [JeBobs' Burnout Paradise Blender Helpers](https://github.com/JeBobs/blender_burnout_paradise_helpers)
