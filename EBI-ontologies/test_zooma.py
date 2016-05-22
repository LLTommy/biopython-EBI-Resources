import unittest
import zooma


#Overview of available Errors: https://docs.python.org/3/library/exceptions.html#exception-hierarchy
print("\n \n")
print("Start testing")

class anotation(unittest.TestCase):
    def test_callZooma(self):
        self.assertRaises(LookupError, zooma.callZooma, "wrongURL")

    def test_searchForValue_wrong_input_argument(self):
        self.assertRaises(TypeError, zooma.searchForValue, 12)

    def test_searchForValueAndType_wrong_first_input_argument(self):
        self.assertRaises(TypeError, zooma.searchForValueAndType, 12, "organism")

    def test_searchForValueAndType_wrong_second_input_argument(self):
        self.assertRaises(TypeError, zooma.searchForValueAndType, "homo+sapiens", 13)

    def test_searchForValueAndType_correct(self):
        x=zooma.searchForValueAndType("homo+sapiens", "organism")
        self.assertTrue(type(x) is list)

    def test_searchForValueAndTypeInDatasource_correct_oneDatasource(self):
        x=zooma.searchForValueAndTypeInDatasource("homo+sapiens", "organism", ["efo"])
        self.assertTrue(type(x) is list)

    def test_searchForValueAndTypeInDatasource_correct_twoDatasources(self):
        x=zooma.searchForValueAndTypeInDatasource("homo+sapiens", "organism", ["efo", "atlas"])
        self.assertTrue(type(x) is list)

    def test_searchForValueAndTypeInDatasource_wrong_first_input_argument(self):
        self.assertRaises(TypeError, zooma.searchForValueAndTypeInDatasource, 12, "organism", ["efo"])

    def test_searchForValueAndTypeInDatasource_wrong_first_second_argument(self):
        self.assertRaises(TypeError, zooma.searchForValueAndTypeInDatasource, "homo+sapiens", 1, ["efo"])

    def test_searchForValueAndTypeInDatasource_wrong_first_third_argument(self):
        self.assertRaises(TypeError, zooma.searchForValueAndTypeInDatasource, "homo+sapiens", "organism", 1)

    def test_parseAnnotation_wrong_input_argument(self):
        self.assertRaises(TypeError, zooma.parseAnnotation, "string")

    def test_showAnnotation_wrong_input_argument(self):
        self.assertRaises(TypeError, zooma.showAnnotation, "string")

if __name__ == '__main__':
    unittest.main()
