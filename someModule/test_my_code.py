from my_code import return_hello 
import unittest 


"""
Food for your thoughts 
-----------------------
The order in which the various tests will be run is determined by sorting the test method names
with respect to the built-in ordering for strings
"""

class TestReturnHello(unittest.TestCase):

    # The testing framework will automatically call this function for every single test run
    def setUp(self):
        print("Hi rashid, I'm setting your tests up")


    def test_return_hello(self):
        self.assertEqual(return_hello(), "Hello world")

    # The testing framework will call this function if the setUp() method succeeded, whether the test succeeded or not
    def tearDown(self):
        print("Hi rashid, tearing your test donw")
    

# Uncomment this if you want unittest to run your test cases for you
#if __name__ == '__main__':
#    unittest.main()


# In most cases, calling unittest.main() will do the right thing and collect all the module's test cases
# for you and execute them.

# However, should you want to customize the building of your test suite, you can do it yourself.
def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestReturnHello('test_return_hello'))
    return suite 

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
