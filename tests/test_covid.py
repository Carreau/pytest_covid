import pytest
import random


@pytest.mark.parametrize("a", list(range(500)))
def test_fail_III(a):
    assert random.random() < 0.99
