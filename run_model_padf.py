#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 14:06:17 2020

@author: andrewmartin
"""

import parallel_model_padf_0p4 as pmp
import multiprocessing as mp

if __name__ == '__main__':

#
# create an instance of the class with all parameters
#
    modelp = pmp.model_padf()


#
# This is the directory that contains the root directory for input/output files
# (don't forget the final "/". If using windows may need "\\" for each one.)
#
#modelp.root = "/Users/andrewmartin/Work/Teaching/2020/ONPS2186/codes/model-padf-master/"
    modelp.root = "C:\\Users\\jackb\\python\\model-padf-master\\"
    
#
# this is a directory for this specific project
#
    modelp.project = "1al1\\"

#
# name of .xyz file containing all the atomic coordinates
#
    modelp.xyz_name = "1al1_ex.xyz"  # the xyz file contains the cartesian coords of the crystal structure expanded to include r_probe


#
# crystallolographic file with unit cell information
#
    modelp.cif_name = "1al1_edit.cif"  # the cif containing the asymmetric unit. This often needs to be edited for PDB CIFs hence '_edit' here
    

#
# The number of processes. 
#
    modelp.pool = mp.Pool(mp.cpu_count())  # change to set the number of processors
    # modelp.pool = mp.Pool(2)  # change to set the number of processors

#
# Unit cell parameters (a,b,c,alpha,beta,gamma)
#
    modelp.ucds = [62.35000, 62.35000, 62.35000, 90.0000, 90.0000, 90.0000]

   
# probe radius: defines the neighbourhood around each atom to correlate
    modelp.r_probe = 10.0

# angular pixel (bin) width in the final PADF function
    modelp.angular_bin = 2.0

# radial pixel (bin) width in the final PADF function
    modelp.r_dist_bin = 0.1

# (not sure, leave it as is)
    modelp.probe_theta = 90.0

# Scale the radial correlations by this power, i.e. r^(r_power)
    modelp.r_power = 2
   
# If you wish to compute the final PADFs from a
# partial data set use this flag and input the loop
# at which the data is converged (check the _cosim.dat plot)
    modelp.convergence_check_flag = False


#
# Include four body terms (True/False)
#
    modelp.fourbody = True

#
# save parameters to file
#
    modelp.write_all_params_to_file()

#
# Run the calculation!
#
    pmp.run(modelp)