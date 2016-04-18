#Just an idea how to structure the code - here we could add the biosamples webservice call stuff
import urllib
from lxml import etree


class Api:

	__BASE_URL = 'https://www.ebi.ac.uk/biosamples/xml/'

	def getSample(self,id):
		url = self.__BASE_URL + 'sample/' + id
		sampleObj = BioSample(self._queryApi(url))
		return sampleObj

	def getGroup(self,id):
		url = self.__BASE_URL + 'group/' + id
		groupObj = BioSampleGroup(self._queryApi(url))
		return groupObj

	def _queryApi(self,url):
		file = urllib.urlopen(url)
		xmlRoot = etree.fromstring(file.read())
		file.close()
		return xmlRoot


class BioProduct:

	def __init__(self,doc):
		self._doc = doc

	def printDoc(self):
		print etree.tostring(self._doc,pretty_print=True, method="xml")

	def properties(self):
		print self._doc.get('property')


class BioSample(BioProduct):

	type='sample'
	
	def deriveFrom(self):
		print self._doc.get('deriveFrom')

class BioSampleGroup(BioProduct):

	type='group'

api = Api()

sample = api.getSample('SAMEA2398387')

sample.properties()
sample.deriveFrom()