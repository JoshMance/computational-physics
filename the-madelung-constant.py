# Calculating the Madelung constant of sodium chloride

import numpy as np # Used for creating and iterating over arrays
import itertools   # Used to find all permutations with replacement 
                   # of a list of integers

A = 1                           # The distance between atoms in meters
E = 1.60217663*(10**-19)        # The charge of a proton
E_0 = 8.8541878128*(10**-12)    # The permittivity of free space
PI = 3.14159265359              
L = 100                         # The cubic lattice has sides of length 
                                # 2*L+1 atoms and contains (2*L+1)**3 atoms

# Calculates the effect the charge a single atom located at (i,j,k)
# will have on the atom at the origin (0,0,0)
def potential(i, j, k):

    # Sodium atoms have a positive charge, chloride atoms have a negative charge
    charge_sign = 1 if ((i+j+k) % 2 == 0) else -1
    
    distance_to_origin = A*(i**2 + j**2 + k**2)**0.5
    potential = (charge_sign*E)/(4*PI*E_0*A*distance_to_origin)

    return potential

# Uses permutations with replacement to return the coordinates of 
# all atoms within the bounds of a lattice defined by L, excluding (0,0,0)
def atom_coordinates_list():
    integers = [val-L for val in list(range((2*L)+1))]
    coordinates = list(itertools.product(integers, repeat=3))
    coordinates.remove((0,0,0))
    return coordinates


def total_potential():
    coordinates = atom_coordinates_list()







