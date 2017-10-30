#!/bin/bash
export PYTHONPATH=src
#nosetests --with-cov --cov src/server --cover-xml --cover-xml-file=test.xml --cov-config src/server/.coveragerc src/server
nosetests --with-cov --cov src/server --cover-xml --cover-xml-file=test.xml src/server
