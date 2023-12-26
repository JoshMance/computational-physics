# Calculating the Madelung constant of sodium chloride

import numpy as np # Standard library for creating and using arrays

A = 1                           # The distance between atoms in meters
E = 1.60217663*(10**-19)        # The charge of a proton
E_0 = 8.8541878128*(10**-12)    # The permittivity of free space
PI = 3.14159265359              
L = 100                         # The cubic lattice has sides of length 2*L+1 atoms
                                # and contains (2*L+1)**3 atoms in total

# Calculates the effect the charge a single atom located at (i,j,k)
# will have on the atom at the origin (0,0,0).
def potential_at_origin(i, j, k):

    # Sodium atoms have a positive charge, chloride atoms have a negative charge
    charge_sign = 1 if ((i+j+k) % 2 == 0) else -1
    
    distance_to_origin = A*(i**2 + j**2 + k**2)**0.5
    potential = (charge_sign*E)/(4*PI*E_0*A*distance_to_origin)

    return potential




