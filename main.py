from check_harmonic_series import *
from virgiliano import *

if __name__ == "__main__":
    instrumento = input("Benvenuto, scegli il tipo di trombone:\n"
        "1. Trombone contralto in D\n"
        "2. Trombone tenore in A\n"
        "3. Trombone basso in D\n"
        "4. Altro\n--> ")
    
    if instrumento == "1" or instrumento == "3":
        nota_base = "D"
    elif instrumento == "2":
        nota_base = "A"
    elif instrumento == "4":
        nota_base = input("Inserisci la nota di base dello strumento (C, C#/Db, D, D#/Eb, E, F, F#/Gb, G, G#/Ab, A, A#/Bb, B):\n-->  ")
    generator = SerieArmonicaGenerator()
    serie_combinada = generator.mostrar_serie_por_posicion(nota_base)
    sacabuche = Virgiliano()
    sacabuche.mostrar_sacabuche(serie_combinada)
