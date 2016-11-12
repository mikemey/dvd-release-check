#!/bin/bash

. drc_variables.sh

python src/drc_main.py > ./drc.log 2>&1
