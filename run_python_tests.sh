#!/bin/bash
fullfile=`realpath $0`
d=$(dirname $fullfile)
PYTHONPATH=$d/src
echo $PYTHONPATH
find . -name '*.pyc' -exec rm {} \;
nosetests  --processes=0 --with-cov --cov $d/src/server --cov-config=$d/src/server/.coveragerc   $@
result=$?
mongo tools/list_db.js
mongo tools/drop_db.js
exit $result
