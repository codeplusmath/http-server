#!/usr/bin/bash

python3 main.py &
echo $! > ../process/pid.txt
echo "CNServer started running successfully..."
