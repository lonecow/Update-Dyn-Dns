#! /usr/bin/env python
import sys

#Delemitor name
DELEMITOR=sys.argv[1]
#old file
OLD_FILE=sys.argv[2]
#new file
NEW_FILE=sys.argv[3]
#extended data file
EXTENDED_DATA_FILE=sys.argv[4]


Start_String = '### START OF %s ####\n' % DELEMITOR
End_String = '### END OF %s ####\n' % DELEMITOR

old_file_fd = open(OLD_FILE, 'r')
new_file_fd = open(NEW_FILE, 'w')
extended_file_fd = open(EXTENDED_DATA_FILE, 'r')

for line in old_file_fd:
   if line != Start_String:
      new_file_fd.write(line)
   else:
      break;

new_file_fd.write('%s' % Start_String)

for line in extended_file_fd:
   new_file_fd.write(line)
 
new_file_fd.write('%s' % End_String)

for line in old_file_fd:
   if line == End_String:
      break;

for line in old_file_fd:
   new_file_fd.write(line)
