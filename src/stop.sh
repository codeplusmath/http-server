#!/usr/bin/bash

pid=`cat ../process/pid.txt`
kill $pid
rm ../process/pid.txt
echo 'CNServer Stopped running successfully...'
