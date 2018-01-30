#!/bin/bash -e

INIT_SEM=./initialized.sem

if [ ! -f $INIT_SEM ]; then
    django-admin startproject holamundo .
    touch $INIT_SEM
fi

pip install -r requirements.txt

while ! nc -z db 5432; do
    sleep 5
done

python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8000
