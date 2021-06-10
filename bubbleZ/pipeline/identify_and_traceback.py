

import h5py

import numpy as np

from pyx import io as pyxio


import write_output



def filter_particles_with_condition(
    snapshot, 
    field, 
    condition,
    
    saveout=None,
):
    """


    Returns
    -------
    particleIDs : set
        Contains the particle IDs within the snaphot that satify the 
        condition. 
    
    n_particles : int
        The number of particles that satify the contition.


    Example
    -------
    >>> filter_particles_with_contition

    """