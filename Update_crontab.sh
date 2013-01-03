#!/bin/sh

if [ "`whoami`" != "root" ];then
   echo "You do not have permissions to run this script"
   exit 255
fi

SCRIPT_DIR="`dirname @0`"

DELIMITOR="DYNDNS CRONTAB CONFIGURATION"
OLD_FILE="`tempfile -p crontab`"
NEW_FILE="`tempfile -p crontab`"
EXTENDED_DATA_FILE="$SCRIPT_DIR/crontab"

crontab -u rbitel -l > $OLD_FILE

$SCRIPT_DIR/FileReplace.py "$DELIMITOR" $OLD_FILE $NEW_FILE $EXTENDED_DATA_FILE

crontab -u rbitel $NEW_FILE

mv $OLD_FILE /tmp/crontab.bak
echo "crontab move to /tmp/crontab.bak"

rm -f $NEW_FILE
exit 0
