class Palindromo:
    def __init__(self, palabra):
        self.palabra = palabra
        self.atributo = palabra

    def es_palindromo(self):
        palabra = self.palabra.replace(' ', '').lower()
        return palabra == palabra[::-1]

    def resultado(self):
        if self.es_palindromo():
            return f'La palabra {self.palabra} es un palíndromo'
        else:
            return f'La palabra {self.palabra} no es un palíndromo'

    def test(self):
        return self.es_palindromo()

    def __del__(self):
        print(self.atributo.upper())

    def __str__(self):
        return self.resultado()


def main():
    palabra = input('Escribe una palabra: ')
    palindromo = Palindromo(palabra)
    print(palindromo)


if __name__ == "__main__":
    main()

# En el código original, la clase Palindromo tiene un método __del__, que se llama cuando una instancia
# de la clase se elimina o se destruye. En Python, cuando una instancia se elimina, se llama al método 
# __del__ automáticamente antes de que la memoria asociada a la instancia se libere.

# En el código original, el método __del__ imprime el atributo self.palabra en mayúsculas. Cuando se 
# instancia un objeto Palindromo con la palabra "sonar", se crea una instancia de la clase, y luego 
# cuando se crea una nueva instancia con la palabra "radar", la instancia anterior se destruye y se 
# llama al método __del__, imprimiendo la palabra "RADAR" en mayúsculas.

# Por lo tanto, "RADAR" se muestra después de la instanciación de Palindromo("sonar") porque el método
#  __del__ se llama cuando se crea una nueva instancia de la clase, antes de que se imprima el resultado 
# del método test() para la nueva instancia.