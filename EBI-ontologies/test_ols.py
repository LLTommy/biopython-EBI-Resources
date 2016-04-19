import unittest
import ols


#Overview of available Errors: https://docs.python.org/3/library/exceptions.html#exception-hierarchy
print("\n \n")
print("Start testing")

class searchFunction(unittest.TestCase):
    def test_callsOLSearch_wrong_URL(self):
        self.assertRaises(LookupError, ols.callOLSsearch, "nothing", "wrong")

class parseFunctions(unittest.TestCase):

    #def test_searchForIriInOntology_(self):

    def test_parseIriandOntologyRequest_wrongArgument(self):
        self.assertRaises(TypeError, ols.parseIriandOntologyRequest, ["wrong structure"])
    def test_parseOntologyData_wrongArgument(self):
        self.assertRaises(TypeError, ols.parseOntoloyData,"Nothing")

    #def test_parseIriandOntologyRequest_correct(self): #not really necessary


class showFunction(unittest.TestCase):
    #Testing showTermList - unclear why this is not working
    #def test_showTermList(self):
    #    self.assertRaises(ValueError, ols.showTermList)

    #Testing showTermByIri
    def test_showTermByIri_notFound(self):
        self.assertRaises(NameError,ols.showTermByIri, "http://purl.obolibrary.org/obo/HP_000478239")

    def test_showTermByIri_found(self):
        ols.searchforlabel("lactose")
        reply=ols.showTermByIri("http://purl.obolibrary.org/obo/HP_0004789")
        print(reply)
        self.assertEqual(reply,True)

    #Testing showTermByIndex
    def test_showTermByIndex_belowZero(self):
        self.assertRaises(ValueError, ols.showTermByIndex, -3) #To be done, checking for exception instead of true/false

    def test_showTermByIndex_found(self):
        ols.searchforlabel("lactose")
        reply=ols.showTermByIndex(2)
        self.assertEqual(reply,True)

    def test_showTermByIndex_OutOfBounds(self):
        self.assertRaises(ValueError, ols.showTermByIndex, 100000)




if __name__ == '__main__':
    unittest.main()
