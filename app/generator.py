"""Random username generator for Auto mode."""
import random
import string
from typing import List

LETTERS = string.ascii_lowercase
DIGITS = string.digits


def build_charset(letters: bool, digits: bool, underscore: bool) -> str:
    return (LETTERS if letters else "") + (DIGITS if digits else "") + ("_" if underscore else "")


def generate_random(count: int, min_len: int, max_len: int, charset: str) -> List[str]:
    """Unique random names. Stops early if the name space is smaller than `count`."""
    if not charset or count < 1 or min_len < 2 or max_len > 32 or min_len > max_len:
        raise ValueError("bad generator settings")
    space = sum(len(charset) ** n for n in range(min_len, max_len + 1))
    count = min(count, space)
    seen, out = set(), []
    while len(out) < count:
        n = random.randint(min_len, max_len)
        name = "".join(random.choice(charset) for _ in range(n))
        if name not in seen:
            seen.add(name)
            out.append(name)
    return out
