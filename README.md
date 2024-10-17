
# Template Package Project

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
  - [System Requirements](#system-requirements)
  - [Installation Guide](#installation-guide)
  - [Run Unit Tests](#run-unit-tests)
- [Usage](#usage)
- [Project Directory Structure](#project-directory-structure)

## Introduction

This project is template package.

## Installation

### System Requirements

- Python >=3.10
- ...

### Installation Guide

1. Clone the repository:

```bash
https://github.com/giangnmt98/TemplatePackage
cd TemplatePackage
```

2. Install the required dependencies:

```bash
make venv
```

### Run Tests
```bash
make test
```

### Run styling
```bash
make style
```

## Usage
### Run the data processor
```bash
python3 dataprocessor/main.py --config_path <path_to_config_file>
````
### Auto create virtual environment and run the data processor
```bash
chmod +x auto_run.sh
./auto_run.sh --package_name dataprocessor --config_path <path_to_config_file>
````
## Project Directory Structure
```
TemplatePackage/
├── dataprocessor/
│   ├── __init__.py
│   ├── module1.py
│   ├── module2.py
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── test_module1.py
│   │   ├── test_module2.py
│   │   └── ...
│   └── ...
│
├── .github/
│   └── workflows/
│       └── project_ci.yaml
├── Makefile
├── README.md
└── setup.py
```

## Folder and File Descriptions
- `dataprocessor/`: Contains the main code modules.
- `dataprocessor/tests/`: Contains test modules.
- `.github/workflows/`: Contains GitHub Actions workflow files.
- `Makefile`: Makefile for setting up the environment, styling, and testing.
- `README.md`: Project documentation.
- `setup.py`: Python package setup file.
