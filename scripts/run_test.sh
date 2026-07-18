#!/bin/bash

cd /root/portfolio
$PWD/python3-virtualenv/bin/python -m unittest discover -v tests/
