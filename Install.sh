#!/bin/bash

Update_crontab()
{
   SCRIPT_DIR="`dirname @0`"

   DELIMITOR="DYNDNS CRONTAB CONFIGURATION"
   OLD_FILE="`tempfile -p crontab`"
   NEW_FILE="`tempfile -p crontab`"
   EXTENDED_DATA_FILE="`tempfile -p crontab`"

   $SCRIPT_DIR/templates/crontab.sh $SCRIPT_DIR > $EXTENDED_DATA_FILE

   crontab -u dyn-dns-update -l > $OLD_FILE

   $SCRIPT_DIR/FileReplace.py "$DELIMITOR" $OLD_FILE $NEW_FILE $EXTENDED_DATA_FILE

   crontab -u dyn-dns-update $NEW_FILE

   mv $OLD_FILE /tmp/crontab.bak
   echo "crontab move to /tmp/crontab.bak"

   rm -f $NEW_FILE
   rm -f $EXTENDED_DATA_FILE
}

if [ "`whoami`" != "root" ]; then
   echo "You do not have permissions to execute this command"
   exit 255
fi

useradd --system --shell /bin/false dyn-dns-update

touch /var/log/RunDynDns_log.txt
chown dyn-dns-update:dyn-dns-update /var/log/RunDynDns_log.txt

Update_crontab

