#!/usr/bin/env python

import setuptools,find_packages

if __name__ == "__main__":
    setup(name='indigo',
        version='0.1',
        description='custom package for helper functions',
        author='Gautham Adamane Pallathadka',
        author_email='gadaman1@jh.edu',
        license='MIT',
        url='https://github.com/vedantchandra/corv',
        package_dir = {"" : "src"},
        packages=find_packages(where='src'),
        package_data={'corv':['models/*']},
        dependency_links = [],
        install_requires=['numpy', 'scipy', 'lmfit', 'matplotlib', 'astropy', 'tqdm'],
        include_package_data=True)