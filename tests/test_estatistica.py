from numpy.random import seed
from numpy.random import randint

import pytest

from pyestat.estatistica import Estatistica

# garante o determinismo do teste.
seed(1)
valores = randint(10, 50, 100)


@pytest.mark.parametrize(
    "valores, minimo, maximo, media",
    [
        ([10, 5, 15, -999], 5, 20, 10),
        (randint(10, 150, 100), 0, 5, 0),
        ([-999], 0, 50, 0),
        ([5, 10, 20, -999], 10, 50, 15),
        ([10, 40, 100, -999], 10, 50, 25),
        (valores, 10, 50, sum(valores) / 100),
    ],
)
def test_calcule_media(valores, minimo, maximo, media):
    """Testa o metodo calcule a média"""
    assert Estatistica.calcule_media(valores, minimo, maximo) == media