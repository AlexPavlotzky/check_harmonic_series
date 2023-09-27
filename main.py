from check_harmonic_series import *
from virgiliano import *

if __name__ == "__main__":
    instrumento = input("Bienvenido, por favor ingrese el registro de su sacabuche:\n"
        "1. Sacabuche alto en D\n"
        "2. Sacabuche tenor en A\n"
        "3. Sacabuche bajo en A\n"
        "4. Otro\n")
    
    if instrumento == "1":
        nota_base = "D"
    elif instrumento == "2" or instrumento == "3":
        nota_base = "A"
    elif instrumento == "4":
        nota_base = input("Ingrese la nota base del instrumento (C, C#/Db, D, D#/Eb, E, F, F#/Gb, G, G#/Ab, A, A#/Bb, B): ")
    generator = SerieArmonicaGenerator()
    serie_combinada = generator.mostrar_serie_por_posicion(nota_base)
    sacabuche = Virgiliano()
    sacabuche.mostrar_sacabuche(serie_combinada)
