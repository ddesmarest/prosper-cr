#!/bin/bash
fullfile=`realpath $0`
d=$(dirname $fullfile)
PYTHONPATH=$d/src
echo $PYTHONPATH
#nosetests  --processes=1 --process-restartworker --with-cov --cov src/server --cov-config=src/server/.coveragerc src/server $@
nosetests  --processes=0 --with-cov --cov $d/src/server --cov-config=$d/src/server/.coveragerc $d/src/server $@
result=$?
mongo tools/list_db.js
exit $result
