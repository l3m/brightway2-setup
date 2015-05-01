#!/usr/bin/env sh

hg clone https://bitbucket.org/cmutel/brightway2-parameters
hg clone https://bitbucket.org/cmutel/brightway2-calc
hg clone https://bitbucket.org/cmutel/brightway2-data
hg clone https://bitbucket.org/cmutel/brightway2-io

cd brightway2-data
hg update 2.0

ln -s brightway2-parameters/bw2parameters
ln -s brightway2-data/bw2data
ln -s brightway2-calc/bw2calc
ln -s brightway2-io/bw2io


