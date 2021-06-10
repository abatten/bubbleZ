"""
write_output
============

Author: Adam Batten, 2021
"""

import os
from .utils import FileAlreadyExists

import numpy as np
import h5py


def convert_dict_to_group_in_hdf5_file(hdf5_file, attrs_dict, group_name):
    """
    Creates a new group in a hdf5 file and writes a dictionary as
    attributes of that group.

    Parameters
    ----------
    hdf5_file: An open HDF5 file (h5py._hl.files.File)
        The open HDF5 file to add the new group into

    attrs_dict: dict
        The attributes of the new group.

    group_name: str
        The name of the new group.

    """

    hdf5_file.create_group(group_name)
    group = hdf5_file[group_name]

    convert_dict_to_hdf5_attributes(group, attrs_dict)


def convert_dict_to_hdf5_attributes(item, attrs_dict):
    """
    Adds attributes from a dictionary to a HDF5 dataset or group. 
    The attributes will be automatically sorted into alphabetical
    order.

    Parameters
    ----------
    item: A dataset or group from an open HDF5 file (h5py._hl.files.File)
        The dataset or group to attach the attributes.

    attrs_dict: dict
        The attributes of the data set or group. The key is the name 
        of the attribute.

    """
    if not isinstance(attrs_dict, dict):  # Must be a dict!
        raise TypeError("attrs_dict must be a dictionary") 

    # Sort into alphabetical order
    attributes = sorted(attrs_dict.items())
    for key, value in attributes:
        item.attrs[key] = value


def write_particle_ids_to_file(
    filename, particle_ids, overwrite=False, 
    dataset_attrs=None, group_attrs=None
    ):
    """
    Checks to see if the file already exists. If so, it will skip
    unless `overwrite=True`.

    Parameters:
    -----------
    filename: str
        The name of the output HDF5 file.

    particle_ids: set or np.ndarray
        Contains the particle IDs that are to be written to file.

    overwrite: bool, optional
        If a file aready exists with filename, then overwrite that file.
        Default: False. 

    dataset_attrs: dict, optional
        Attributes of the `particle_ids` dataset. These attributes are a
        dictionary with the key representing the name of the attribute.
        Default: None

    group_attrs: dict, optional
        Group attributes to be written to the file. These `group_attrs`
        must be a dict with the key representing the name of the new 
        group and the value another dictionary containing all the 
        attributes of the group. Default: None

    """

    # Check if the file already exists and if we can overwrite the file.
    if os.path.isfile(filename) and not overwrite:
        msg = f"{filename} already exists and overwrite=False. Will not overwrite!"
        raise FileAlreadyExists(msg)

    else:
        with h5py.File(filename, "w") as output:

            # If there are group attributes, write them to file first
            if group_attrs is not None:
                if not isinstance(group_attrs, dict):  # Must be a dict!
                    raise TypeError("group_attrs must be a dictionary")

                else:
                    # Write groups in alphabetical order
                    group_attrs = sorted(group_attrs.items())
                    for group_name, attrs in group_attrs:
                        convert_dict_to_group_in_hdf5_file(output, attrs, group_name)

            # Since you can't save a set to a HDF5 dataset, convert to np.array
            if isinstance(particle_ids, set):
                particle_ids = np.array(list(particle_ids))

            # Create the Particle IDs dataset and write attributes
            pIDs_dataset = output.create_dataset('ParticleIDs', data=particle_ids)
            if dataset_attrs is not None:
                if not isinstance(dataset_attrs, dict):  # Must be a dict!
                    raise TypeError("dataset_attrs must be a dictionary")
                else:
                    convert_dict_to_hdf5_attributes(pIDs_dataset, dataset_attrs)
