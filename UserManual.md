# Modeling with Sproxel #


---


## Mouse Controls ##
The mouse controls the movement of the camera and the creation and manipulation of filled cells in the voxel grid.

**Camera Controls:**
The camera controls are identical to that in Autodesk's Maya.  Holding the **ALT** key drops the 3d view into camera control mode.

  * **ALT** + **LEFT MOUSE BUTTON** - Rotate the camera around its center of interest.
  * **ALT** + **MIDDLE MOUSE BUTTON** - Translate the camera orthographic to its look direction.
  * **ALT** + **RIGHT MOUSE BUTTON** - Translate the camera towards its look point (feels like a scale).
  * **ALT** + **LEFT MOUSE BUTTON** + **MIDDLE MOUSE BUTTON** - Scale (same as RMB).

**Cell Manipulation:**
Cells are created by shooting a ray through the pixel you click, intersecting it with the voxel grid, and modifying the grid cells the ray intersects.  A configuration system to re-map these mouse combinations is in the works (and on the [Feature Request](http://code.google.com/p/sproxel/wiki/FeatureRequests) wiki).

  * **LEFT MOUSE BUTTON** - Operate the tool selected in the toolbar.
  * **RIGHT MOUSE BUTTON** (Erase tool) - Clear the color in the first colored cell the ray intersects.
  * **MIDDLE MOUSE BUTTON** (Pixel-Sample tool) - Sample the palette's foreground  color from the first voxel intersected (eye dropper).
  * **CTRL** + **LEFT MOUSE BUTTON** (Replace tool) - Replace the first voxel the ray intersects  with the current color.


---


## Toolbar ##
All tools selected in the toolbar are operated by a **LEFT CLICK** in the modeling window.

  * **Splat tool (green splat icon)** - Place a cell of the current color in the last grid cell the ray intersects before it hits another filled cell.  This can be thought of as shooting a wad of paint into the voxel grid.
  * **Replace tool (yellow pencil icon)** - Replace the first voxel the ray intersects with the current color.
  * **Flood-fill tool (paint bucket icon)** - Replace the color of the intersected voxel and all neighboring voxels of the same color with the palette's foreground color.
  * **Pixel-Sample tool (eye dropper icon)** - Sample the intersected voxel's color into the palette's foreground color.
  * **Erase tool (eraser icon)** - Clear the color for the intersected voxel.
  * **Slab tool (filled plane in grid icon)** - Set an entire slice of voxels to the palette's foreground color.  If a filled voxel is intersected fill from that location, otherwise fill from the first voxel intersected on the edge.  The orientation of the slab is controlled by setting the current axis (**ALT**+**X** -or- **ALT**+**Y** -or- **ALT**+**Z**).


---


## Palette ##
Someday this will have a bunch of color swatches to choose from, potentially an image to sample from, and the ability to save all your settings.  For now, you can **LEFT CLICK** in the foreground or background color boxes to set the colors.


---


## Keyboard Controls ##
WIP: The quick-quick summary is that the holding **ALT** and using the **ARROW KEYS** moves the camera, the **ARROW KEYS** on their own move the cursor (it adjusts according to the direction your camera is facing), **CTRL** + **UP/DOWN ARROW** shifts the cursor in camera depth, and the **SPACE BAR** fills the voxel with the current color.


---


## Misc Controls ##
(<font color='#880000'>Red</font> entries will be present in the next release.)
  * **Q** - Change to the Splat tool.
  * **W** - Change to the Replace tool.
  * **E** - Change to the Flood-fill tool.
  * **R** - Change to the Pixel-sample tool.
  * **T** - Change to the Erase tool.
  * **Y** - Change to the Slab tool.

  * **X** - Swap foreground and background colors.
  * **G** - Toggle voxel grid visibility.
  * **F** - Frame the voxels in the scene (or the voxel grid if there are none).
  * **CTRL** + **F** - Frame the entire voxel grid regardless of the voxels in scene.

  * **CTRL** + **N** - Bring up new file dialog.
  * **CTRL** + **S** - Save current voxel grid.
  * **CTRL** + **O** - Open voxel grid from disk.
  * **CTRL** + **Z** - Undo
  * **CTRL** + **SHIFT** + **Z** - Redo
  * **CTRL** + **C** - Bring up color picker (this will change).
  * **CTRL** + **G** - Toggle ground plane grid visibility.
  * **ALT** + **X** - Set the X plane as your working plane.
  * **ALT** + **Y** - Set the Y plane as your working plane.
  * **ALT** + **Z** - Set the Z plane as your working plane.

## Mac Note ##

Anywhere it says **CTRL**, use **Command** instead.

<br>

<h1>Sproxel File I/O</h1>

<hr />
Sproxel has two primary file formats.  The <b>CSV</b> (comma-separated value) file and the <b>enhanced PNG</b> file.  It can also export OBJ & corresponding MTL files.<br>
<br>
Saving <b>enhanced PNG file format</b> files creates standard PNG image files, but adds three important tags to the PNG tEXT metadata chunk.  These tags, "VoxelGridDimX", "VoxelGridDimY", and "VoxelGridDimZ" describe the voxel grid resolution.  The image itself contains XY slices starting at the back of the volume, progressing forward (it's possible future versions of this file format will offer other options).  Code to read and write these using QT is located in the GlModelWidget class loadGridPNG & saveGridPNG.  This file format is the default type when saving.<br>
<br>
The <b>CSV file format</b> is a simple text format that stores four unsigned 8-bit values per voxel cell.  It is arranged as XZ slices starting at the top of the voxel volume, moving towards the bottom.  Functions for reading and writing are in the GlModelWidget class as loadGridCSV and saveGridCSV.  This file format can be selected from the File->Save dialog type pulldown.<br>
<br>
Exporting a file to the <b>OBJ file format</b> is done by clicking File->Export and selecting OBJ from type type pulldown.  This file format contains a polygonal representation of the voxel grid as ASCII text.  A <b>MTL</b> file is automatically created with the same filename prefix as the <b>OBJ</b> file, and is referenced by the <b>OBJ</b>.  This file contains color information for the voxel grid.  These OBJs have been successfully imported into Maya 2012, but have not yet been tested in other software.