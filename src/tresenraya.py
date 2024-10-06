import random  # Importa el módulo random para generar movimientos aleatorios
import os  # Importa el módulo os para limpiar la pantalla de la consola
import time  # Importa el módulo time

class TresEnRaya:
    def __init__(self):
        """
        Inicializa el tablero de juego y establece el jugador actual.
        """
        dibujo_tablero = []  # Inicializa la matriz de 3x3
        for i in range(3):
            fila = [" "] * 3
            dibujo_tablero.append(fila)
        
        self.tablero = dibujo_tablero  # Asigna la matriz a self.tablero
        self.jugador_actual = "X"  # El primer jugador será el usuario, con la X


    def limpiar_pantalla(self): #Esto no ha funcionado. Próximos pasos conseguir limpiar.
        """
        Limpia la pantalla de la consola.
        """
        # Para Windows
        if os.name == 'nt':
            os.system('cls')  # Limpia la pantalla en Windows
        # Para Mac y Linux
        else:
            os.system('clear')  # Limpia la pantalla en Mac y Linux

    def print_tablero(self):
        """
        Imprime el estado actual del tablero.
        """
        # Imprime el tablero
        for fila in self.tablero:
            print("|".join(fila))  # Separa los campos de cada fila con |
            print("-" * 5)  # Separa las filas con una línea ---

    def buscar(self, user1):
        """
        Busca si el jugador especificado ha ganado.
        
        Args:
            user1 (str): El símbolo del jugador a buscar (X u O).
        
        Returns:
            bool: True si el jugador ha ganado, False en caso contrario.
        """
        # Revisa filas para buscar un ganador
        for fila in self.tablero:
            if fila.count(user1) == 3:  # Si todas las celdas de una fila son del jugador
                return True  # Hay un ganador

        # Revisa columnas para buscar un ganador
        for col in range(3): #Matriz es de 3x3
            if all(self.tablero[fila][col] == user1 for fila in range(3)):  # Si todas las celdas de una columna son del jugador
                return True  # Hay un ganador

        # Revisar diagonales
        # diagonal 1
        # Verifica si todas las celdas de la diagonal principal son del jugador user1
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] == user1:
            return True

        # diagonal 2
        # Verifica si todas las celdas de la diagonal secundaria son del jugador user1
        if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] == user1:
            return True

        return False  # No hay ganador

    def ocupada(self):
        """
        Verifica si el tablero está lleno.
        
        Returns:
            bool: True si todas las celdas están ocupadas, False si hay alguna celda vacía.
        """
        # Revisa si el tablero está lleno
        for fila in self.tablero:
            for celda in fila:
                if celda == " ":  # Si hay alguna celda vacía
                    return False  # El tablero no está lleno
        return True  # El tablero está lleno

    def usuario_auto(self):
        """
        Genera un movimiento aleatorio para el ordenador.
        
        Returns:
            tuple: Una tupla con la fila y columna seleccionadas.
        """
        # Genera un movimiento aleatorio del ordenador
        fila, col = random.choice([(i, j) for i in range(3) for j in range(3) if self.tablero[i][j] == " "])
        return fila, col  # Devuelve una fila y una columna

    def jugar(self):
        """
        Contiene las reglas del juego y controla el flujo del mismo.
        """
        # Método con reglas del juego
        while True:
            self.print_tablero()  # Imprime el estado actual del tablero
            print("\n")

            if self.jugador_actual == "X":
                while True:
                    
                    # Recibir input del jugador
                    fila = int(input(f"Jugador {self.jugador_actual}, elige una fila (0, 1, 2): "))
                    col = int(input(f"Jugador {self.jugador_actual}, elige una columna (0, 1, 2): "))
                    print(f"Has elegido fila {fila} y columna {col}")

                    if fila in range(3) and col in range(3):  # Si el input es válido
                        break  # Rompe el bucle
                    else:
                        print("Por favor, introduce números válidos (0, 1, 2).")

            else:
                fila, col = self.usuario_auto()  # Recibir input aleatorio del ordenador
                print(f"Oponente elige fila {fila} y columna {col}")

            if self.tablero[fila][col] == " ":
                self.tablero[fila][col] = self.jugador_actual  # Introducir input del usuario al tablero

                if self.buscar(self.jugador_actual):  # Si hay un ganador
                    self.print_tablero()  # Imprime el estado final del tablero
                    print("\n")
                    
                    print(f"El jugador {self.jugador_actual} gana")  # Imprime quién es el ganador
                    break

                elif self.ocupada():  # Si el tablero está lleno
                    self.print_tablero()  # Imprime el estado final del tablero
                    print("No hay ganador")  # Imprime que no hay ganador
                    break

                # Cambio de jugador
                self.jugador_actual = "O" if self.jugador_actual == "X" else "X"
            else:
                if self.jugador_actual == "X":
                    print("Celda ocupada. Introduce otra")  # Jugador debe elegir otra celda si la actual está ocupada
    
    def partida(self):
        """
        Inicia una partida y pregunta al usuario si quiere jugar de nuevo.
        """
        self.jugar()  # Inicia el juego

        while input("Jugamos de nuevo? Introduce S o N: ").upper() == "S":  # Pregunta al usuario si quiere jugar de nuevo
            self.__init__()  # Reinicia el juego
            self.jugar()  # Inicia una nueva partida
