import json
from setuptools import setup, find_namespace_packages

with open('osvimdriver/pkg_info.json') as fp:
    _pkg_info = json.load(fp)

with open("DESCRIPTION.md", "r") as description_file:
    long_description = description_file.read()

ignition_version = _pkg_info['ignition-version']

setup(
    name='os-vim-driver',
    version=_pkg_info['version'],
    author='IBM',
    description='Openstack implementation of a VIM driver',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/IBM/openstack-vim-driver",
    packages=find_namespace_packages(include=['osvimdriver*']),
    include_package_data=True,
    install_requires=[
        f'ignition-framework=={ignition_version}',
        'python-heatclient>=1.17.0,<2.0',
        'python-keystoneclient>=3.19.0,<4.0',
        'python-neutronclient>=6.5.1,<7.0',
        'python-novaclient>=13.0.0,<14.0.0',
        'tosca-parser @ git+https://github.com/IBM/tosca-parser.git@accanto',
        'heat-translator @ git+https://github.com/IBM/heat-translator.git@accanto-nfv',
        'gunicorn==20.1.0'
    ],
    entry_points='''
        [console_scripts]
        ovd-dev=osvimdriver.__main__:main
    '''
)
