import unittest
import zooma


#Overview of available Errors: https://docs.python.org/3/library/exceptions.html#exception-hierarchy
print("\n \n")
print("Start testing")

class anotation(unittest.TestCase):
    def test_callZooma(self):
        self.assertRaises(LookupError, zooma.callZooma, "wrongURL")

    def test_predictAnnotation_wrong_input_argument(self):
        self.assertRaises(TypeError, zooma.predictAnnotation, 12)

    def test_parseAnnotation_wrong_input_argument(self):
        self.assertRaises(TypeError, zooma.parseAnnotation, "string")

    def test_showAnnotation_wrong_input_argument(self):
        self.assertRaises(TypeError, zooma.showAnnotation, "string")

if __name__ == '__main__':
    unittest.main()
