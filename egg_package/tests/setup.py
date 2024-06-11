import setuptools


setuptools.setup(
	name="klarfio",
	version="0.9",
	author="hadriman",
	description="Minimalist python module to read and write klarf files",
	url='https://github.com/hadriman/klarfio',
	packages=["klarfio"],
	license="GPL-3.0 license",
	keywords=["klarf","defect","wafer","parser","read","write","v1.8","v1.2"],
	long_description="""Minimalist python library to read and write Klarf v1.8 and v1.2 files.
This module is a pure python module, there are no dependencies outside the standard library.
The idea is that once the data is loaded, you can copy the defects data into a numpy array or a pandas dataframe for further processing.

The data of the klarf file is held in a nested dictionnary that follows closely the structure of the klarf files.
""",
	)