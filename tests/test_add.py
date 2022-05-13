import numpy as np
from src.add import add
def test_add():
    assert add(np.array([1]),np.array([1])) == [2]


