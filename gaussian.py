#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# PROGRAMMER:       Daniel Rines
# DATE CREATED:     2019.05.28
# REVISED DATE:     2019.05.28
# PURPOSE:  Function for calculating a Gaussian probablity.
#
# NOTES:    Program takes in three values:
#               1. mu - mean
#               2. sigma2 - variance
#               3. x - value
#
#   Example call:
#      python gaussian.py --mu <value> --sigma2 <value> --x <value>
##

import argparse
from math import sqrt, pi, exp


def get_input_args():
    """
    Retrieves and parses the command line arguments provided by the user when
    they run the program from a terminal window. This function uses Python's
    argparse module to created and defined these command line arguments. If
    the user fails to provide some or all of the arguments, then the default
    values are used for the missing arguments. 
    Command Line Arguments:
      1. mean --mu <float> 
      2. variance --sigma2 <float> 
      3. x --x <float>
    This function returns these arguments as an ArgumentParser object.
    Parameters:
     None - using argparse module to store command line arguments
    Returns:
     parse_args() -data structure that stores the command line arguments
    """
    # Create Parse using ArgumentParser
    parser = argparse.ArgumentParser(description='Calcs Gaussian.')
    # Create the command line arguments as mentioned above
    parser.add_argument('--mu',
                        type=float,
                        default=10.0,
                        help='Mean: (default: 10.0).')
    parser.add_argument('--sigma2',
                        type=float,
                        default=4.0,
                        help='Variance: (default: 4.0).')
    parser.add_argument('--x',
                        type=float,
                        default=8.0,
                        help='X Value: (default: 8.0).')

    # Return the parsed arguments back to the calling function
    return parser.parse_args()


def gaussian(mu, sigma2, x):
    """
    Calculates the gaussian probablity
    """
    norm = 1 / sqrt(2 * pi * sigma2)
    exponent = exp(-.5 * (x - mu)**2 / sigma2)
    
    return norm * exponent


def main():
    """
    The main function for call the gaussian function.
    PARAMETERS: None
    RETURNS:    None
    """
    # parse in the input arguments
    in_args = get_input_args()

    # call the posterior and print the result to the terminal
    prob = gaussian(in_args.mu, in_args.sigma2, in_args.x)
    print('The probability is: ' + str(prob))

# Call to main function to run the program
if __name__ == "__main__":
    main()