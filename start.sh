#!/usr/bin/bash

python3 ./src/main.py &
echo $! > ./process/pid.txt
echo "CNServer started running successfully..."
