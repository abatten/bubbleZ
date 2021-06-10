import os
import pytest

import numpy as np
from ..pipeline.utils import FileAlreadyExists
from ..pipeline import write_output


def test_writing_particle_ids_to_existing_file_without_overwrite_should_fail():
    filename = "test_particleIDs.h5"
    file = open(filename, "a")
    file.close()

    particle_ids = set([1,2,3,4,5,6,7,8,9])

    with pytest.raises(FileAlreadyExists):
        write_output.write_particle_ids_to_file(filename, particle_ids)
    
    os.remove(filename)

def test_writing_particle_ids_to_file():
    filename = "test_particleIDs.h5"

    particle_ids = np.array([1,2,3,4,5,6,7,8,9])

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
        "VarDescription": "The unique particle identifier that satified the selection criteria."
    }

    write_output.write_particle_ids_to_file(filename, particle_ids, dataset_attrs=dataset_attrs, group_attrs=group_attrs)
    
    #os.remove(filename)