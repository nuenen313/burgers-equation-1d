import numpy as np
import os

cwd = os.getcwd()
blockMeshDictPath = os.path.join(cwd, "system", "blockMeshDict")

with open(blockMeshDictPath, 'r') as f:
    block_mesh_dict_lines = f.readlines()

    cell_count_line = [line for line in block_mesh_dict_lines if 'cell_count_x' in line][0]
    cell_count_x = int(''.join(c for c in cell_count_line if c.isdigit()))

    cell_count_y_line = [line for line in block_mesh_dict_lines if 'cell_count_y' in line][0]
    cell_count_y = int(''.join(c for c in cell_count_y_line if c.isdigit()))

try:
    if cell_count_x is not None and cell_count_y is not None:
        print(f'Creating the 0/U file:\n *    Cell count along the x axis: {cell_count_x}\n '
              f'*    Cell count along the y axis: {cell_count_y} \n')
    else:
        raise TypeError
except TypeError:
    print('Failed to read cell count value from system/blockMeshDict')

sineList = []

for j in range(cell_count_y):
    for i in range(cell_count_x):
        if cell_count_x != 1:
            x = float(i) / (cell_count_x - 1)
        else:
            x = 1.0
        if cell_count_y != 1:
            y = float(j) / (cell_count_y - 1)
        else:
            y = 1.0

        if i == 0 or i == cell_count_x - 1:
            sineList.append([0, 0, 0])
        else:
            sineList.append([np.sin(2.0 * np.pi * x), 0, 0])

UFilePath = os.path.join(cwd, "0", "U")
with open(UFilePath, "w") as file:
    file.write("/*--------------------------------*- C++ -*----------------------------------*\\\n")
    file.write(" =========                 |                                                 \n")
    file.write(" \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           \n")
    file.write("  \\    /   O peration     | Version:  10                                    \n")
    file.write("   \\  /    A nd           | Web:      www.OpenFOAM.org                      \n")
    file.write("    \\/     M anipulation  |                                                 \n")
    file.write("\\*---------------------------------------------------------------------------*/\n")
    file.write("FoamFile\n{\n    format      ascii;\n    class       volVectorField;\n"
               "    location    \"0\";\n    object      U;\n}\n")
    file.write("// ************************************************************************* //\n")
    file.write("dimensions [0 1 -1 0 0 0 0];\n \n")
    file.write("internalField   nonuniform List<vector>\n")
    file.write(f"{len(sineList)}\n(\n")
    for vector in sineList:
        file.write(f"    ({vector[0]} {vector[1]} {vector[2]})\n")
    file.write(");\n")
    file.write("boundaryField\n{\n")
    file.write("    inlet\n")
    file.write("    {\n")
    file.write("        type            fixedValue;\n")
    file.write("        value           uniform (0 0 0);\n")
    file.write("    }\n")
    file.write("    outlet\n")
    file.write("    {\n")
    file.write("        type            fixedValue;\n")
    file.write("        value           uniform (0 0 0);\n")
    file.write("    }\n")
    file.write("    sides\n")
    file.write("    {\n")
    file.write("        type            empty;\n")
    file.write("    }\n")
    file.write("}\n")
    file.write("// ************************************************************************* //\n")
