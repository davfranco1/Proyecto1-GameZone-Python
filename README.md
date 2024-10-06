
# ¡Bienvenido a GameZone!

<p align="center">
  <a href="https://francoonline.net">
    <img src="https://th.bing.com/th/id/OIG4.HXYEoU95.5C77AL0ddA2?pid=ImgGn" height="300px">
  </a>
</p>


## Descripción
- Este es el primer proyecto de un Bootcamp de Data Science e IA, para poner en práctica el conocimiento adquierido durante la primera semana, incluyendo conceptos de funciones, clases, bucles y el uso de Git.
- En este primer proyecto, una empresa nos ha contactado para desarrollar una serie de videojuegos clásicos para su plataforma usando Python. Para llevar a cabo esta tarea, ponemos en práctica todos nuestros conocimientos de Python. Los juegos que la empresa quiere desarrollar son los siguientes:

#### Preguntados:
En este juego tendremos que ir haciendo preguntas al usuario sobre una variedad de temas y el usuario tendrá que ir respondiendo correctamente para avanzar. Las preguntas podrán ser de distintas categorías: cultura general, historia, entretenimiento, actualidad, etc. El usuario ganará el juego si consigue adivinar 10 preguntas seguidas.

#### Tres en raya:
Mítico juego donde el primero que consiga colocar tres fichas seguidas(en horizontal, vertical o diagonal) en un tablero 3x3 gana la partida. En nuestro caso, la empresa nos ha pedido que el usuario juegue contra la máquina.

#### Ahorcado:
El usuario juega contra la máquina. En este juego el usuario tendrá que adivinar una palabra elegida al azar por la máquina de entre una lista que nosotros definiremos previamente. Cada vez que el usuario se equivoque, mostraremos una nueva parte del personaje del ahorcado en una horca. Si el usuario consigue adivinar la palabra antes de que se le acaben las oportunidades, gana el juego.

#### Piedra-papel-tijera:
En este juego, el usuario tendrá que elegir una de las opciones y después, la máquina eligirá otra al azar. Gana el primero que gane tres rondas en total. Además la empresa nos ha pedido que, además del juego clásico, el usuario pueda elegir la opción de jugar a piedra-papel-tijera-lagarto-spock.


## Objetivos
- Cada juego tiene que estar programado como una clase y recogido dentro de un archivo  .py en la carpeta src.

- Tenemos que tener un archivo .py que nos permita elegir entre los juegos que hemos desarrollado y jugarlos sin necesidad de ir a cada archivo del juego.

- Una vez que acabe, cada juego tiene que dar la opción de volver a jugar al mismo juego, volver a la elección de juegos o terminar el programa.


## Uso

Podrás jugar a 4 juegos diferentes, accediento desde un menú principal con 4 opciones:
1. Piedra, papel, tijera
2. Ahorcado
3. Tres en Raya
4. Preguntados

Para salir del programa, usa el número "0".

### Piedra Papel Tijera Lagarto Spock
- El objetivo del juego es vencer al oponente seleccionando el elemento que gana según una serie de reglas.

#### Instrucciones para el Jugar:
- Se te pedirá que elijas la versión del juego:
- Introduce 1 para jugar a Piedra, Papel, Tijera.
- Introduce 2 para jugar a Piedra, Papel, Tijera, Lagarto, Spock.

#### Elección del Jugador:
- Se te pedirá que elijas una opción entre las disponibles (por ejemplo: piedra, papel, tijera).
- Escribe tu elección y presiona Enter.

#### Elección del Oponente:
- El oponente (controlado por la computadora) elegirá una opción aleatoriamente.

#### Resultado de la Ronda:
- Se compararán las elecciones y se determinará el ganador de la ronda según las reglas del juego:
*Piedra vence a Tijera.*
*Papel vence a Piedra.*
*Tijera vence a Papel.*

