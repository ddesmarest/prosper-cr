#!/bin/bash
export PYTHONPATH=src
nosetests --with-cov --cov src/server --cov-config src/server/.coveragerc src/server
