#Just an idea how to structure the code - here we could add the biosamples webservice call stuff
import urllib
from lxml import etree


class Api:

    __BASE_URL = 'https://www.ebi.ac.uk/biosamples/xml/'

    def __init__(self):
        pass

    def getSample(self, id):
        url = self.__BASE_URL + 'sample/' + id
        sampleObj = BioSample(self._queryapi(url))
        return sampleObj


    def getGroup(self, id):
        url = self.__BASE_URL + 'group/' + id
        groupObj = BioSampleGroup(self._queryapi(url))
        return groupObj


    @staticmethod
    def _queryapi(url):
        urlDocument = urllib.urlopen(url)
        xmlRoot = etree.fromstring(urlDocument.read())
        urlDocument.close()
        return xmlRoot


class BioProduct:

    _NS = "{http://www.ebi.ac.uk/biosamples/SampleGroupExport/1.0}"

    def __init__(self,doc):
        self._doc = doc

    def getRoot(self):
        return self._doc

    def printDoc(self):
        print etree.tostring(self._doc,pretty_print=True, method="xml")

    def getproperties(self):
        return self._doc.findall(self._NS + "Property")

    def getaccession(self):
        return self._doc.attrib['id']

class BioSample(BioProduct):

    type='sample'

    def __init__(self,doc):
        BioProduct.__init__(self,doc)
        self.ancestors = []
        self.cachedancestor = False

    def getderiveFrom(self):
        return self._doc.find(self._NS + "derivedFrom")

    def hasparent(self):
        return self.getderiveFrom() is not None

    def getorigin(self):
        ancestors = self.getderivationtree()
        if len(ancestors):
            return ancestors[-1]
        else:
            return ancestors

    def getderivationtree(self):
        if not self.cachedancestor:
            elem = self
            tempapi = Api()
            while elem.hasparent():
                parentAcc = elem.getderiveFrom().text
                elem = tempapi.getSample(parentAcc)
                self.ancestors.append(elem)
            self.cachedancestor=True
        return self.ancestors


    def printderivationtree(self):
        ancestors = self.getderivationtree()
        i = 1
        print self.getaccession()
        for elem in ancestors:
            print '\r' + i*'\t' + '|'
            print '\r' + i*'\t' + '+- ' + elem.getaccession()
            i += 1

class BioSampleGroup(BioProduct):

    type='group'



api = Api()

sample = api.getSample('SAMEA4448577')
sampleorigin = sample.getorigin()
sample.printderivationtree()

