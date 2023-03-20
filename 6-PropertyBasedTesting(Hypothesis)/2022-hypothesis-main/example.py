from functools import reduce

# convert to and from list of ascii codes

# string to int
def to_ascii_codes(inp: str) -> list[int]:
    return [ord(c) for c in inp]


# int to string
def from_ascii_codes(inp: list[int]) -> str:
    return reduce(lambda x, y: x + chr(y), inp, "")
