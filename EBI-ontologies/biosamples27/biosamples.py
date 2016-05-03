import urllib2
from lxml import etree

class Api:
    """Base class to get BioSamples and BioSamplesGroup usign the BioSample API"""

    __BASE_URL = 'https://www.ebi.ac.uk/biosamples/xml/'

    def __init__(self):
        pass

    def getSample(self, accession):
        """Get the BioSample with specific id"""
        url = self.__BASE_URL + 'sample/' + accession
        sampleObj = BioSample(self._queryapi(url))
        return sampleObj


    def getGroup(self, accession):
        """Get the BioSampleGroup with specific id"""
        url = self.__BASE_URL + 'group/' + accession
        groupObj = BioSampleGroup(self._queryapi(url))
        return groupObj

    def getGroupSamples(self, accession, query="", sortby='relevance', sortorder='descending', pagesize=10, page=1):
        """Get the BioSamples accessions associated with the group"""
        baseurl = self.__BASE_URL
        url = '{baseurl}groupsamples/{accession}/query={query}&sortby={sortby}&sortorder={sortorder}&pagesize={pagesize}&page={page}'.format(**locals())
        self._printdoc(self._queryapi(url))

    def _queryapi(self,url):
        """Return the xml document parsed from the url"""
        urlDocument = urllib2.urlopen(url)
        xmlRoot = etree.fromstring(urlDocument.read())
        urlDocument.close()
        return xmlRoot

    def _printdoc(self,doc):
        """Print the XML document"""
        print etree.tostring(doc,pretty_print=True, method="xml")

class BioProduct:
    """Generic class representing both BioSamples and BioSamplesGroups"""

    _NS = "{http://www.ebi.ac.uk/biosamples/SampleGroupExport/1.0}"

    def __init__(self,doc):
        self._doc = doc

    def getRoot(self):
        """Get the document"""
        return self._doc

    def printDoc(self):
        """Print the XML document"""
        print etree.tostring(self._doc,pretty_print=True, method="xml")

    def getproperties(self):
        """Get all the properties"""
        return self._doc.findall(self._NS + "Property")

    def getaccession(self):
        """Return the BioProduct accession"""
        return self._doc.attrib['id']

class BioSample(BioProduct):

    type='sample'

    def __init__(self,doc):
        BioProduct.__init__(self,doc)
        self.ancestors = []
        self.cachedancestor = False

    def getderiveFrom(self):
        """Get BioSample parent"""
        return self._doc.find(self._NS + "derivedFrom")

    def hasparent(self):
        """Check if BioSample has a parent"""
        return self.getderiveFrom() is not None

    def getorigin(self):
        """Get BioSample origin"""
        ancestors = self.getderivationtree()
        if len(ancestors):
            return ancestors[-1]
        else:
            return ancestors

    def getderivationtree(self):
        """Get the list of ancestors for the BioSample """
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
        """Nicely printed derivation tree"""
        ancestors = self.getderivationtree()
        i = 1
        print self.getaccession()
        for elem in ancestors:
            print '\r' + i*'\t' + '|'
            print '\r' + i*'\t' + '+- ' + elem.getaccession()
            i += 1

class BioSampleGroup(BioProduct):

    type='group'
    
    def __init__(self,doc):
        BioProduct.__init__(self,doc)
        self.groupsamples = {}
        self.cachedsamples = False

    def samplenumber(self):
        tempapi = Api()


if __name__ == "__main__":
    """Inner Test suite"""
    api = Api()
    # api.getGroupSamples('SAMEG82620')
    sample = api.getSample('SAMEA4448577')
    sample.printDoc()
    sampleorigin = sample.getorigin()
    sample.printderivationtree()
    