- En la versión extendida:
*Piedra vence a Tijera y Lagarto.*
*Papel vence a Piedra y Spock.*
*Tijera vence a Papel y Lagarto.*
*Lagarto vence a Spock y Papel.*
*Spock vence a Tijera y Piedra.*

#### Puntuación:
- Cada ronda ganada suma un punto.
- El juego continúa hasta que uno de los jugadores alcance 3 puntos.

#### Ganador:
- El primer jugador en alcanzar 3 puntos es declarado ganador.

#### Reiniciar el Juego:
- Después de cada partida, se te preguntará si deseas jugar de nuevo.
- Introduce S para jugar otra vez o N para salir.

### Ahorcado
- El objetivo del juego es adivinar una palabra relacionada con elementos de la naturaleza antes de que se te acaben las vidas.

#### Inicio del Juego:
- El juego comienza con 3 vidas.
- Se selecciona una palabra aleatoria relacionada con la naturaleza.
- La palabra se muestra como una serie de guiones bajos, representando cada letra de la palabra.

#### Adivinar Letras:
- Introduce una letra cuando se te solicite.
- Si la letra está en la palabra, se revelará en su(s) posición(es) correspondiente(s).
- Si la letra no está en la palabra, perderás una vida.

#### Reglas:
- Solo puedes introducir una letra a la vez.
- Si introduces una letra que ya has adivinado, se te informará y no perderás una vida.
- Si introduces una letra incorrecta, perderás una vida.
- El juego termina cuando adivinas todas las letras de la palabra o te quedas sin vidas.

#### Figuras del Ahorcado:
- La figura del ahorcado se actualizará con cada vida perdida.
- Hay cuatro figuras diferentes, que representan desde 3 vidas restantes hasta 0 vidas restantes.

#### Final del Juego:
- Si adivinas la palabra antes de quedarte sin vidas, ganarás el juego.
- Si te quedas sin vidas antes de adivinar la palabra, perderás el juego y se te mostrará la palabra correcta. Al final de cada partida, se te preguntará si quieres jugar de nuevo. Introduce “S” para jugar otra vez o “N” para salir.

#### Consejos:
- Las palabras están relacionadas con elementos de la naturaleza, ¡así que piensa en cosas como el sol, la luna, árboles, etc.!
- Intenta adivinar primero las vocales, ya que suelen aparecer con frecuencia en las palabras.

### Tres en Raya
- El objetivo del juego Tres en Raya es ser el primero en alinear tus símbolos (ya sea “X” o “O”) en una fila, columna o diagonal de un tablero. Es un juego de estrategia y táctica donde debes anticipar los movimientos de tu oponente y bloquear sus intentos de ganar mientras buscas crear tu propia línea de tres.

#### Inicio del Juego:
- El juego comienza con un tablero vacío de 3x3.
- El primer jugador será el usuario, representado por “X”.

#### Objetivo del Juego:
- El objetivo es alinear tres de tus símbolos (X o O) en una fila, columna o diagonal.

#### Cómo Jugar:
- Hay dos jugadores en la partida: tú (X) y el ordenador (O).

- Jugador X:
*Introduce la fila y columna donde deseas colocar tu “X”.*
*Las filas y columnas están numeradas del 0 al 2.*
*Ejemplo: Para colocar una “X” en la esquina superior izquierda, introduce fila 0 y columna 0.*

- Jugador O (Ordenador):
*El ordenador colocará su “O” en una posición aleatoria disponible.*

#### Condiciones de Victoria:
- El juego revisará después de cada movimiento si hay tres símbolos iguales en una fila, columna o diagonal.
- Si un jugador alinea tres símbolos, se declara ganador y el juego termina.

#### Empate:
- Si todas las celdas del tablero están ocupadas y no hay un ganador, el juego termina en empate.

#### Cambio de Turno:
- Después de cada movimiento válido, el turno cambia al otro jugador.
- Si la celda seleccionada ya está ocupada, el jugador debe elegir otra celda

