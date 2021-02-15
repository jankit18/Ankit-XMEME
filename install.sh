#!/bin/bash

echo "Y" | sudo apt-update
echo "Y" | sudo apt install python3
echo "Y" | sudo apt install python3-pip
echo "Y" | pip3 install django
echo "Y" | pip3 install djangorestframework
echo "Y" | pip3 install -U drf-yasg 
