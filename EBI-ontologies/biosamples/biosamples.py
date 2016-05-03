#Just an idea how to structure the code - here we could add the biosamples webservice call stuff
from lxml import etree
from .biosamples_api import Api

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
        print(etree.tostring(self._doc,pretty_print=True, method="xml"))

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
                elem = BioSample(tempapi.getSampleXml(parentAcc))
                self.ancestors.append(elem)
            self.cachedancestor=True
        return self.ancestors


    def printderivationtree(self):
        """Nicely printed derivation tree"""
        ancestors = self.getderivationtree()
        i = 1
        print(self.getaccession())
        for elem in ancestors:
            print('\r' + i*'\t' + '|')
            print('\r' + i*'\t' + '+- ' + elem.getaccession())
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
    sample = BioSample(api.getSampleXml('SAMEA4448577'))
    sample.printDoc()
    sampleorigin = sample.getorigin()
    sample.printderivationtree()
    

