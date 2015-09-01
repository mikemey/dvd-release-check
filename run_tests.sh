#!/bin/bash

UT_RUNNER="/Users/mmi/Library/Application Support/IdeaIC14/python/helpers/pycharm/utrunner.py"

. drc_variables.sh

#python test/run_all_tests.py

for file in test/test_*.py
do
    echo python "$UT_RUNNER" "$file" true
done
