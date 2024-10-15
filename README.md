
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
git clone https://github.com/xxxxxxx
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


## Project Directory Structure

```
TemplatePackage/
├── .github/
│   └── workflows/
│       └── project_ci.yaml
├── csvreader/
├── Makefile
├── README.md
└── setup.py
```

### Folder and File Descriptions

- **.github/workflows/**: Contains GitHub Actions workflow files for CI/CD.
- **csvreader/**: Directory containing the main source code for the project.
- **csvreader/tests/**: Directory containing test cases for the project.
- **Makefile**: File containing make commands for setting up the environment, running tests, and styling the code.
- **README.md**: This file, providing an overview and instructions for the project.
- **pyproject.toml**: Script for setting up the package and its dependencies.
