class SerieArmonicaGenerator:
    def __init__(self):
        self.notas = ['C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab', 'A', 'A#/Bb', 'B']

    def generar_serie_armonica(self, nota):
        indice_nota = self.notas.index(nota)

        serie_armonica = []
        for i in range(1, 9):
            if i == 1 or i == 2 or i == 4 or i == 8:
                serie_armonica.append(self.notas[indice_nota])
            elif i == 3 or i == 6:
                posicion_quinta = (indice_nota + 7) % 12
                serie_armonica.append(self.notas[posicion_quinta])
            elif i == 5:
                posicion_tercera_mayor = (indice_nota + 4) % 12
                serie_armonica.append(self.notas[posicion_tercera_mayor])
            elif i == 7:
                posicion_septima_menor = (indice_nota + 10) % 12
                serie_armonica.append(self.notas[posicion_septima_menor])

        return ', '.join(serie_armonica)

    def mostrar_serie_por_posicion(self, nota):
        posiciones = ['1', '2', '3', '4', '5', '6', '7']
        
        indice_nota = self.notas.index(nota)

        for i, posicion in enumerate(posiciones):
            nota_base = self.notas[indice_nota]
            serie = self.generar_serie_armonica(nota_base)
            print(f"Posición {posicion}: {serie}")
            indice_nota = (indice_nota - 1) % 12
