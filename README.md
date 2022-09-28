[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Build Status](https://travis-ci.com/IBM/openstack-vim-driver.svg?branch=main)](https://travis-ci.com/IBM/openstack-vim-driver)

# Openstack VIM Driver

A VIM driver implementation that manages infrastructure with Openstack. Create/delete operations are managed through the Heat Orchestration API and supports templates written in both Heat or TOSCA, by first translating the template into a Heat template.

Currently the only external infrastructure that can be returned by the "find infrastructure" API is Networks.

Please read the following guides to get started with the VIM Driver:

## Developer

- [Developer Docs](./developer_docs/index.md) - docs for developers to install the driver from source or run the unit tests

## User

- [User Guide](./docs/index.md) 
