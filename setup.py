from setuptools import setup, find_packages

setup(
    name='geospatial_library',
    version='0.1.0',
    author='Your Name',
    description='A simple geospatial Python library for areas and distances.',
    packages=find_packages(),
    install_requires=[
        'geopandas>=0.10',
        'shapely>=1.7',
    ],
    python_requires='>=3.6',
    include_package_data=True,
    package_data={
        '': ['*.geojson'],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
