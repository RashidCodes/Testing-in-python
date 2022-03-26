# Unit testing in Python using the unittest library 
Source: https://docs.python.org/3/library/unittest.html

 
## Concepts

- <b>test fixture:</b> 
	A test fixture represents the <b>preparation</b> needed to perform one or more tests, and any associated cleanup actions. This may involve, for example, creating temporary or proxy databases, directories, or starting a server process.

- <b>test case:</b>
	A test case is the individual <b>unit</b> of testing. It checks for a specific response to a particular set of inputs. <code>unittest</code> provides a base clas, <code>TestCase</code>, which may be used to create new test cases.

- <b>test suite:</b>
	A test suite is a <b>collection</b> of test cases, test suites or both. It is used to aggregate tests that should be executed together.

- <b>test runner:</b>
	A test runner is a component which orchestrates the execution of tests and provides the outcome to the user. The runner may be a graphical interface, a textual interface, or return a special value to indicate the results of executing tests.









