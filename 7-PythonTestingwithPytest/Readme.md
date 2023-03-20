- Source Article
    - Effective Python Testing With Pytest
    - https://realpython.com/pytest-python-testing/
- python -m pip install pytest
- If you’ve written unit tests for your Python code before, then you may have used Python’s built-in unittest module.
- Most functional tests follow the Arrange-Act-Assert model:

    - Arrange, or set up, the conditions for the test
    - Act by calling some function or method
    - Assert that some end condition is true
- Ex. code using unittest
# test_with_unittest.py

from unittest import TestCase

class TryTesting(TestCase):
    def test_always_passes(self):
        self.assertTrue(True)

    def test_always_fails(self):
        self.assertTrue(False)

-  All you need to do is include a function with the test_ prefix. Because you can use the assert keyword, you don’t need to learn or remember all the different self.assert* methods in unittest, either. If you can write an expression that you expect to evaluate to True, and then pytest will test it for you.

# test_with_pytest.py

def test_always_passes():
    assert True

def test_always_fails():
    assert False

- You can run your test suite using the pytest command from the top-level folder of your project

- the assert keyword is also powerful
- Ex. 
# test_assert_examples.py

def test_uppercase():
    assert "loud noises".upper() == "LOUD NOISES"

def test_reversed():
    assert list(reversed([1, 2, 3, 4])) == [4, 3, 2, 1]

def test_some_primes():
    assert 37 in {
        num
        for num in range(2, 50)
        if not any(num % div == 0 for div in range(2, num))
    }

- Easier to Manage State and Dependencies
- pytest leads you toward explicit dependency declarations that are still reusable thanks to the availability of fixtures. pytest fixtures are functions that can create data, test doubles, or initialize system state for the test suite.
Ex. 
# fixture_demo.py
import pytest

@pytest.fixture
def example_fixture():
    return 1

def test_with_fixture(example_fixture):
    assert example_fixture == 1
- Fixtures can also make use of other fixtures, again by declaring them explicitly as dependencies. Although the ability to insert fixtures into other fixtures provides enormous flexibility, it can also make managing dependencies more challenging as your test suite grows.

- Easy to Filter Tests
    - Name-based filtering: You can limit pytest to running only those tests whose fully qualified names match a particular expression. You can do this with the -k parameter.
    - Directory scoping: By default, pytest will run only those tests that are in or under the current directory.
    - Test categorization: pytest can include or exclude tests from particular categories that you define. You can do this with the -m parameter. pytest enables you to create marks, or custom labels, for any test you like.

- Allows Test Parametrization
    - When you’re testing functions that process data or perform generic transformations, you’ll find yourself writing many similar tests. They may differ only in the input or output of the code being tested.

- Has a Plugin-Based Architecture
    - Almost every piece of the program can be cracked open and changed. As a result, pytest users have developed a rich ecosystem of helpful plugins.

- Fixtures: Managing State and Dependencies
    - pytest fixtures are a way of providing data, test doubles, or state setup to your tests. Fixtures are functions that can return a wide range of values. ach test that depends on a fixture must explicitly accept that fixture as an argument.
    - If you find yourself writing several tests that all make use of the same underlying test data, then a fixture may be in your future. You can pull the repeated data into a single function decorated with @pytest.fixture to indicate that the function is a pytest fixture
- Ex.
    @pytest.fixture
    def example_people_data():
        return [
            {
                "given_name": "Alfonsa",
                "family_name": "Ruiz",
                "title": "Senior Software Engineer",
            },
            {
                "given_name": "Sayid",
                "family_name": "Khan",
                "title": "Project Manager",
            },
        ]
- used as below ->
def test_format_data_for_display(example_people_data):
    assert format_data_for_display(example_people_data) == [
        "Alfonsa Ruiz: Senior Software Engineer",
        "Sayid Khan: Project Manager",
    ]
- Avoiding Fixtures
- they aren’t always as good for tests that require slight variations in the data.
- Scale Fixtures
-  In pytest, fixtures are modular. Being modular means that fixtures can be imported, can import other modules, and they can depend on and import other fixtures. All this allows you to compose a suitable fixture abstraction for your use case.
- If you want to make a fixture available for your whole project without having to import it, a special configuration module called conftest.py will allow you to do that. pytest looks for a conftest.py module in each directory. If you add your general-purpose fixtures to the conftest.py module, then you’ll be able to use that fixture throughout the module’s parent directory and in any subdirectories without having to import it. 
- Another interesting use case for fixtures and conftest.py is in guarding access to resources

