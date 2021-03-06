#!/bin/bash
fullfile=`realpath $0`
d=$(dirname $fullfile)
PYTHONPATH=$d/src
echo $PYTHONPATH
nosetests  --processes=0 --with-cov --cov $d/src/server --cov-config=$d/src/server/.coveragerc $d/src/server $@
result=$?
exit $result
