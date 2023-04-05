import unittest

class TestExample(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Setting up class")
    
    @classmethod
    def tearDownClass(cls):
        print("Tearing down class")
    
    def setUp(self):
        print("Setting up test")
    
    def tearDown(self):
        print("Tearing down test")
    
    def test_example_1(self):
        print("Running test 1")
        self.assertEqual(1+1, 2)
    
    def test_example_2(self):
        print("Running test 2")
        self.assertEqual(2+2, 4)
    
    @classmethod
    def setUpModule(cls):
        print("Setting up module")
    
    @classmethod
    def tearDownModule(cls):
        print("Tearing down module")
