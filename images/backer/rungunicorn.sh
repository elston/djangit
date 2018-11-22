#!/bin/bash

BASE_DIR=/usr/local/lib/$BASE_PROJECT/$PROJECT
cd $BASE_DIR
source ./.env/$PROJECT/bin/activate
# ..
gunicorn wsgi:application \
    --workers=5 \
    --bind=0.0.0.0:8000 \
    --log-file=-