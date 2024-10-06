import random  # Importa el módulo random para seleccionar elementos aleatorios.

class Preguntados:
    """
    Clase principal para gestionar el juego de preguntas y respuestas.
    """

    class Pregunta:
        """
        Clase para representar una pregunta con sus opciones y respuesta correcta.
        """
        def __init__(self, pregunta, opciones, respuesta_correcta):
            """
            Inicializa una instancia de Pregunta.

            Parámetros:
            pregunta (str): El texto de la pregunta.
            opciones (list): Lista de opciones de respuesta.
            respuesta_correcta (str): La respuesta correcta.
            """
            self.pregunta = pregunta  # Asigna el texto de la pregunta.
            self.opciones = opciones  # Asigna la lista de opciones.
            self.respuesta_correcta = respuesta_correcta  # Asigna la respuesta correcta.

        def comprobar_respuesta(self, respuesta_usuario):
            """
            Comprueba si la respuesta del usuario es correcta.

            Parámetros:
            respuesta_usuario (str): La respuesta proporcionada por el usuario.

            Retorna:
            bool: True si la respuesta es correcta, False en caso contrario.
            """
            # Compara la respuesta del usuario con la respuesta correcta (ignorando mayúsculas/minúsculas).
            return self.respuesta_correcta.lower() == respuesta_usuario.lower()

    class Categoria:
        """
        Clase para representar una categoría de preguntas.
        """
        def __init__(self, nombre):
            """
            Inicializa una instancia de Categoria.

            Parámetros:
            nombre (str): El nombre de la categoría.
            """
            self.nombre = nombre  # Asigna el nombre de la categoría.
            self.preguntas = []  # Inicializa una lista vacía para almacenar preguntas.

        def agregar_pregunta(self, pregunta):
            """
            Agrega una pregunta a la categoría.

            Parámetros:
            pregunta (Pregunta): Una instancia de la clase Pregunta.
            """
            self.preguntas.append(pregunta)  # Añade la pregunta a la lista de preguntas.

        def pregunta_aleatoria(self):
            """
            Selecciona una pregunta aleatoria de la categoría.

            Retorna:
            Pregunta: Una instancia de la clase Pregunta.
            """
            return random.choice(self.preguntas)  # Devuelve una pregunta aleatoria de la lista.

    def __init__(self):
        """
        Inicializa una instancia de Preguntados.
        """
        self.categorias = []  # Inicializa una lista vacía para almacenar categorías.

    def agregar_categoria(self, categoria):
        """
        Agrega una categoría al juego.

        Parámetros:
        categoria (Categoria): Una instancia de la clase Categoria.
        """
        self.categorias.append(categoria)  # Añade la categoría a la lista de categorías.

    def pregunta_aleatoria(self):
        """
        Selecciona una pregunta aleatoria de una categoría aleatoria.

        Retorna:
        Pregunta: Una instancia de la clase Pregunta.
        """
        categoria = random.choice(self.categorias)  # Selecciona una categoría aleatoria.
        return categoria.pregunta_aleatoria()  # Devuelve una pregunta aleatoria de la categoría seleccionada.

    def jugar(self):
        """
        Inicializa el juego y empieza la partida.
        """
        # Crear categorías y agregar preguntas
        historia_espana = self.Categoria("Historia de España")  # Crea una categoría de Historia de España.
        python = self.Categoria("Python")  # Crea una categoría de Python.
        cultura_general = self.Categoria("Cultura General")  # Crea una categoría de Cultura General.
        deporte = self.Categoria("Deporte")  # Crea una categoría de Deporte.

        # Agregar preguntas a las categorías
        preguntas_historia_espana = [
    ("¿En qué año comenzó la Reconquista?", ["1492", "711", "1085", "1212"], "711"),
    ("¿Quién fue el primer rey de la dinastía Borbón en España?", ["Carlos III", "Felipe V", "Fernando VII", "Alfonso XII"], "Felipe V"),
    ("¿En qué año se firmó la Constitución de Cádiz?", ["1833", "1812", "1820", "1808"], "1812"),
    ("¿Qué evento marcó el fin de la Guerra de Independencia Española?", ["Batalla de Trafalgar", "Tratado de Valençay", "Batalla de Waterloo", "Batalla de Bailén"], "Tratado de Valençay"),
    ("¿Quién fue el dictador de España desde 1939 hasta 1975?", ["Adolfo Suárez", "Francisco Franco", "Manuel Azaña", "Miguel Primo de Rivera"], "Francisco Franco"),
    ("¿En qué año se celebraron las primeras elecciones democráticas tras la dictadura de Franco?", ["1981", "1975", "1977", "1982"], "1977"),
    ("¿Qué rey abdicó en 2014?", ["Carlos IV", "Felipe VI", "Juan Carlos I", "Alfonso XIII"], "Juan Carlos I"),
    ("¿Cuál fue el principal conflicto bélico en España durante el siglo XIX?", ["Guerra de Sucesión", "Guerra de Independencia", "Guerra de los Treinta Años", "Guerra Civil"], "Guerra de Independencia"),
    ("¿En qué año se produjo la caída de Granada, último bastión musulmán en España?", ["1492", "1482", "1500", "1478"], "1492"),
    ("¿Quién fue el líder del bando republicano durante la Guerra Civil Española?", ["Francisco Largo Caballero", "Manuel Azaña", "Francisco Franco", "José Antonio Primo de Rivera"], "Manuel Azaña")
]

        preguntas_python = [
    ("¿Quién es el creador de Python?", ["Guido van Rossum", "James Gosling", "Dennis Ritchie", "Bjarne Stroustrup"], "Guido van Rossum"),
    ("¿Qué tipo de lenguaje es Python?", ["Compilado", "Interpretado", "Ensamblador", "Máquina"], "Interpretado"),
    ("¿Cuál es la extensión de archivo para los módulos de Python?", [".py", ".java", ".cpp", ".js"], ".py"),
    ("¿Qué palabra clave se usa para definir una función en Python?", ["def", "function", "func", "define"], "def"),
    ("¿Cuál de las siguientes es una estructura de datos mutable en Python?", ["Lista", "Tupla", "Cadena", "Entero"], "Lista"),
    ("¿Qué operador se usa para la exponenciación en Python?", ["**", "^", "*", "//"], "**"),
    ("¿Cuál es la salida de print(type([])) en Python?", ["<class 'list'>", "<class 'tuple'>", "<class 'dict'>", "<class 'set'>"], "<class 'list'>"),
    ("¿Qué biblioteca se usa para el análisis de datos en Python?", ["Pandas", "NumPy", "Matplotlib", "SciPy"], "Pandas"),
    ("¿Qué función se usa para obtener la longitud de una lista en Python?", ["len()", "length()", "size()", "count()"], "len()"),
    ("¿Cuál es el resultado de 3 + 2 * 2 en Python?", ["7", "10", "8", "9"], "7")
]

        preguntas_cultura_general = [
    ("¿En qué año comenzó la Reconquista?", ["1492", "711", "1085", "1212"], "711"),
    ("¿Cuál es el río más largo del mundo?", ["Nilo", "Amazonas", "Yangtsé", "Misisipi"], "Amazonas"),
    ("¿Quién escribió 'Cien años de soledad'?", ["Gabriel García Márquez", "Mario Vargas Llosa", "Julio Cortázar", "Isabel Allende"], "Gabriel García Márquez"),
    ("¿Cuál es el planeta más grande del sistema solar?", ["Júpiter", "Saturno", "Neptuno", "Urano"], "Júpiter"),
    ("¿En qué año cayó el Muro de Berlín?", ["1989", "1991", "1987", "1990"], "1989"),
    ("¿Quién pintó 'La última cena'?", ["Leonardo da Vinci", "Miguel Ángel", "Rafael", "Donatello"], "Leonardo da Vinci"),
    ("¿Cuál es la capital de Australia?", ["Sídney", "Melbourne", "Canberra", "Brisbane"], "Canberra"),
    ("¿Qué país tiene la mayor población del mundo?", ["India", "Estados Unidos", "Indonesia", "China"], "China"),
    ("¿En qué año se fundó la ONU?", ["1945", "1939", "1950", "1948"], "1945"),
    ("¿Cuál es el idioma más hablado en el mundo?", ["Inglés", "Español", "Chino mandarín", "Hindú"], "Chino mandarín")
]

        preguntas_deporte = [
    ("¿En qué año se celebraron los primeros Juegos Olímpicos modernos?", ["1896", "1900", "1912", "1920"], "1896"),
    ("¿Quién ganó la Copa Mundial de la FIFA en 2018?", ["Brasil", "Alemania", "Francia", "Argentina"], "Francia"),
    ("¿Cuál es el récord mundial de los 100 metros lisos?", ["9.58 segundos", "9.63 segundos", "9.69 segundos", "9.72 segundos"], "9.58 segundos"),
    ("¿En qué deporte se utiliza una pelota llamada 'shuttlecock'?", ["Bádminton", "Tenis", "Voleibol", "Rugby"], "Bádminton"),
    ("¿Cuántos jugadores hay en un equipo de baloncesto en la cancha?", ["5", "6", "7", "8"], "5"),
    ("¿Quién es conocido como 'El Rey del Fútbol'?", ["Pelé", "Maradona", "Messi", "Cristiano Ronaldo"], "Pelé"),
    ("¿En qué año ganó España su primera Copa Mundial de la FIFA?", ["2010", "2006", "1998", "2014"], "2010"),
    ("¿Cuál es el torneo de tenis más antiguo del mundo?", ["Wimbledon", "Roland Garros", "US Open", "Australian Open"], "Wimbledon"),
    ("¿Cuántos anillos de campeonato tiene Michael Jordan?", ["6", "5", "7", "8"], "6"),
    ("¿En qué deporte se puede realizar un 'hole in one'?", ["Golf", "Críquet", "Béisbol", "Hockey"], "Golf")
]

        # Poblar categorías con preguntas
        for pregunta in preguntas_historia_espana: # Añade preguntas a la categoría Historia de España. 
            historia_espana.agregar_pregunta(self.Pregunta(*pregunta))  # El * saca los elementos de la tupla para que puedan usarse independientemente.

        for pregunta in preguntas_python:
            python.agregar_pregunta(self.Pregunta(*pregunta))  # Añade preguntas a la categoría Python.

        for pregunta in preguntas_cultura_general:
            cultura_general.agregar_pregunta(self.Pregunta(*pregunta))  # Añade preguntas a la categoría Cultura General.

        for pregunta in preguntas_deporte:
            deporte.agregar_pregunta(self.Pregunta(*pregunta))  # Añade preguntas a la categoría Deporte.

        # Agregar categorías al juego
        self.agregar_categoria(historia_espana)  # Añade la categoría Historia de España al juego.
        self.agregar_categoria(python)  # Añade la categoría Python al juego.
        self.agregar_categoria(cultura_general)  # Añade la categoría Cultura General al juego.
        self.agregar_categoria(deporte)  # Añade la categoría Deporte al juego.

        # Empezar el juego
        respuestas_consecutivas_correctas = 0  # Inicializa el contador de respuestas correctas consecutivas.
        
        while respuestas_consecutivas_correctas < 10:
            pregunta = self.pregunta_aleatoria()  # Selecciona una pregunta aleatoria.
            print(pregunta.pregunta)  # Muestra la pregunta.

            for i, opcion in enumerate(pregunta.opciones, 1): #el parámetro "1" suma 1 al índice para mostrar en respuestas
                print(f"{i}. {opcion}")  # Muestra las opciones de respuesta.
            respuesta_usuario = input("Tu respuesta (1, 2, 3 o 4): ")  # Solicita la respuesta del usuario.
            
            if pregunta.comprobar_respuesta(pregunta.opciones[int(respuesta_usuario) - 1]): #-1 para coincidir con índices de ppython
                print("¡Correcto!")  # Informa al usuario si la respuesta es correcta.
                respuestas_consecutivas_correctas += 1  # Incrementa el contador de respuestas correctas.
            else:
                print(f"Te has equivocado! La respuesta correcta es: '{pregunta.respuesta_correcta}'")  # Informa al usuario si la respuesta es incorrecta.
                respuestas_consecutivas_correctas = 0  # Reinicia el contador de respuestas correctas.

            print(f"Aciertos consecutivos: {respuestas_consecutivas_correctas}")  # Muestra el número de aciertos consecutivos.
            print("\n")  # Imprime una línea en blanco para separar las preguntas.

        print(f"\n¡Felicidades! Has acertado 10 preguntas consecutivas.")  # Felicita al usuario por ganar el juego.

        while True:  # Bucle para jugar múltiples partidas
            self.jugar()  # Juega una partida
            if input("Jugamos de nuevo? Introduce S o N: ").upper() != "S":  # Pregunta si quiere jugar de nuevo
                break  # Sale del bucle si la respuesta no es "S"