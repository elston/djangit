#!/bin/bash
# ..
BASE_DIR=/usr/local/lib/$BASE_PROJECT/$PROJECT
cd $BASE_DIR
# ..
source ./.env/$PROJECT/bin/activate
python3 ./manage.py migrate