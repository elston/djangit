#!/bin/bash

BASE_DIR=/usr/local/lib/$PROJECT/$CONTAINER

mkdir -p $BASE_DIR/.env
cd $BASE_DIR/.env
# ..
virtualenv $CONTAINER
source $CONTAINER/bin/activate
pip install -r /tmp/requirements.txt

# ...logs
mkdir -p $BASE_DIR/.logs
echo '' > $BASE_DIR/.logs/main.log