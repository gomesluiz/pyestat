from numpy.random import seed
from numpy.random import randint

from pyestat.estatistica import Estatistica

class TestEstatistica:

    def test_calcula_media_caminho_1(self):
        assert Estatistica.calcule_media([10, 5, 15, -999], 5, 20) == 10


    def test_calcula_media_caminho_2(self):
        seed(1)
        assert Estatistica.calcule_media(randint(10, 150, 100), 0, 5) == 0


    def test_calcula_media_caminho_3(self):
        assert Estatistica.calcule_media([-999], 0, 50) == 0


    def test_calcula_media_caminho_4(self):
        assert Estatistica.calcule_media([5, 10, 20, -999], 10, 50) == 15


    def test_calcula_media_caminho_5(self):
        assert Estatistica.calcule_media([10, 40, 100, -999], 10, 50) == 25

    def test_calcula_media_caminho_6(self):
        valores = randint(10, 50, 100)
        assert Estatistica.calcule_media(valores, 10, 50) == sum(valores)/100