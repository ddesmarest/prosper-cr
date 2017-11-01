#!/bin/bash
fullfile=`realpath $0`
d=$(dirname $fullfile)
export PYTHONPATH=$d/src
nosetests --with-cov --cov src/server --cov-config=src/server/.coveragerc src/server $@
