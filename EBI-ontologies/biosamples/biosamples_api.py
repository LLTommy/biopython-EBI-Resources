import urllib
from lxml import etree

class Api:
    """Base class to get BioSamples and BioSamplesGroup usign the BioSample API"""

    __BASE_URL = 'https://www.ebi.ac.uk/biosamples/xml/'

    def __init__(self):
        pass

    def getSampleXml(self, accession):
        """Get the BioSample with specific id"""
        from .biosamples import BioSample
        url = self.__BASE_URL + 'sample/' + accession
        return self._queryapi(url)



    def getGroupXml(self, accession):
        """Get the BioSampleGroup with specific id"""
        from .biosamples import BioSampleGroup
        url = self.__BASE_URL + 'group/' + accession
        return self._queryapi(url)

    def getGroupSamples(self, accession, query="", sortby='relevance', sortorder='descending', pagesize=10, page=1):
        """Get the BioSamples accessions associated with the group"""
        baseurl = self.__BASE_URL
        url = '{baseurl}groupsamples/{accession}/query={query}&sortby={sortby}&sortorder={sortorder}&pagesize={pagesize}&page={page}'.format(**locals())
        self._printdoc(self._queryapi(url))

    def _queryapi(self,url):
        """Return the xml document parsed from the url"""
        urlDocument = urllib.request.urlopen(url)
        xmlRoot = etree.fromstring(urlDocument.read())
        urlDocument.close()
        return xmlRoot

    def _printdoc(self,doc):
        """Print the XML document"""
        print(etree.tostring(doc,pretty_print=True, method="xml"))

# if __name__ == "__main__":
#     api = Api()
#     api.getGroupSamples('SAMEG82620')
    
