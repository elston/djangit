#!/bin/bash

source /$PROJECT/.env/$PROJECT/bin/activate  
cd /$PROJECT/$PROJECT
# ..
gunicorn $PROJECT.wsgi:application \
    --workers=5 \
    --bind=0.0.0.0:8000 \
    --capture-output \
    --log-level=debug \
    --enable-stdio-inheritance    