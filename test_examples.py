import pytest


def test_string_ops():
    result = "pytest"[:4]
    assert result == "python", f"Expected 'python' got {result}"
    
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    
@pytest.fixture
def sample_data():
    return [3, 1, 4, 1, 5]

def test_sum(sample_data):
    assert sum(sample_data) == 14

def test_len(sample_data):
    assert len(sample_data) == 5
    
@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, -1, -2),
    (100, 200, 300)
])
def test_addition(a, b, expected):
    assert add(a, b) == expected