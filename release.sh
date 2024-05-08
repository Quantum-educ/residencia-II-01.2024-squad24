#!/usr/bin/env sh

python escola_ez/manage.py makemigrations --noinput
python escola_ez/manage.py migrate --noinput
python escola_ez/manage.py collectstatic --noinput
python escola_ez/manage.py runserver 0.0.0.0:8000