### Preguntados
- El objetivo del juego es responder a preguntas de categorías aleatorias hasta alcanzar un número de aciertos.

#### Creación de Categorías y Preguntas:
- El juego crea automáticamente cuatro categorías: Historia de España, Python, Cultura General y Deporte. Cada categoría se llena con preguntas predefinidas.

#### Estructura de las Preguntas:
- Cada pregunta tiene un texto, una lista de 4 opciones y una respuesta correcta.

#### Instrucciones para el Juego de Preguntados
- Al iniciar, el juego muestra una pregunta aleatoria de una categoría aleatoria.

#### Respondiendo a las Preguntas:
- Se muestra la pregunta y las opciones de respuesta.
- Introduce el número correspondiente a tu respuesta (1 al 4) y presiona Enter.

#### Comprobación de Respuestas:
- El juego verifica si tu respuesta es correcta.
- Si es correcta, se incrementa el contador de respuestas correctas consecutivas.
- Si es incorrecta, el contador se reinicia y se muestra la respuesta correcta.

#### Objetivo del Juego:
- El objetivo es responder correctamente a 10 preguntas consecutivas.
- El juego continúa hasta que logres este objetivo.

#### Fin del Juego:
- Cuando aciertes 10 preguntas consecutivas, el juego te felicitará y terminará, preguntando si deseas jugar de nuevo.


## Lenguaje

Todo el código está escrito en lenguaje Python.

## Conclusiones

- Este proyecto ha sido una oportunidad para aplicar y consolidar los conocimientos de Python en la primera semana del bootcamp de Data Science e IA, en el desarrollo de videojuegos clásicos.

- A través de la creación de juegos como Preguntados, Tres en raya, Ahorcado y Piedra-papel-tijera, podemos poner a prueba nuestra capacidad para diseñar y programar soluciones interactivas y entretenidas, aplicando la lógica y sintaxis.

- Cada juego ha sido implementado como una clase independiente, que hace el código más fácil de entender y gestionar. Debo seguir practicando el uso de esta característica como buena práctica para un código modular y más eficiente.

- Aprender a implementar por primera vez un sistema centralizado (main.py), que permite a los usuarios seleccionar y jugar cualquier juego desde un único punto de entrada, mejora la experiencia. Con el uso de bucles, tiene la opción de reiniciar el juego, cambiar de juego o finalizar el programa, añadiendo una capa adicional de flexibilidad y usabilidad.

- En el plazo de entrega de 3 días, se han cumplido los objetivos del proyecto, y sirve como ejercicio de compromiso con intensas jornadas de estudio y trabajo, pero también de motivación por haberlo conseguido.

- Pese al margen de mejora, me siento satisfecho con el resultado dado el desafío. 🚀🚀

## Próximos pasos

- El más importante es, sin duda, añadir métodos de control de errores
- En general, para todos los juegos, mejorar la visualización y añadir elementos como emojis, código o animaciones ASCII para hacerlo más vistoso.
- Para el juego de tres en raya, mejorar la visualización del tablero y borrar las impresiones según avanza el juego, para que sea más fácil de entender. Otra mejora podría ser la de añadir la posibilidad de un segundo usuario humano.
- Como he mencionado para todos el juegos, en el caso del ahorcado, mejorar la impresión de la figura según avanza el juego, y animarla para ser más llamativa.
- Para el juego de preguntados, incluir todas las preguntas dentro de un documento de texto, por ejemplo, .txt, de modo que el código sea más corto y legible. 
- En este mismo juego, para que no se repitan las preguntas, dado que tengo una lista donde se van añadiendo las preguntas, añadir una condición if para no mostrarlas en caso de ya encontrarse en ella.

## Acceso

- Los juegos están disponibles accediento a este enlace: [Entrar a GameZone](https://github.com/davfranco1/Proyecto1-GameZone-Python/blob/main/main.py)