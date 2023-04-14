class Estatistica:
    """Class docstrings go here."""

    @staticmethod
    def calcule_media(valores, minimo, maximo):
        """Class method docstrings go here."""

        soma = media = validas = i = 0

        while (i < 100) and (valores[i] != -999):
            if (valores[i] >= minimo) and (valores[i] <= maximo):
                soma += valores[i]
                validas += 1

            i += 1

        if validas > 0:
            media = soma / validas

        return media
