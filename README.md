# Soldado Espacial
Soldado espacial es una aventura con la cual podrás surcar los cielos evadiendo misiles y balas de plasma, ¿el objetivo? Logra tu mejor puntaje antes de que uno de los proyectiles te alcance.

## Requisitos del sistema
- El juego solo esta disponible para sistemas operativos Windows 10 en adelante.
- RAM: 1G
- Espacio en disco: 34 Mb

## Inicio rapido
Para empezar a jugar solo debes descomprimir el archivo juego.zip dentro de el encontraras una carpeta llamada soldado espacial y dentro de esta un archivo llamado juego.exe ábrelo y disfruta.

## Para desarrolladores
El código fuente y los recursos que usa el juego los puede encontrar en la carpeta dev.

### Arquitectura
El juego está escrito en Python (versión 3.11.2).
Se realiza el control de gráficos e interfaz de usuario mediante PyGame (versión 2.4.0).

### Componentes
Se realizo el desarrollo del juego en único archivo juego.py mediante un bucle infinito el cual se rompe con acciones específicas del jugador.

#### Librerías
En las líneas 1 a 4 importa las librerías necesarias para su desarrollo.

- PyGame: Para el control y desarrollo de la interfaz gráfica con el usuario.
- Random: Para la obtención de números aleatorios.
- Sys: para llamar utilidades del sistema operativo.
- Pygame.locals: importa las variables para el manejo de eventos.

#### Variables de configuración
En las líneas 6 a la 24 se definen las variables de configuración del juego y la interfaz gráfica.
SCREEN_W: Establece el ancho de la pantalla de juego, se deben usar valores enteros según la cantidad de pixeles deseados.
SCREEN_H: Establece el alto de la pantalla de juego, se deben usar valores enteros según la cantidad de pixeles deseados.
TEXT_COLOR: Color del texto primario desplegado en la interfaz. Usa una tupla de 3 valores enteros los cuales simbolizan el estándar RGB.
TEXT_COLOR2: Color del texto alterno desplegado en la interfaz. Usa una tupla de 3 valores enteros los cuales simbolizan el estándar RGB.
BG_COLOR: Color del fondo cuando se inicia una partida. Usa una tupla de 3 valores enteros los cuales simbolizan el estándar RGB.
FPS: Controla los fotogramas máximos que puede usar el juego, se deben usar valores enteros.
WMIN_ROCKET: Establece el ancho mínimo en pixeles de los misiles que atacan al jugador, se deben usar valores enteros según la cantidad de pixeles deseados.
WMAX_ROCKET: Establece el alto máximo en pixeles de los misiles que atacan al jugador, se deben usar valores enteros según la cantidad de pixeles deseados.
WMIN_PLASMA: Establece el ancho mínimo en pixeles de las balas de plasma que atacan al jugador, se deben usar valores enteros según la cantidad de pixeles deseados.
WMAX_PLASMA: Establece el alto máximo en pixeles de las balas de plasma que atacan al jugador, se deben usar valores enteros según la cantidad de pixeles deseados.
WMIN_VXITEM: Establece el ancho mínimo en pixeles de los objetos usados para distraer al jugador, se deben usar valores enteros según la cantidad de pixeles deseados.
WMAX_VXITEM: Establece el ancho máximo en pixeles de los objetos usados para distraer al jugador, se deben usar valores enteros según la cantidad de pixeles deseados.
MIN_SPEED_ENEMY: Establece el avance mínimo en pixeles por ciclo de los enemigos (misiles / balas de plasma), se deben usar valores enteros según la cantidad de pixeles deseados.
MAX_SPEED_ENEMY: Establece el avance máximo en pixeles por ciclo de los enemigos (misiles / balas de plasma), se deben usar valores enteros según la cantidad de pixeles deseados.
MIN_SPEED_VXITEM: Establece el avance mínimo en pixeles por ciclo de los objetos usados para distraer al jugador, se deben usar valores enteros según la cantidad de pixeles deseados.
MAX_SPEED_VXITEM: Establece el avance mínimo en pixeles por ciclo de los objetos usados para distraer al jugador, se deben usar valores enteros según la cantidad de pixeles deseados.
RATENEWENEMY: Establece la taza de ciclos para generar un nuevo enemigo.
RATENEWVXITEM: Establece la taza de ciclos para generar distractor.
RATE_PLAYER_SPEED: Establece la taza de la velocidad de movimiento del jugador.

#### Funciones personalizadas

- terminate(): Termina la ejecución del juego.
- holdPlayerAction(): Espera a que el jugador presioné una tecla para continuar con la ejecución.
- playerDefeated(playerHitBox, enemies): Evalúa si el jugador fue vencido por alguno de los enemigos, recibe 2 parámetros el primero es el hit box del jugador y el segundo una lista con los enemigos actuales en la pantalla.

#### Ejecución
Se realiza desde la línea 58 el código cuenta con comentarios para facilitar la lectura del código de realizar modificaciones recuerde añadir o modificar el comentario y compilar de nuevo para crear el ejecutable para el uso por parte del jugador.

## Créditos
Jairo Londoño.

## Licencia
Creative Commons – Limitada a las restricciones establecidas para Python y por los desarrolladores para PyGame.