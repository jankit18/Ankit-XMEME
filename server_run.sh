#!/bin/bash
cd XMEME

python3 manage.py sqlflush | python3 manage.py dbshell
python3 manage.py migrate  
python3 manage.py runserver 8081
