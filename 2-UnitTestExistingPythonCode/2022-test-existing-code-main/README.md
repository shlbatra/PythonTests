# How To Write Unit Tests For Existing Python Code

In this two-part miniseries, I show you a practical example of adding unit tests to existing code. This first part focuses on adding tests while not changing the original code. There are also a few things in the test setup that are not ideal, like how dates are used in the test code, using a real API key and doing actual card charges. I address these things in part 2, where I also show how refactoring the code simplifies test writing while improving the design as well.

NOTES:

1) There are a few things in the test setup that are not ideal, like how dates are used in the test code, using a real API key and doing actual card charges. I'll address these things in part 2.

2) patching means that you're replacing a dependency in a function or method by something else. The thing that you replace it with is called a mock (apologies, my use of the terms in the video is a bit messy).

- tests help you refactor code and design better - easy to test and change later on
- Ex. valid card number to test -> 1249190007575069
- Test -> how deal with class objects or manual inputs 
- Libraries used here -> pytest, pytest-cov (Coverage report)
- Command to run coverage -> pytest --cov
- Command to review coverage report -> coverage html
- Where to start 
    - Most simple to test
    - Which part of code responsible for most breaks ? dangerous pieces to break. Ex - Order and Line items
- Tests allow to analyze code and where issues in code -> overall design better ex. checkluhn doesnt require creating an object of paymentprocessor so create it in a seperate place
- Ex. pay_order hardest to test as lot of interactions happening here
- Mocking -> replacing systems/modules with mock version so test the thing using that system.

- Refactor Code
- instead of creating object of class in method, pass it as object. Prefer using protocol class so easy to create mock object of that class and use in test
- inputs manual enter - update input patching system, if use in app and not have keyboard input, inputs group and put in main function and provide to pay_order and process payment. in test provide mock values. card, month, year -> create creditcard dataclass
- In unit testing, Fixtures allow you to provide standard objects that you are going to need in several of your tests so define at one place and use in several tests. 
- Remove hardcoded dates from unittests
- package to read variables in env files called python-dotenv
- Make sure test right thing at right place -> for order, test order.total and not charge that is linked to processor



