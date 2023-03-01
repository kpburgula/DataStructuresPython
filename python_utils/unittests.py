import unittest
from selenium.webdriver import Chrome

driver = Chrome()


class SimpleAsserts(unittest.TestCase):
    # assertTrue: assertTrue(value1, optional_message)
    def test1(self):
        self.assertTrue(True, "It's not a Match.")
    # assertFalse: assertFalse(value1, optional_message)
    def test2(self):
        self.assertFalse(True, "It's not a Match.")
    # assertIs: assertIs(value1, value2, optional_message )
    def test3(self):
        self.assertIs("Selenium", "Python", "value do not Match.")
    # assertIsNot: assertIsNot(value1, value2, optional_message )
    def test4(self):
        self.assertIsNot("Python", "Python", "Value is Match.")
    # assertIsNone: assertIsNone(value, optional_message )
    def test5(self):
        self.assertIsNone(None, "It is not None")
    # assertIsNotNone: assertIsNotNone(value, optional_message )
    def test6(self):
        self.assertIsNotNone(None, "It is not None")
    # assertIsInstance: assertIsInstance(value, cls, optional_message )
    def test7(self):
        self.assertIsInstance(driver, Chrome, "Instance not matching")
    # assertNotIsInstance: assertNotIsInstance(value, cls, optional_message )
    def test8(self):
        self.assertNotIsInstance(driver, Chrome, "Instance matching")

class OperatorType(unittest.TestCase):
    # assertEqual: assertEqual(value1, value2, optional_message)
    def test1(self):
        self.assertEqual(1,2,"Here 1 is not equal 2")
    # assertNotEqual: assertNotEqual(value1, value2, optional_message)
    def test2(self):
        self.assertNotEqual(1,1,"1 is equal 1")
    # assertGreater: assertGreater (value1, value2, optional_message )
    def test3(self):
        self.assertGreater (1,3)
    # assertGreaterEqual: assertGreaterEqual (value1, value2, optional_message )
    def test4(self):
        self.assertGreaterEqual (4,5)
    # assertLess: assertLess (value1, value2, optional_message )
    def test5(self):
        self.assertLess (4,8)
    # assertLessEqual: assertLessEqual (value1, value2, optional_message )
    def test6(self):
        self.assertLessEqual (1,2)

class ArrayAsserts(unittest.TestCase):
    # Lists: assertListEqual(list1, list2, optional_message)
    def test1(self):
        self.assertListEqual([], [])
    # Tuples: assertTupleEqual(tuple1, tuple2, optional_message)
    def test2(self):
        self.assertTupleEqual((), ())
    # Sets: assertSetEqual(set1, set2, optional_message)
    def test3(self):
        self.assertSetEqual({1,2}, {1,2})
    # Dictionary: assertDictEqual(dict1, dict2, optional_message)
    def test4(self):
        self.assertDictEqual({1:2},{1:2})
    # assertIn: assertIn(value1, value2, optional_message)
    def test5(self):
        self.assertIn(1, [1,2])
    # assertNotIn: assertNotIn(value1, value2, optional_message)
    def test6(self):
        self.assertNotIn(1,[2,3])

        
if __name__ =="__main__":
    unittest.main()
