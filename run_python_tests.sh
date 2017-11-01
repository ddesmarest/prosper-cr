
#!/bin/bash

#fullfile=`realpath $0`
#d=$(dirname $fullfile)
export PYTHONPATH=src
echo $PYTHONPATH
tree
#nosetests  --processes=1 --process-restartworker --with-cov --cov src/server --cov-config=src/server/.coveragerc src/server $@
nosetests  --processes=0 --with-cov --cov src/server --cov-config=src/server/.coveragerc src/server $@
result=$?
mongo tools/list_db.js
exit $result
