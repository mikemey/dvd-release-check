#!/bin/bash

. drc_variables.sh

if [ -z ${DRC_DESTINATION} ]; then
    echo Email settings not found!
    exit
fi

echo Email settings found!

python test.py