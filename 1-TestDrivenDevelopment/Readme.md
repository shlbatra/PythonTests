- Test Driven Development 
- Red Green Refractor (5 Steps) 
    1. Write Tests - pass if feature specification met
    2. Run Tests - run and make sure they fail to see if test running fine
    3. Write Actual code - Make the tests pass
    4. All Tests pass -> All new and old tests pass
    5. Refactor and Improve -> always have test running and passing
- do these in incremental small steps 
- Pros
    - forces developer think about reqts/interfaces first
    - save time overall as detect bugs much earlier
    - write code that is easily testable. code extend and seperate from other functionality
- Cons 
    - writing tests take time. 
    - if changes happen very frequent
    - false sense of security if too many unit test correct
    - blind spot if developer write test for his own code
    - developer implement test in wrong way and functionality in wrong way
- Testing Tips
    - tests should be decoupled. use diff data. change in 1 test not effect other tests. Dont use global instances in all tests. 
    - not reqd to test python built in functions
    - test compare output with a fixed value