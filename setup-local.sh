#!/usr/bin/env sh

hg clone https://bitbucket.org/cmutel/brightway2
hg clone https://bitbucket.org/cmutel/brightway2-parameters
hg clone https://bitbucket.org/cmutel/brightway2-calc
hg clone https://bitbucket.org/cmutel/brightway2-data
hg clone https://bitbucket.org/cmutel/brightway2-io

cd brightway2-data
hg update 2.0
cd ..

cd brightway2
hg update 2.0
cd ..


