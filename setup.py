#!/usr/bin/env python

from setuptools import setup,find_packages

setup(name='indigo',
        version='0.1',
        description='custom package for helper functions',
        author='Gautham Adamane Pallathadka',
        author_email='gadaman1@jh.edu',
        license='MIT',
        url='https://github.com/ap-gautham/indigo',
        package_dir = {"" : "src"},
        package_data = {'indigo':['data/*']},
        packages=find_packages(where='src'),
        dependency_links = [],
        install_requires=['numpy', 'scipy', 'matplotlib', 'astropy'],
        include_package_data=True)