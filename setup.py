from setuptools import setup, find_packages
from codecs import open
import os
import re

with open("README.rst", "r") as f:
    long_description = f.read()

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

def get_version():
    here = os.path.abspath(os.path.dirname(__file__))
    version_file = os.path.join(here, 'bubbleZ', '__version__.py')

    with open(version_file, "r") as vf:
        lines = vf.read()
        version = re.search(r"^_*version_* = ['\"]([^'\"]*)['\"]", lines, re.M).group(1)
        return version


bubbleZ_version = get_version()

setup(
    name='bubbleZ',
    version=bubbleZ_version,
    author='Adam Batten',
    author_email='adamjbatten@gmail.com',
    url='https://github.com/abatten/bubbleZ',
    project_urls={
        'Source Code': "https://github.com/abatten/bubbleZ"
        },
    description='Metallicity Bubbles in the IGM',
    long_description=long_description,
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8"
        "License :: OSI Approved :: BSD License",
        "Operating System :: MacOS",
        "Operating System :: Unix",
        ],
    package_dir={"bubbleZ": "bubbleZ"},
    packages=find_packages(),
    package_data={'bubbleZ': ['*.npz', '*.npy', '*.csv', "*.hdf5", ".*.h5"]},
    include_package_data=True,
    keywords=("Metallicity Astronomy IGM"),
)