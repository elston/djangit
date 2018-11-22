#!/bin/sh

set -e

# Perform all actions as $POSTGRES_USER
export PGUSER="$POSTGRES_USER"


# Create $DB_NAME
echo "====> Create database $DB_NAME"
# ..
"${psql[@]}" \
--set DB_NAME="$DB_NAME" \
--set DB_USER="$DB_USER" \
--set DB_PASSWORD="'$DB_PASSWORD'" \
<<-'EOSQL'
    create database :DB_NAME template DEFAULT;
    create user :DB_USER with encrypted password :DB_PASSWORD;
    grant all privileges on database :DB_NAME to :DB_USER;
EOSQL