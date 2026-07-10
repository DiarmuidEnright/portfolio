#!/bin/bash

RAND_VAL=$RANDOM
CREATE_RESPONSE=$(curl -s -X POST http://localhost:5000/api/timeline_post -d "name=User$RAND_VAL" -d "email=user$RAND_VAL@test.com" -d "content=Content$RAND_VAL")

POST_ID=$(echo $CREATE_RESPONSE | tr -d ' ' | grep -Eo '"id":[0-9]+' | grep -Eo '[0-9]+')

curl -s http://localhost:5000/api/timeline_post

curl -s -X DELETE http://localhost:5000/api/timeline_post/$POST_ID
