from src.piedrapapeltijera import JugarPPT
from src.ahorcado import Ahorcado
from src.tresenraya import TresEnRaya
from src.preguntados import Preguntados

class Menu:
    def __init__(self) -> None:
        pass

    def mostrar_juegos(self):
        print(""" ______ ______________   __    __________   ____________  _____     _______     _________________________________ _____ __   ________
 |_____]  |  |______| \  | \  / |______| \  |  |  |     \|     |    |_____|    |  ____|_____||  |  ||______ ____/|     || \  ||______
 |_____]__|__|______|  \_|  \/  |______|  \_|__|__|_____/|_____|    |     |    |_____||     ||  |  ||______/_____|_____||  \_||______
                                                                                                                                     """)
        print("Elige un juego:")
        print("1. Piedra, papel, tijera")
        print("2. Tres en raya")
        print("3. Ahorcado")
        print("4. Preguntados")
        print("0. Salir")

    def main(self):
        self.mostrar_juegos()
        while True:
            try:
                opcion_juego = int(input("Introduce la opción del juego que quieras jugar (0,1,2,3,4): "))
            except ValueError:
                print("Por favor, introduce un número válido.")
                continue

            if opcion_juego == 0:
                break
            elif opcion_juego == 1:
                juego = JugarPPT()
                juego.jugar()
            elif opcion_juego == 2:
                juego = TresEnRaya()
                juego.partida()
            elif opcion_juego == 3:
                juego = Ahorcado()
                juego.partida()
            elif opcion_juego == 4:
                juego = Preguntados()
                juego.jugar()
            else:
                print("Opción inválida")
            
            self.mostrar_juegos()

        print("El programa se ha cerrado")

if __name__ == "__main__":
    menu = Menu()
    menu.main()
