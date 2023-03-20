# Property-Based Testing In Python: Hypothesis is AWESOME

Hypothesis is an awesome Python package for property-based testing. In this video I talk about what property-based testing is, and show you a practical example of how to use it to make writing software tests in Python a breeze.

- Start with unit tests - take time with more complex code
- Property testing -> make testing faster than Unit tests using Hypothesis package
- unit test defines fixture (predefined specific set of input values), executes code using that fixture and asserts the result as expected -> Arrange Act Assert -> describes what test code is doing
- Behavior driven development -> Given When Then -> describes in way what user might do
- Property Test
    - fn/program/system abides by property
    - dont need to know about specific input or output of system, just check specific characterstics
    - test property of system by automatically generating example input data
    - diff properties test
        - reversible operation. Encoding and decoding string. 
        - property of data that code is manipulating. Ex. sorting not change length of list (list length property)
        - result of fn call adheres to some condition. ex fn generate uuid -> generated id follows uuid structure
        - build own stratergy gives you control over how you generate data. Use SearchStrategy and  composite
        - hypothesis generate test code for you . Ex ->
            hypothesis write <class or method> > <testfile.py>
            hypothesis write office.generate_random_team > test_office_v1.py
- flexible data generation option. numpy datastructure, pandas dataframe
- app need random selection of things with specific conditions
- stateful testing / model based testing -> generate data and tests. provide flowchart, get sequence of actions that can lead to failure to test. 