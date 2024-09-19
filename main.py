import pytest


def always_returns_true():
    return True


def test_always_returns_true():
    result = always_returns_true()
    assert result == True
