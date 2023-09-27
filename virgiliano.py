class Virgiliano:
    def mostrar_sacabuche(self, serie):
        serie = [elemento.strip('"') for elemento in serie]

        notas = ["".join(filter(lambda c: not c.isdigit(), elemento)) for elemento in serie]

        print(f"     ____   ")
        print(f"    / __ \  ")
        print(f"    ||  ||  NUOVA INTAVOLATURA DI TROMBONI PER SONARLI IN CONCERTO ~ + * + ")
        print(f"    ||  ||  ")
        print(f"    ||__||  ")
        print(f" __ ||--||  ")
        print(f" () ||  ||  ")
        print(f" ||-||  ||   -{notas[1]}-{notas[2]}-{notas[3]}-{notas[4]}-{notas[5]}-{notas[6]}-{notas[7]}- ")
        print(f" ||-||  ||  ")
        print(f" || ||  /\   -{notas[17]}-{notas[18]}-{notas[19]}-{notas[20]}-{notas[21]}-{notas[22]}-{notas[23]}- ")
        print(f" || || /  \ ")
        print(f" || ||<----> -{notas[33]}-{notas[34]}-{notas[35]}- ")
        print(f" || ||      ")
        print(f" || ||       -{notas[49]}-{notas[50]}-- ")
        print(f" \___/      ")
