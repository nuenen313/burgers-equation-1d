# burgers-equation-1d
Solution to the Burgers' equation in 1D, using OpenFOAM10 and comparing the results achieved by using linear discretization scheme and upwind discretization scheme. A python script (sineList.py) is used to generate initial conditions of the case.

To run on Ubuntu 22.04, build the BFoam solver and then ./Allrun the case in the terminal.

## Case setup
The case consists of a 1D channel, with 45 mesh cells (note: when changing the number of cells, make sure that it is odd. Even numbers cause some unexpected results in the cells in the middle).
![mesh](https://github.com/nuenen313/burgers-equation-1d/assets/129689130/64ea610a-fb6c-41a2-942d-b4fadf5f1309)

The `Allrun` script includes creating the initial conditions (by calling `sineList.py`), running blockMesh, and then running the solver.

## Results
The linear discretization scheme produces the following results:
![t0linear](https://github.com/nuenen313/burgers-equation-1d/assets/129689130/0ed1b6f1-f570-4c13-a6dd-cab842f9a968)
![t2linear](https://github.com/nuenen313/burgers-equation-1d/assets/129689130/961670c1-2a9b-443f-834c-851e02a8ef07)
![t3linear](https://github.com/nuenen313/burgers-equation-1d/assets/129689130/d6cc3452-986d-41f4-9a01-fc8e53ddf041)
![t4linear](https://github.com/nuenen313/burgers-equation-1d/assets/129689130/79334ab4-52fb-4d3b-837d-cc62a72dc69d)

And the upwind discretization scheme produces the following results:
![t0up](https://github.com/nuenen313/burgers-equation-1d/assets/129689130/5f1e7d5c-01c9-46c4-b4b0-244b56127735)
![t1up](https://github.com/nuenen313/burgers-equation-1d/assets/129689130/99ea3bb4-a85d-45d8-9235-81c8c706a24e)
![t3up](https://github.com/nuenen313/burgers-equation-1d/assets/129689130/328ec96a-a5e8-43c1-9662-465965d9f1c1)
![t4up](https://github.com/nuenen313/burgers-equation-1d/assets/129689130/bb88d3e3-df74-4d61-a75d-196fbdb57078)

The results showcase the discontinuities (a shock wave), and the fact that the linear interpolation scheme produces an unstable solution when discontinuities are present. When the upwind scheme is used, the discontinuity dissipates over time. This is consistent with the general behaviour of first and second order discretization schemes - the upwind method (first order scheme) is characterized by the loss of amplitude over time, and is more stable over discontinuities than the second order linear scheme.



W9
