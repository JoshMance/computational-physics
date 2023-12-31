# Calculating the Madelung constant of sodium chloride
# Larger values of L will use more atoms and be more accurate while 
# also increasing the total required computation time

import numpy as np      # Used for creating and iterating over arrays
import itertools        # Used to find all permutations with replacement 
                        # of a list of integers
from tqdm import tqdm   # Provides 'loading bar' for loops

A = 1                           # The distance between atoms (unit value)
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

# Creates and iterates over all coordinates constrained by L to find
# the total potential experienced by the atom at the origin (0,0,0)
def find_total_potential():
    
    total_potential = 0

    integers = [val-L for val in list(range((2*L)+1))]
    for i, j, k in tqdm(itertools.product(integers, repeat=3)):
        if (i, j, k) != (0,0,0):
            total_potential += potential(i, j, k)

    return total_potential

# Multiplies the total potential by appropriate constants
# to get the Madelung constant 
def get_madelung_constant(total_potential):
    madelung_constant = total_potential*((4*PI*E_0*A)/E)
    return madelung_constant


total_potential = find_total_potential()
madelung_constant = get_madelung_constant(total_potential)
print("The Total Potential: {} \n The Calculated Madelung Constant: {}".format(
      "{:e}".format(total_potential), "{:e}".format(madelung_constant)))








