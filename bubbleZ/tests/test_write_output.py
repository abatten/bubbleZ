import os
import pytest

import numpy as np
import h5py
from ..pipeline.utils import FileAlreadyExists
from ..pipeline import write_output

# Global Variables
TEST_DIR_PATH = os.path.abspath(os.path.dirname(__file__))     # Path to tests directory

hdf5_test_output = os.path.join(TEST_DIR_PATH, "hdf5_test_output.h5")
partIDs_test_output = os.path.join(TEST_DIR_PATH, "partIDs_test_output.h5")

particle_ids = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
particle_ids_set = set([1, 2, 3, 4, 5, 6, 7, 8, 9])


def test_converting_dict_to_attributes():
    attrs_dict = {
        "Z_Solar": 0.012663729,
        "C": 2.9979e10,
        "GRAVITY": 6.672e8,
    }
    with h5py.File(hdf5_test_output, "a") as f:
        dataset = f.create_dataset("Testing", data=particle_ids)
        write_output.convert_dict_to_hdf5_attributes(dataset, attrs_dict)
    os.remove(hdf5_test_output)

def test_converting_non_dict_to_attributes_should_fail():
    attrs_list = [0.012663729, 2.9979e10, 6.672e8]

    with h5py.File(hdf5_test_output, "a") as f:
        dataset = f.create_dataset("Testing", data=particle_ids)
        with pytest.raises(TypeError):
            write_output.convert_dict_to_hdf5_attributes(dataset, attrs_list)
    os.remove(hdf5_test_output)


def test_writing_particle_ids_from_array_to_file():
    write_output.write_particle_ids_to_file(partIDs_test_output, particle_ids)
    os.remove(partIDs_test_output)  

def test_writing_particle_ids_from_set_to_file():
    write_output.write_particle_ids_to_file(partIDs_test_output, particle_ids_set)
    os.remove(partIDs_test_output)    

def test_writing_particle_ids_to_existing_file_with_overwrite():
    file = open(partIDs_test_output, "a")
    file.close()

    write_output.write_particle_ids_to_file(partIDs_test_output, particle_ids, overwrite=True)
    os.remove(partIDs_test_output)

def test_writing_particle_ids_to_existing_file_without_overwrite_should_fail():
    file = open(partIDs_test_output, "a")
    file.close()

    with pytest.raises(FileAlreadyExists):
        write_output.write_particle_ids_to_file(partIDs_test_output, particle_ids)
    os.remove(partIDs_test_output)

def test_writing_particle_ids_to_file_with_all_attributes():
    header_info = {
        "Criteria": "Metallicity",
        "Value" : 0.001,
        "High/Low": "higher",
    }

    constants_info = {
        "Z_Solar": 0.012663729,
        "C": 2.9979e10,
        "GRAVITY": 6.672e8,
    }

    group_attrs = {
        "Header" : header_info,
        "Constants" : constants_info,
}
 
    dataset_attrs = {
        "VarDescription": "Unique particle identifier."
    }

    write_output.write_particle_ids_to_file(partIDs_test_output, particle_ids, 
        dataset_attrs=dataset_attrs, group_attrs=group_attrs)

    os.remove(partIDs_test_output)

def test_writing_particle_ids_to_file_with_non_dict_attributes_should_fail():
    header_info = ["Criteria", "Value", "High/Low"]
    constants_info = ["Z_Solar", "C", "GRAVITY"]

    group_attrs = [header_info, constants_info]
 
    dataset_attrs = ["VarDescription"]

    with pytest.raises(TypeError):
        write_output.write_particle_ids_to_file(partIDs_test_output, particle_ids, 
            dataset_attrs=dataset_attrs)
    os.remove(partIDs_test_output)

    with pytest.raises(TypeError):
       write_output.write_particle_ids_to_file(partIDs_test_output, particle_ids, 
           group_attrs=group_attrs)
    os.remove(partIDs_test_output)