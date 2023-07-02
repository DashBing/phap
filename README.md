# phap
### *Programing Helpful Algorithm Package*
### Powered by Python 3.11
[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat)](http://choosealicense.com/licenses/mit/)

### English  | [简体中文](README-zh-CN.md)

# Links
[Github](https://github.com/DashBing/phap/ "Github") | [Pypi](https://pypi.org/project/phap/ "Pypi") | [Pypi (stralgo)](https://pypi.org/project/stralgo/ "Pypi (stralgo)")

# Versions
## Stable Version
+ v0.1.0 (stralgo)
+ v1.1.1 (stralgo)
+ v2.1.2
+ v2.2.1

## Latest Available Version
+ v2.2.1

## Latest Version
### *(The data under the master branch is inaccurate. Please refer to the dev branch for details)*
+ v3.0.0-alpha2

# Build
## Precondition
+ Install git and make tools
+ Install Python(the version 3.9 or the version 3.11)
+ Clone source code from source repository
```
git clone git@github.com:DashBing/phap.git
```
### or
```
git clone https://github.com/DashBing/phap.git
```

## Initialize packaging environment
```
make init
```
#### or
#### Try to install the package:
+ build
+ twine
#### This is the example command on Windows:
```
python -m pip install build
python -m pip install twine
```

## Build release
```
make build
```
