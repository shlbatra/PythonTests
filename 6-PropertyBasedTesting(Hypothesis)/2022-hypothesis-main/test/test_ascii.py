from example import from_ascii_codes, to_ascii_codes
from hypothesis import (  # function defines how example data will be generated
    example,
    given,
    settings,
)
from hypothesis.strategies import text  # generate text here


# string - encode and decode - get string back
@given(text())  # given some text
@example("")  # provide empty string as an example in list of generated strings
@settings(max_examples=100)  # max examples so test not run infinite time
def test_decode_inverts_encode(test_str: str) -> None:
    assert from_ascii_codes(to_ascii_codes(test_str)) == test_str


# length of encoded and original string same
@given(text())
def test_list_length(test_str: str):
    encoded = to_ascii_codes(test_str)
    assert len(encoded) == len(test_str)
