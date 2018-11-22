#!/bin/sh

BASE_DIR=/usr/local/lib/$PROJECT/$CONTAINER
cd $BASE_DIR
yarn install

# ..ugly hack
rm ./node_modules/flow-bin/flow-linux64-v0.86.0/flow
ln -s ln -s /usr/bin/flow ./node_modules/flow-bin/flow-linux64-v0.86.0/flow