# conftest.py

import pytest
import requests

@pytest.fixture(autouse=True)
def disable_network_calls(monkeypatch):
    def stunted_get():
        raise RuntimeError("Network access not allowed during testing!")
    monkeypatch.setattr(requests, "get", lambda *args, **kwargs: stunted_get())

By placing disable_network_calls() in conftest.py and adding the autouse=True option, you ensure that network calls will be disabled in every test across the suite. Any test that executes code calling requests.get() will raise a RuntimeError indicating that an unexpected network call would have occurred.

- Marks: Categorizing Tests
- pytest enables you to define categories for your tests and provides options for including or excluding categories when you run your suite. You can mark a test with any number of categories.
- Ex. Marking tests is useful for categorizing tests by subsystem or dependencies. If some of your tests require access to a database, for example, then you could create a @pytest.mark.database_access mark for them.
    - If you’d like to run only those tests that require database access, then you can use pytest -m database_access. 
    - To run all tests except those that require database access, you can use pytest -m "not database_access". 
    - You can even use an autouse fixture to limit database access to those tests marked with database_access.
- You can use the --strict-markers flag to the pytest command to ensure that all marks in your tests are registered in your pytest configuration file, pytest.ini. It’ll prevent you from running your tests until you register any unknown marks.
- pytest provides a few marks out of the box:

    - skip skips a test unconditionally.
    - skipif skips a test if the expression passed to it evaluates to True.
    - xfail indicates that a test is expected to fail, so if the test does fail, the overall suite can still result in a passing status.
    - parametrize creates multiple variants of a test with different values as arguments. 
- get help using pytest --markers

- Parametrization: Combining Tests
- when you have several tests with slightly different inputs and expected outputs
- you can parametrize a single test definition, and pytest will create variants of the test for you with the parameters you specify.
- Ex.
def test_is_palindrome_empty_string():
    assert is_palindrome("")

def test_is_palindrome_single_character():
    assert is_palindrome("a")

def test_is_palindrome_mixed_casing():
    assert is_palindrome("Bob")

all above tests similar to ->
def test_is_palindrome_<in some situation>():
    assert is_palindrome("<some string>")

-> Use @pytest.mark.parametrize(comma-delimited string of parameter names,  list of either tuples or single values that represent the parameter value)
@pytest.mark.parametrize("palindrome", [
    "",
    "a",
    "Bob"
])
def test_is_palindrome(palindrome):
    assert is_palindrome(palindrome)

@pytest.mark.parametrize("maybe_palindrome, expected_result", [
    ("", True),
    ("a", True),
    ("Bob", True),
    ("Never odd or even", True),
    ("Do geese see God?", True),
    ("abc", False),
    ("abab", False),
])
def test_is_palindrome(maybe_palindrome, expected_result):
    assert is_palindrome(maybe_palindrome) == expected_result

- Durations Reports: Fighting Slow Tests
- pytest can automatically record test durations for you and report the top offenders.
- Use the --durations option to the pytest command to include a duration report in your test results. --durations expects an integer value n and will report the slowest n number of tests. you can increase the report verbosity and show these by passing -vv together with --durations
- Ex. pytest --durations=5

- Useful pytest Plugins
- pytest-randomly
- pytest-randomly forces your tests to run in a random order. pytest-randomly forces your tests to run in a random order. This is a great way to uncover tests that depend on running in a specific order, which means they have a stateful dependency on some other test.  Use seed value in configuration description to run tests in same order.
- pytest-cov
- pytest-cov integrates coverage, so you can run pytest --cov to see the test coverage report. It measure how well your tests cover your implementation code
- pytest-django
- provides a handful of useful fixtures and marks for dealing with Django tests. 
- pytest-bdd
- Behavior-driven development (BDD) encourages writing plain-language descriptions of likely user actions and expectations, which you can then use to determine whether to implement a given feature. pytest-bdd helps you use Gherkin to write feature tests for your code.





