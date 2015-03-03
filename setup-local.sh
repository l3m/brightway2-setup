#!/usr/bin/env sh

hg clone ssh://hg@bitbucket.org/cmutel/brightway2-parameters
hg clone ssh://hg@bitbucket.org/cmutel/brightway2-calc
hg clone ssh://hg@bitbucket.org/cmutel/brightway2-data
hg clone ssh://hg@bitbucket.org/cmutel/brightway2-io

virtualenv .
source bin/activate
pip install -r brightway2-parameters/requirements.txt
pip install -r brightway2-calc/requirements.txt
pip install -r brightway2-data/requirements.txt
pip install -r brightway2-io/requirements.txt

ln -s brightway2-parameters/bw2parameters
ln -s brightway2-data/bw2data
ln -s brightway2-calc/bw2calc
ln -s brightway2-io/bw2io


