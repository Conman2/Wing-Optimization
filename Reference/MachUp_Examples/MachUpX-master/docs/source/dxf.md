# Modeling Guide for MachUpX .dxf Files in SolidWorks
There are at three types of files for each wing segment created in MachUpX. How each file is used is described as follows. Alternately, a video tutorial for the whole craft can be found [here](https://youtu.be/szW97Rz5sOU). The files used were generated for a traditional aircraft with a main wing, horizontal, and vertical stabilizers.

## Import Planes
The first file imported is used to create the plane lines.

### Insert Plane Lines
This first file terminates in _planes for the wing segment being modeled. This .dxf file must be inserted on the right plane. Note the plane must be selected prior to selecting Insert > DXF/DWG...

![](dxf_figs/01_plane_insert.png)

In this case, the file name is traditional_main_wing_right_planes.dxf.

![](dxf_figs/02_dxf0_select.png)

This file must be imported as a 2D file.

![](dxf_figs/03_insert_dxf0_2D.png)

### Changing Units if 'SI' in MachUpX
If you're using SI units in MachUpX, the base unit for all .dxf files created will be meters. If you're using English units, the base unit for all .dxf files is in inches. If you're using English units, you don't need to change the import units.
To modify the units import, move to the next window in the DXF/DWG Import wizard.

![](dxf_figs/04_01_change_unit.png)

Select meters

![](dxf_figs/04_02_change_unit.png)

### Create Planes
Beginning near the origin point, select the body of each T, along with the right plane. Insert a plane using these selections. The plane inserted will be coincident with the line, and perpendicular to the right plane.

![](dxf_figs/05_insert_plane.png)

## Import 2D .dxf Airfoils
Next the airfoil outlines must be imported to the planes previously created.

It can help to rename each plane created to _## beginning at 0 at the root / origin plane. The .dxf file to be imported on this first plane (in the image plane_00) is traditional_airplane_main_wing_right_00.

![](dxf_figs/06_dxf1_select.png)

Insert the .dxf shape (as 2D).

![](dxf_figs/07_dxf1_2_import.png)

Continue through each plane and related .dxf file. There will be at least 2. The number of these files depends on how many changes in airfoil occur in the wing segement.

NOTE : If one of your airfoil outlines does not import, check whether you have a wing segment with a taper ratio of 0. Because Soliworks cannot loft between a point and 2D shape, MachUpX modifies the chord at the tip point from 0 to 1e-5. If your model is already extremely small, it may cause sever changes in the model compared to your input design. Consider scaling the values you put into MachUpX to resolve this issue.

## Import 3D .dxf Guide Curves
Lastly, the guide curves must be imported.

When imported a 3D .dxf file, the plane selected prior does not matter. Import the guide curves file (traditional_main_wing_right_GC in this example) as a 3D .dxf.

![](dxf_figs/08_dxf2_import_3D.png)

### Problems with guide curves?
Often, with a complex shape, two guide curves are not enough to constrain the wing geometry through the loft. For more complex lofts, we recommend several guide curves. The number of guide curves can be increased in the .dxf export function. It should be noted that SolidWorks begins to fail after around forty guide curves. We recommend between four and twenty if two is insufficient. If the loft does not complete, sometimes unselecting some guide curves may help.

We also recommend an even number of guide curves. This ensures a guide curve is placed at the trailing edge and at the leading edge. Otherwise, the nose of the wing may not loft as desired.

## Loft
Now the loft can be performed

### Loft Point Correlation
As selecting each 2D outline, ensure the loft points relate to the same point on each airfoil. Otherwise, the loft will fail.

![](dxf_figs/09_01_wrong_green.png)

The points must be positioned like so.

![](dxf_figs/09_02_right_green.png)

### Loft Complete
Select each outline sequentially, and then each guide curve.

![](dxf_figs/10_loft.png)

Success! Good Luck!

![](dxf_figs/11_complete.png)