"""A simple testing example"""

import random


# mutant testing example -> change + to - (mutant will fail the test)
def add_three(x: int) -> int:
    return x + 3


# test proprty -> add and remove three should be 0
def remove_three(x: int) -> int:
    return x - 3


# mutant testing example -> change * to + (mutant still passes the test)
def multiply_by_two(x: int) -> int:
    return x * 2


def add_three_alt(
    x: int,
) -> int:  # pass test - tests cant prove that program is correct
    if x == 1:
        return 4
    elif x == 2:
        return 5
    elif x == 3:
        return 6
    else:
        return 0


def main():
    # testing the function add_three
    assert add_three(1) == 4
    assert add_three(2) == 5
    assert add_three(3) == 6
    assert multiply_by_two(2) == 4
    assert add_three(remove_three(4)) == 4  # property testing with 1 value
    for _ in range(100):
        x = random.randint(-1000, 1000)
        assert (
            add_three(remove_three(x)) == x
        )  # property testing with any input value - can generate case not think about
    print("All tests pass!")


if __name__ == "__main__":
    main()
