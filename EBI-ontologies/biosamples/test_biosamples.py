import unittest
import ols


#Overview of available Errors: https://docs.python.org/3/library/exceptions.html#exception-hierarchy
print("\n \n")
print("Start testing")

class testApi(unittest.TestCase):

    def test_getSample_idFound(self):
    def test_getSample_idNotFound(self):


    def test_getGroup_idFound(self):
    def test_getGroup_idNotFound(self):


    def test_queryApi_CorrectUrl(self):
    def test_queryApi_wrongUrl(self):


class testBioProduct(unittest.TestCase):
    def test_printDoc_Positiv(self):
    def test_printDoc_noDoc(self):

    def test_properties_Positiv(self):
    def test_properties_noProperty(self):

class testBioSample(unittest.TestCase):
    def test_deriveFrom(self):


class testBioSampleGroup(self):



if __name__ == '__main__':
    unittest.main()
