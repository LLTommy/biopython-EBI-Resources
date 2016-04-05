import unittest
import ols

print("\n \n")
print("Start testing")

class showFunction(unittest.TestCase):
    print("showFunctionTest")

    def test_showTermByIri_notFound(self):
        reply=ols.showTermByIri("http://purl.obolibrary.org/obo/HP_000478239")
        print(reply)
        self.assertEqual(reply,False)

    def test_showTermByIriFalse_found(self):
        reply=ols.showTermByIri("http://purl.obolibrary.org/obo/HP_0004789")
        print(reply)
        self.assertEqual(reply,True)

    def test_showTermByIndex_belowZero(self):
        reply=ols.showTermByIndex(-3)
        print(reply)
        self.assertEqual(reply,False)
        #self.assertRaises(reply, mymod.myfunc) #To be done, checking for exception instead of true/false

    #def test_showTermByIndex_OutOfBounds(self):
    #    reply=ols.showTermByIndex(10)
    #    self.assertEqual(reply,False)


if __name__ == '__main__':
    unittest.main()
