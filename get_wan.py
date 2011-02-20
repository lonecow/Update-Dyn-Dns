import urllib
import re

class getWan:
	def __init__(self):
		self._http = urllib.urlopen('http://www.whatismyip.com/automation/n09230945.asp')
		self._responseRead = False
		self._lastIpRead = False
		pass

	def _getResponse(self):
		if not self._responseRead:
			response = self._http.read()
			self._retip = response
			self._responseRead = True
			self._http.close()
	
	def _ReadLastAddr(self):
		if not self._lastIpRead:
			self._last_ip = ''
			try:
				ipFile = open('/tmp/wanip', 'r')
				self._last_ip = ipFile.read()
				ipfile.close()
			except:
				pass
			self._lastIpRead = True
		return self._last_ip

	def isIpAddressValid(self):
		self._getResponse()
		ip_regex = re.compile("(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)")
		return None != ip_regex.match(self._retip)

	def getIpAddress(self):
		self._getResponse()
		return self._retip

	def getLastIPAddress(self):
		return self._ReadLastAddr()

	def hasIpAddressChanged(self):
		if self._ReadLastAddr() != self.getIpAddress() and self.isIpAddressValid():
			ipFile = open('/tmp/wanip', 'w')
			ipFile.write(self.getIpAddress())
			ipFile.close()
			return True
		else:
			return False
