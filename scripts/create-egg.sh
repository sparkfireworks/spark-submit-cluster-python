#!/bin/bash

SCRIPT_PATH=$(readlink -f $0)
CWD=$(dirname $SCRIPT_PATH)

python $CDW/../setup.py bdist_egg
