import unittest
import biosamples


#Overview of available Errors: https://docs.python.org/3/library/exceptions.html#exception-hierarchy
print("\n \n")
print("Start testing")

class testApi(unittest.TestCase):

    def test_queryApi_CorrectUrl(self):
        api = biosamples.Api()
        response = api._queryapi("https://www.ebi.ac.uk/biosamples/xml/sample/SAMEA4448577")
        #check if the right element/class is returned - might not be necessary

    def test_queryApi_wrongUrl(self):
        api = biosamples.Api()
        self.assertRaises(LookupError, api._queryapi, "No URL")


#    def test_getSample_idFound(self):
#        api = biosamples.Api()
#        sample = api.getSample('SAMEA4448577')
#        positive test, might not be that important

    def test_getSample_idNotFound(self):
        api = biosamples.Api()
        sample = api.getSample('FunnySample')
        print(sample)
        print("Comment: We get an instance back, but it is empty. We should find a way to check for that")

    #def test_getGroup_idFound(self):
    #def test_getGroup_idNotFound(self):

#class testBioProduct(unittest.TestCase):
    #def test_printDoc_Positiv(self):
    #def test_printDoc_noDoc(self):

    #def test_properties_Positiv(self):
    #def test_properties_noProperty(self):

#class testBioSample(unittest.TestCase):
    #def test_deriveFrom(self):


#class testBioSampleGroup(self):



if __name__ == '__main__':
    unittest.main()
