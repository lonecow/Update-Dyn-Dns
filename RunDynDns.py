#!/usr/bin/env python

import getopt
import sys
from setDynDns import setDynDns
from get_wan import getWan

def usage():
	print """RunDynDns.py
	-h	--help		displays this message
	-v	--verbose	displays verbose messages
	-f	--force		forces update of dyndns"""

try:
	opts, args = getopt.getopt(sys.argv[1:], "hvf", ["help", "verbose", "force"])
except getopt.GetoptError as err:
	# print help information and exit:
	print(err) # will print something like "option -a not recognized"
	usage()
	sys.exit(2)
verbose = False
Force = False
for o, a in opts:
	if o in ("-v", "--verbose"):
		verbose = True
	elif o in ("-h", "--help"):
		usage()
		sys.exit()
	elif o in ("-f", "--force"):
		Force = True
	else:
		assert False, "unhandled option"

log_file = open('./RunDynDns_log.txt','a')

getIp = getWan()

if (getIp.isIpAddressValid() and getIp.hasIpAddressChanged()) or Force == True:
	if getIp.isIpAddressValid() and not Force:
		update = setDynDns(getIp.getIpAddress())
		log_file.write("Sending Out Change in IP OLD[%s]:New[%s] Ret Code [%s]\n" % (getIp.getLastIPAddress(), getIp.getIpAddress(), update.getReturnCode()))
	elif getIp.isIpAddressValid() and Force:
		update = setDynDns(getIp.getIpAddress())
		log_file.write("Sending Out Change in IP OLD[%s]:New[%s] Ret Code [%s] By Force\n" % (getIp.getLastIPAddress(), getIp.getIpAddress(), update.getReturnCode()))
	elif Force:
		update = setDynDns(getIp.getLastIPAddress())
		log_file.write("Sending Out Change in IP OLD[%s]:New[%s] Ret Code [%s] By Force\n" % (getIp.getLastIPAddress(), getIp.getIpAddress(), update.getReturnCode()))
		

log_file.close()
