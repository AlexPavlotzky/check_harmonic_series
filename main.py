from check_harmonic_series import *

if __name__ == "__main__":
    instrumento = input("Bienvenido, por favor ingrese el instrumento para ver su série armónica:\n"
        "1. Trompeta en Bb (transpone a C)\n" 
        "2. Trompeta en C\n"
        "3. Corno en F\n" 
        "4. Corno en Eb\n"
        "5. Trombón alto en Eb\n"
        "6. Trombón tenor en Bb\n"
        "7. Sacabuche alto en D\n"
        "8. Sacabuche tenor en A\n"
        "9. Otro\n")
    
    if instrumento == "1" or instrumento == "2":
        nota_base = "C"
    elif instrumento == "3":
        nota_base = "F"
    elif instrumento == "4" or instrumento == "5":
        nota_base = "D#/Eb"
    if instrumento == "6":
        nota_base = "A#/Bb"
    elif instrumento == "7":
        nota_base = "D"
    elif instrumento == "8":
        nota_base = "A"
    elif instrumento == "9":
        nota_base = input("Ingrese la nota base del instrumento (C, C#/Db, D, D#/Eb, E, F, F#/Gb, G, G#/Ab, A, A#/Bb, B): ")
    generator = SerieArmonicaGenerator()
    generator.mostrar_serie_por_posicion(nota_base)
