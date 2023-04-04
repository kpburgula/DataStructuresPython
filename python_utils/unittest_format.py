import unittest

# Define a test case by creating a subclass of unittest.TestCase
class MyTestCase(unittest.TestCase):
    
    # Define a test fixture by adding a method named setUp
    def setUp(self):
        # Set up any resources needed by the test case
        self.my_var = "foo"
        
    # Define a test case by adding a method starting with "test_"
    def test_something(self):
        # Perform some action to test
        result = self.my_var.upper()
        # Use assertions to check that the result is correct
        self.assertEqual(result, "FOO")
        
    # Define another test case
    def test_another_thing(self):
        result = len(self.my_var)
        self.assertEqual(result, 3)
    
    # Define a test fixture cleanup by adding a method named tearDown
    def tearDown(self):
        # Clean up any resources created by the test case
        self.my_var = None

# Create a test suite by instantiating unittest.TestSuite
suite = unittest.TestSuite()

# Add test cases to the suite by passing their names as strings
suite.addTest(MyTestCase("test_something"))
suite.addTest(MyTestCase("test_another_thing"))

# Create a test runner and run the suite
runner = unittest.TextTestRunner()
result = runner.run(suite)

# Print a summary of the test results
print(f"Ran {result.testsRun} tests in {result.totalTime:.3f}s")
if result.wasSuccessful():
    print("All tests passed!")
else:
    print(f"{len(result.failures)} tests failed:")
    for test, error in result.failures:
        print(f" - {test.id()}: {error}")
