#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 14:06:17 2020

@author: andrewmartin
"""

import parallel_model_padf_0p65 as pmp
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
    modelp.root = "/home/jack/python/model_padf/"
    # modelp.root = "C:\\Users\\jackb\\python\\model-padf-master\\"

    #
    # this is a directory for this specific project
    #
    modelp.project = "vit_k3/"

    #
    # name of .xyz file containing all the atomic coordinates
    #
    modelp.xyz_name = "vit_k3.xyz"  # the xyz file contains the cartesian coords of the crystal structure expanded to include r_probe

    #
    # crystallographic file with unit cell information
    #
    modelp.cif_name = "vit_k3.cif"  # the cif containing the asymmetric unit. This often needs to be edited for PDB CIFs hence '_edit' here

    #
    # The number of processes.
    #
    # modelp.pool = mp.Pool(2)  # change to set the number of processors

    #
    # Unit cell parameters (a,b,c,alpha,beta,gamma)
    #
    modelp.ucds = [13.16600, 6.88120, 11.95800,  90.0000,  90.0000,  90.0000]

    # probe radius: defines the neighbourhood around each atom to correlate
    modelp.r_probe = 7.0

    # angular pixel (bin) width in the final PADF function
    modelp.angular_bin = 2.0

    # radial pixel (bin) width in the final PADF function
    modelp.r_dist_bin = 0.1

    # Scale the radial correlations by this power, i.e. r^(r_power)
    modelp.r_power = 2

    # If you wish to compute the final PADFs from a
    # partial data set use this flag and input the loop
    # at which the data is converged (check the _cosim.dat plot)
    modelp.convergence_check_flag = False

    '''
    Calculation mode.
    'rrprime' :     Calculate the r = r' slice
    
    # Under development:
    'rrtheta' :     Calculate slices through Theta(r,r',theta)
                    slice frequency given by probe_theta_bin
    'stm'     :     Calculate Theta(r,r',theta) and send directly to a 
                    numpy matrix (Straight-To-Matrix). Can't be rebinned
                    at a later date
    '''
    modelp.mode = 'rrprime'
    # modelp.mode = 'stm'

    '''
    theta bin size for constructing full r, r', theta matrix
    '''
    modelp.probe_theta_bin = 20.0

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
    pmp.model_padf.run(modelp)
