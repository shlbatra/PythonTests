from typing import Callable

import pytest
from hypothesis import given
from hypothesis.strategies import SearchStrategy, composite, integers
from office import Employee, fire_random_employee, generate_random_team


# custom stratergy to create teams/data generation process for us. Avoid boiler plate code for each test
# draw function to draw values from another stratergy
@composite
def teams(
    draw: Callable[[SearchStrategy[int]], int], min_size: int = 1, max_size: int = 10
) -> list[Employee]:
    rand_val = draw(integers(min_value=min_size, max_value=max_size))
    return generate_random_team(rand_val)


# test length of team 0
@given(integers(max_value=0))
def test_negative_team_size(team_size: int):
    with pytest.raises(ValueError):
        generate_random_team(team_size)


# test length of team
@given(integers(min_value=1, max_value=10))
def test_team_size(team_size: int):
    assert len(generate_random_team(team_size)) == team_size


# test that team has CEO
@given(teams(min_size=1))
def test_team_has_ceo(team: list[Employee]):
    assert Employee.CEO in team


# check length of list after firing employee
@given(teams(min_size=1))
def test_fire_employee(team: list[Employee]):
    emp_list_copy = team.copy()
    fire_random_employee(emp_list_copy)
    assert len(emp_list_copy) == len(team) - 1
