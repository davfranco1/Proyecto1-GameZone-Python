import random  # Importa el módulo random para generar elecciones aleatorias

class PiedraPapelTijeraBase:
    def __init__(self, opciones):
        """
        Inicializa la clase base con las opciones dadas.

        Args:
            opciones (list): Lista de opciones para el juego.
        """
        self.opciones = opciones  # Asigna las opciones del juego a un atributo de la clase

    def elegir_juego(self):
        """
        Solicita al usuario que elija la versión del juego.

        Returns:
            PiedraPapelTijera o PiedraPapelTijeraLagartoSpock: La versión del juego elegida.
        """
        # Solicita al usuario que elija una versión del juego
        juego_elegido = input("Elige la versión del juego: 1 para Piedra, Papel, Tijera, o 2 para Piedra, Papel, Tijera, Lagarto, Spock: ")
        if juego_elegido == "1":
            return PiedraPapelTijera()  # Devuelve una instancia de PiedraPapelTijera si elige 1
        elif juego_elegido == "2":
            return PiedraPapelTijeraLagartoSpock()  # Devuelve una instancia de PiedraPapelTijeraLagartoSpock si elige 2
        else:
            print("Opción inválida")  # Muestra un mensaje de error si la opción es inválida
            exit()  # Termina el programa

    def usuario_1(self):
        """
        Solicita al usuario que elija una opción.

        Returns:
            str: La opción elegida.
        """
        # Solicita al usuario que elija una opción y la convierte a minúsculas
        user1 = input(f"Elige una opción: ({', '.join(self.opciones)}): ").lower()
        while user1 not in self.opciones:  # Verifica si la opción es válida
            user1 = input(f"Opción inválida. Elige: {', '.join(self.opciones)}: ").lower()  # Solicita nuevamente si es inválida
        return user1  # Devuelve la opción elegida

    def usuario_auto(self):
        """
        Elige una opción aleatoriamente para el oponente.

        Returns:
            str: La opción elegida.
        """
        return random.choice(self.opciones)  # Devuelve una opción aleatoria de la lista de opciones

    def jugar(self, user1, user2):
        """
        Determina si user1 gana contra user2.

        Args:
            user1 (str): La opción elegida por user1.
            user2 (str): La opción elegida por user2.

        Returns:
            bool: True si user1 gana, False en caso contrario.
        """
        # Verifica las condiciones en las que user1 gana contra user2
        return (user1 == "piedra" and user2 == "tijera") or \
               (user1 == "papel" and user2 == "piedra") or \
               (user1 == "tijera" and user2 == "papel")

    def ganador(self):
        """
        Juega hasta que un jugador alcance 3 puntos y declara al ganador.
        """
        puntos_user1 = 0  # Inicializa los puntos del usuario 1
        puntos_user2 = 0  # Inicializa los puntos del usuario 2

        while puntos_user1 < 3 and puntos_user2 < 3:  # Continúa jugando hasta que uno de los jugadores alcance 3 puntos
            user1 = self.usuario_1()  # Solicita la opción del usuario 1
            user2 = self.usuario_auto()  # Genera la opción del oponente automáticamente
            print("\nHas elegido:", user1)  # Muestra la opción elegida por el usuario 1
            print("El oponente ha elegido:", user2)  # Muestra la opción elegida por el oponente

            if user1 == user2:  # Si hay empate
                puntos_user1 += 1
                puntos_user2 += 1
                print("Empate. 1 punto para cada jugador")

            elif self.jugar(user1, user2):  # Si el usuario 1 gana
                puntos_user1 += 1
                print("Sumas 1 punto")

            else:  # Si el oponente gana
                puntos_user2 += 1
                print("El oponente suma 1 punto")

            # Muestra los puntos actuales de ambos jugadores
            print(f"Puntos Usuario 1: {puntos_user1}")
            print(f"Puntos Usuario 2: {puntos_user2}")

        if puntos_user1 > puntos_user2:  # Declara al ganador
            print("\n¡Has ganado!")
        else:
            print("\nEl oponente ha ganado")

    def partida(self):
        """
        Juega múltiples partidas hasta que el usuario decida detenerse.
        """
        while True:  # Bucle para jugar múltiples partidas
            self.ganador()  # Juega una partida
            if input("Jugamos de nuevo? Introduce S o N: ").upper() != "S":  # Pregunta si quiere jugar de nuevo
                break  # Sale del bucle si la respuesta no es "S"

class PiedraPapelTijera(PiedraPapelTijeraBase):
    def __init__(self):
        """
        Inicializa la clase PiedraPapelTijera con las opciones para el juego.
        """
        opciones = ["piedra", "papel", "tijera"]  # Define las opciones para Piedra, Papel, Tijera
        super().__init__(opciones)  # Llama al constructor de la clase base

class PiedraPapelTijeraLagartoSpock(PiedraPapelTijeraBase):
    def __init__(self):
        """
        Inicializa la clase PiedraPapelTijeraLagartoSpock con las opciones para el juego.
        """
        opciones = ["piedra", "papel", "tijera", "lagarto", "spock"]  # Define las opciones para Piedra, Papel, Tijera, Lagarto, Spock
        super().__init__(opciones)  # Llama al constructor de la clase base

    def jugar(self, user1, user2):
        """
        Determina si user1 gana contra user2 en la versión extendida del juego.

        Args:
            user1 (str): La opción elegida por user1.
            user2 (str): La opción elegida por user2.

        Returns:
            bool: True si user1 gana, False en caso contrario.
        """
        # Verifica las condiciones en las que user1 gana contra user2 en la versión extendida
        return (user1 == "piedra" and user2 in ["tijera", "lagarto"]) or \
               (user1 == "papel" and user2 in ["piedra", "spock"]) or \
               (user1 == "tijera" and user2 in ["papel", "lagarto"]) or \
               (user1 == "lagarto" and user2 in ["spock", "papel"]) or \
               (user1 == "spock" and user2 in ["tijera", "piedra"])


class JugarPPT:
    """
    Clase para jugar al juego de Piedra, Papel, Tijera, Lagarto, Spock.

    Métodos
    -------
    __init__():
        Inicializa la clase JugarPPT.
    
    jugar():
        Ejecuta una partida del juego Piedra, Papel, Tijera, Lagarto, Spock.
    """

    def __init__(self):
        """
        Inicializa la clase JugarPPT sin parámetros adicionales.
        """
        pass

    def jugar(self):
        """
        Ejecuta una partida del juego Piedra, Papel, Tijera, Lagarto, Spock.
        
        El método selecciona las opciones disponibles y utiliza una instancia
        de PiedraPapelTijeraBase para elegir y jugar una partida.
        """
        opciones = ["piedra", "papel", "tijera", "lagarto", "spock"]
        juego_base = PiedraPapelTijeraBase(opciones)
        juego = juego_base.elegir_juego()
        juego.partida()
