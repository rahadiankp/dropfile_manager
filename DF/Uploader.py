from DF.Ui import *
import requests

class Upload:
	def setLink(self, link):
		self.link = link

	def getLink(self):
		return self.link

	def upload(self):
		try:
			req = requests.post('https://dropfile.to/upload', files={'file':open(self.link, 'rb')})
			if(req.json()['status']==0 and req.status_code==200):
				return {
							'status' : 0,
							'dropID' : req.json()['url'],
							'aKey' : req.json()['access_key']
				}
			else:
				return {'status' : 1}
		except requests.exceptions.ConnectionError:
			return { 'status' : 2 }
