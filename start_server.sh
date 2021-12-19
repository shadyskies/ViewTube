#!/usr/bin/env bash
# start-server.sh

(cd core; python3 manage.py migrate; python3 manage.py runserver)