class Virgiliano:
    def transformar_elemento(self, elemento):
        if len(str(elemento)) == 1:
           return f"--{elemento}--"
        else:
           return elemento

    def mostrar_sacabuche(self, serie):
        serie = [elemento.strip('"') for elemento in serie]

        notas = ["".join(filter(lambda c: not c.isdigit(), elemento)) for elemento in serie]

        notas = [self.transformar_elemento(elemento) for elemento in notas]
        print(f"     ____   ")
        print(f"    / __ \  ")
        print(f"    ||  ||  NUOVA INTAVOLATURA DI TROMBONI PER PER SONARLI IN CONCERTO ~ + * +")
        print(f"    ||  ||  ")
        print(f"    ||__||  ")
        print(f" __ ||--||  ")
        print(f" () ||  ||  ")
        print(f" ||-||  ||   1ra pos. -------------------------------{notas[1]}----------{notas[2]}----------{notas[3]}----------{notas[4]}----------{notas[5]}----------{notas[6]}----------{notas[7]}- ")
        print(f" ||-||  ||   2da pos. --------------------------{notas[9]}----------{notas[10]}----------{notas[11]}----------{notas[12]}----------{notas[13]}----------{notas[14]}----------{notas[15]}------")
        print(f" || ||  /\   3da pos. ---------------------{notas[17]}----------{notas[18]}----------{notas[19]}----------{notas[20]}----------{notas[21]}----------{notas[22]}----------{notas[23]}----------- ")
        print(f" || || /  \  4ta pos. ----------------{notas[25]}----------{notas[26]}----------{notas[27]}----------{notas[28]}----------{notas[29]}----------{notas[30]}----------{notas[31]}----------------")
        print(f" || ||<----> 5da pos. -----------{notas[33]}----------{notas[34]}----------{notas[35]}----------{notas[36]}----------{notas[37]}----------{notas[38]}----------{notas[39]}--------------------- ")
        print(f" || ||       6ta pos. ------{notas[41]}----------{notas[42]}----------{notas[43]}----------{notas[44]}----------{notas[45]}----------{notas[46]}----------{notas[47]}--------------------------")
        print(f" ||_||       7ma pos. -{notas[49]}----------{notas[50]}----------{notas[51]}----------{notas[52]}----------{notas[53]}----------{notas[54]}----------{notas[55]}------------------------------- ")
        print(f" \___/      ")
