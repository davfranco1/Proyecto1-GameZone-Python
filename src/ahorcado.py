import random  # Importa el módulo random para seleccionar palabras aleatorias

class Ahorcado:
    def __init__(self):
        """
        Inicializa el juego con 3 vidas, una palabra aleatoria, y otras variables necesarias.
        """
        self.vidas = 3  # Establece el número de vidas iniciales
        self.palabra = self.palabra_aleatoria()  # Selecciona una palabra aleatoria
        self.palabra_completada = ["_"] * len(self.palabra)  # Crea una lista con guiones bajos para representar la palabra incompleta
        self.letras_adivinadas = []  # Lista para almacenar las letras que el usuario ha adivinado
        self.resuelto = False  # Indica si la palabra ha sido adivinada completamente

    def figura(self):
        """
        Devuelve la representación gráfica del ahorcado según las vidas restantes.
        """
        partes = [
            """
              +---+
              |   |
              O   |
             /|\  |
             / \  |
                  |
              =========""",  # Figura del ahorcado con 0 vidas restantes
            """
              +---+
              |   |
              O   |
             /|\  |
                  |
                  |
              =========""",  # Figura del ahorcado con 1 vida restante
            """
              +---+
              |   |
              O   |
              |   |
                  |
                  |
              =========""",  # Figura del ahorcado con 2 vidas restantes
            """
              +---+
              |   |
                  |
                  |
                  |
                  |
              ========="""  # Figura del ahorcado con 3 vidas restantes
        ]
        return partes[self.vidas]  # Devuelve la figura correspondiente al número de vidas restantes

    def palabra_aleatoria(self):
        """
        Selecciona y devuelve una palabra aleatoria de una lista de palabras relacionadas con la naturaleza.
        """
        palabras = ["sol", "luna", "playa", "montaña", "rio", "arbol", "flor", "cielo", "estrella", "nube", "lluvia", "bosque", "lago", "desierto", "oceano", "isla", "valle", "cascada", "cueva", "pradera"]
        return random.choice(palabras)  # Devuelve una palabra seleccionada aleatoriamente de la lista

    def jugar(self):
        """
        Ejecuta el ciclo principal del juego, solicitando al usuario que adivine letras y actualizando el estado del juego.
        """
        print(self.figura())  # Imprime la figura del ahorcado
        print(" ".join(self.palabra_completada))  # Imprime la palabra incompleta con espacios entre los guiones bajos
        print("\n")

        while not self.resuelto and self.vidas > 0:  # Bucle principal del juego que continúa hasta que se adivine la palabra o se queden sin vidas
            letra_usuario = input("Introduce una letra: . ¡Pista! Las palabras tienen relación con elementos de la naturaleza").lower()  # Solicita al usuario que introduzca una letra y la convierte a minúscula

            if letra_usuario.isalpha() and len(letra_usuario) == 1:  # Verifica que la entrada del usuario sea una letra y tenga una longitud de 1
                if letra_usuario in self.letras_adivinadas:
                    print(f"La letra '{letra_usuario}' ya está en la palabra")  # Informa al usuario si la letra ya ha sido adivinada

                elif letra_usuario not in self.palabra:
                    print(f"La letra '{letra_usuario}' no está en la palabra")  # Informa al usuario si la letra no está en la palabra
                    self.vidas -= 1  # Resta una vida
                    self.letras_adivinadas.append(letra_usuario)  # Añade la letra a la lista de letras adivinadas

                else:
                    print(f"¡Bien! La letra '{letra_usuario}' está en la palabra")  # Informa al usuario si la letra está en la palabra
                    self.letras_adivinadas.append(letra_usuario)  # Añade la letra a la lista de letras adivinadas

                    for i, letra in enumerate(self.palabra):  # Recorre la palabra para encontrar todas las ocurrencias de la letra adivinada
                        if letra == letra_usuario:
                            self.palabra_completada[i] = letra_usuario  # Actualiza la palabra incompleta con la letra adivinada

                    if "_" not in self.palabra_completada:  # Verifica si la palabra ha sido completamente adivinada
                        self.resuelto = True  # Marca la palabra como resuelta

            else:
                print("Debes introducir una letra")  # Informa al usuario si la entrada no es válida

            print(self.figura())  # Imprime la figura del ahorcado actualizada
            print(" ".join(self.palabra_completada))  # Imprime la palabra incompleta actualizada
            print("\n")

        if self.resuelto:
            print("¡Has adivinado la palabra!")  # Felicita al usuario si ha adivinado la palabra
        else:
            print(f"¡Ahorcado! La palabra era '{self.palabra}'")  # Informa al usuario si ha perdido y muestra la palabra correcta

    def partida(self):
        """
        Inicia una partida y pregunta al usuario si quiere jugar de nuevo.
        """
        self.jugar()  # Inicia el juego

        while input("Jugamos de nuevo? Introduce S o N: ").upper() == "S":  # Pregunta al usuario si quiere jugar de nuevo
            self.__init__()  # Reinicia el juego
            self.jugar()  # Inicia una nueva partida
