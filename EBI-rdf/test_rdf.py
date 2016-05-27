#testclass for rdf
import unittest
import rdf
import variables

#Some variables
chembl="https://www.ebi.ac.uk/rdf/services/chembl/servlet/query?query="


#Overview of available Errors: https://docs.python.org/3/library/exceptions.html#exception-hierarchy
print("\n \n")
print("Start testing")



class searchFunction(unittest.TestCase):
    def test_callService_wrong_URL(self):
        self.assertRaises(LookupError, rdf.callService, "nothing", "wrongquery")

    def test_callService_wrong_query(self):
        self.assertRaises(LookupError, rdf.callService, variables.chembl, "NoOptionsAdded")
        #Change return type here


if __name__ == '__main__':
    unittest.main()
