import unittest
import ols


#Overview of available Errors: https://docs.python.org/3/library/exceptions.html#exception-hierarchy
print("\n \n")
print("Start testing")

class searchFunction(unittest.TestCase):
    def test_callsOLSearch_wrong_URL(self):
        self.assertRaises(LookupError, ols.callOLSsearch, "nothing", "wrong")

    def test_searchForIriInOntology_wrongIRI(self):
        self.assertRaises(LookupError, ols.searchForIriInOntology,"xxx","efo")
    def test_searchForIriInOntology_wrongOntology(self):
        self.assertRaises(LookupError, ols.searchForIriInOntology,"http://www.ebi.ac.uk/efo/EFO_0001443","xxx")


    #Calling a bunch of somewhat random ontologies to test the function
    def test_searchEFO_positiv(self):
        ols.searchForOntology("efo")
    def test_searchHB_positiv(self):
        ols.searchForOntology("hp")
    def test_searchHB_positiv(self):
        ols.searchForOntology("aeo")
    def test_searchHB_positiv(self):
        ols.searchForOntology("atol")
    def test_searchHB_positiv(self):
        ols.searchForOntology("chebi")


class parseFunctions(unittest.TestCase):

    def test_parseIriandOntologyRequest_wrongArgument(self):
        self.assertRaises(TypeError, ols.parseIriandOntologyRequest, ["wrong structure"])
    def test_parseOntologyData_wrongArgument(self):
        self.assertRaises(TypeError, ols.parseOntoloyData,"Nothing")

    #def test_parseIriandOntologyRequest_correct(self): #not really necessary


class showFunction(unittest.TestCase):
    #Testing showTermList - unclear why this is not working
    #def test_showTermList(self):
    #    self.assertRaises(ValueError, ols.showTermList)

    def test_showTerm_noTerm(self):
        self.assertRaises(AttributeError, ols.showTerm, "Just a string")

    #Testing showTermByIri
    def test_showTermByIri_notFound(self):
        self.assertRaises(NameError,ols.showTermByIri, "http://purl.obolibrary.org/obo/HP_000478239")

    def test_showTermByIri_found(self):
        ols.searchforlabel("lactose")
        reply=ols.showTermByIri("http://purl.obolibrary.org/obo/HP_0004789")

    #Testing showTermByIndex
    def test_showTermByIndex_belowZero(self):
        self.assertRaises(ValueError, ols.showTermByIndex, -3)

    def test_showTermByIndex_found(self):
        ols.searchforlabel("lactose")
        reply=ols.showTermByIndex(2)


    def test_showTermByIndex_OutOfBounds(self):
        self.assertRaises(ValueError, ols.showTermByIndex, 100000)

    #Testing showOntology
    def test_showOntology_wrongData(self):
        self.assertRaises(TypeError, ols.showOntoloy, ["just a random type"])


if __name__ == '__main__':
    unittest.main()
