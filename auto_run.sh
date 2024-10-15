#!/bin/bash

# Default values
PACKAGE_NAME=""

# Parse arguments
while [[ "$#" -gt 0 ]]; do
    case $1 in
        --packagename) PACKAGE_NAME="$2"; shift ;;
        *) echo "Unknown parameter passed: $1"; exit 1 ;;
    esac
    shift
done

# Check if PACKAGE_NAME is set
if [ -z "$PACKAGE_NAME" ]; then
    echo "Error: --packagename parameter is required."
    exit 1
fi

# Export package name
export PACKAGE_NAME=${PACKAGE_NAME}
make venv PACKAGE_NAME=${PACKAGE_NAME}
source ${PACKAGE_NAME}_env/bin/activate && python3 ${PACKAGE_NAME}/main.py