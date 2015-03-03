#!/usr/bin/env bash

apt-get update
apt-get install -y python2.7 python-pip python2.7-dev python-lxml python2.7-numpy python2.7-scipy
pip install -r /vagrant/brightway2-data/requirements.txt
pip install -r /vagrant/brightway2-io/requirements.txt
