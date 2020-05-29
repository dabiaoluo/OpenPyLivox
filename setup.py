from setuptools import setup

setup(
    name='openpylivox_pkg',
    version='1.0.2',
    url='https://github.com/ryan-brazeal-ufl/openpylivox',
    author='Ryan Brazeal',
    author_email='ryan.brazeal@ufl.edu',
    packages=['openpylivox'],
    description='Python3 driver for Livox lidar sensors',    
    install_requires=['numpy >= 1.15.4', 'crcmod >= 1.7.0', 'deprecated >= 1.2.7'],
    python_requires='>=3.5',
)
