#!/bin/bash
fullfile=`realpath $0`
d=$(dirname $fullfile)
export PYTHONPATH=$d/src
cd ~
code
