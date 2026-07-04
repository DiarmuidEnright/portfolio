#!/bin/bash

cd ~/portfolio

git pull origin main

source python3-virtualenv/bin/activate

pip install -r requirements.txt

tmux kill-session -t flask_app

tmux new-session -d -s flask_app "source python3-virtualenv/bin/activate && flask run --host=0.0.0.0"
