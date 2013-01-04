#!/bin/sh
echo "0,10,20,30,40,50 * * * * `readlink -f $1`/RunDynDns.py
0 0 1,15 * * `readlink -f $1`/RunDynDns.py --force"
