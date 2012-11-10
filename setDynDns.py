import urllib
import settings

class setDynDns:
	def __init__(self, ipaddress):
		self._http = urllib.urlopen('https://%s:%s@members.dyndns.org:443/nic/update?hostname=%s&myip=%s' % (settings.username, settings.password, settings.web_address, ipaddress))
		self._inputipaddress = ipaddress
		self._responseRead = False

	def _getResponse(self):
		if not self._responseRead:
			response = self._http.read()
			self._retcode = response.split(' ')[0]
			self._retip = response.split(' ')[1]
			self._responseRead = True

	def Passed(self):
		self._getResponse()
		return self._retcode == 'good' and self._retip == self._inputipaddress 

	def getReturnCode(self):
		self._getResponse()
		return self._retcode

