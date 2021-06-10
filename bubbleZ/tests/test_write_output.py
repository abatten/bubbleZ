import os
import pytest

import numpy as np
from ..pipeline.utils import FileAlreadyExists
from ..pipeline import write_output

# Global Variables
TEST_DIR_PATH = os.path.abspath(os.path.dirname(__file__))     # Path to tests directory

partIDs_test_output = os.path.join(TEST_DIR_PATH, "partIDs_test_output.h5")

particle_ids = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
particle_ids_set = set([1, 2, 3, 4, 5, 6, 7, 8, 9])


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