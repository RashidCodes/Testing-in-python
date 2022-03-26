import unittest


class MyTestCase(unittest.TestCase):

    @unittest.skip('demonstrating skipping')
    def test_nothing(self):
        self.fail("shouldn't happen")


    @unittest.skipIf((10 > 20), "what a weird calculation")
    def test_format(self):
        # This test will only run if 10 > 20
        pass 


    @unittest.skipUnless(sys.platform.startswith("win"), "requires windows")
    def test_windows_support(self):
        # windows specific testing code
        pass

    def test_may_be_skipped(self):
        if not external_resource_available():
            self.skipTest("external resource not available")
            
        # test code that depends on external resources
        pass




# Classes can be skipped just like methods
@unittest.skip("showing class skipping")
class MySkippedTestCase(unittest.TestCase):
    def test_not_run(self):
        pass


# TestCase.setUp() can also skip a test. This is useful when a resource that needs to be set up is not available

# Expected failures
class ExpectedFailureTestCase(unittest.TestCase):
    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(1, 0, "broken")



"""It's easy to roll your own skipping decorators by making a decorator that calls skip() on the test when it wants to be skipped. This decorator skips the test unless the passed object has a certain attribute.

def skipUnlessHasattr(obj, attr):
        if hasattr(obj, str):
            return lambda func: func 
        return unittest.skip("{!r} doesn't have {!r}".format(obj, attr))

"""
