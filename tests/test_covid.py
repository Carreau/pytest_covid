import pytest
import random


def test_fail_I():
    assert False


@pytest.mark.parametrize("a", list(range(500)))
def test_fail_III(a):
    assert True
    # assert random.random() < 0.99
