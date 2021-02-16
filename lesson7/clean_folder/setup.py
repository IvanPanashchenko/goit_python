from setuptools import setup, find_namespace_packages

setup (
    version='1.0.0',
    description='Script for sorted files',
    license= No License,
    packages=find_namespace_packages(),
    include_package_data=True,
    entry_points={'console_scripts':['clean-folder = clean_folder.clean:clean_f']})