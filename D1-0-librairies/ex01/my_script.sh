#!/bin/bash

LOG_FILE="install.log"
PYTHON_PATH="/usr/bin/python3"
REPO_URL="https://github.com/jaraco/path.git"
INSTALL_DIR="local_lib"

# pip version
python3 -m pip --version

# pip install
python3 -m pip install --force-reinstall git+$REPO_URL --target=$INSTALL_DIR > install.log 2>&1

# execute my_program
echo "executing program ..."
python3 my_program.py