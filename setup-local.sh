#!/usr/bin/env sh

hg clone https://bitbucket.org/cmutel/brightway2-parameters
hg clone https://bitbucket.org/cmutel/brightway2-calc
hg clone https://bitbucket.org/cmutel/brightway2-data
hg clone https://bitbucket.org/cmutel/brightway2-io

virtualenv .
if [ "$(expr substr $(uname -s) 1 10)" == "MINGW32_NT" ]; then
    source Scripts/activate;
else
    source bin/activate;
fi
pip install -r brightway2-parameters/requirements.txt
pip install -r brightway2-calc/requirements.txt
pip install -r brightway2-data/requirements.txt
pip install -r brightway2-io/requirements.txt

ln -s brightway2-parameters/bw2parameters
ln -s brightway2-data/bw2data
ln -s brightway2-calc/bw2calc
ln -s brightway2-io/bw2io


