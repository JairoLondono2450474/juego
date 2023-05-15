import pygame
import random
import sys
from pygame.locals import *

SCREEN_W = 800
SCREEN_H = 600
TEXT_COLOR = (255, 255, 255)
TEXT_COLOR2 = (0, 0, 0)
BG_COLOR = (0, 168, 255)
FPS = 40
WMIN_ROCKET = 10
WMAX_ROCKET = 25
WMIN_PLASMA = 10
WMAX_PLASMA = 20
WMIN_VXITEM = 50
WMAX_VXITEM = 90
MIN_SPEED_ENEMY = 1
MAX_SPEED_ENEMY = 8
MIN_SPEED_VXITEM = 1
MAX_SPEED_VXITEM = 3
RATENEWENEMY = 6
RATENEWVXITEM = 12
RATE_PLAYER_SPEED = 5


def terminate():
    pygame.quit()
    sys.exit()


def holdPlayerAction():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # Cierra el juego al presionar ESCAPE
                    terminate()
                return


def playerDefeated(playerHitBox, enemies):
    for v in enemies:
        if playerHitBox.colliderect(v['rect']):
            return True
    return False


def drawTxt(text, font, surface, x, y, color=TEXT_COLOR):
    textObj = font.render(text, 1, color)
    textArea = textObj.get_rect()
    textArea.topleft = (x, y)
    surface.blit(textObj, textArea)

# Ejecucion del juego
# establece un pygame, la ventana y la visibilidad para el cursor del ratón
pygame.init()
mainClock = pygame.time.Clock()
screenPlay = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption('Soldado Espacial')
pygame.mouse.set_visible(False)

# establece las fuentes
font = pygame.font.SysFont(None, 48)

# establece los sonidos
gameOverSound = pygame.mixer.Sound('./media/sounds/juegoterminado.wav')
pygame.mixer.music.load('./media/sounds/musicajuego.mp3')

# establece las imagenes
playerImage = pygame.image.load('./media/img/nave.png')
playerHitBox = playerImage.get_rect()
playerHitBox.width = 35
playerHitBox.height = 43
rocketImg = pygame.image.load('./media/img/misil.png')
plasmaImg = pygame.image.load('./media/img/plasma.png')
cloudImg = pygame.image.load('./media/img/nube.png')

# Muestra la pantalla inicial
drawTxt('Soldado Espacial', font, screenPlay,
        (SCREEN_W / 4), (SCREEN_H / 4))
drawTxt('Controles', font, screenPlay,
        (SCREEN_W / 4) - 180, (SCREEN_H / 4) + 50)
drawTxt('Moverse: W,A,S,D o con el Ratón', font, screenPlay,
        (SCREEN_W / 4) - 140, (SCREEN_H / 4) + 100)
drawTxt('Poderes', font, screenPlay,
        (SCREEN_W / 4) - 180, (SCREEN_H / 4) + 150)
drawTxt('Rebobinar: Z', font, screenPlay,
        (SCREEN_W / 4) - 140, (SCREEN_H / 4) + 200)
drawTxt('Ralentizar: X', font, screenPlay,
        (SCREEN_W / 4) - 140, (SCREEN_H / 4) + 250)
drawTxt('Presione una tecla para comenzar el juego...', font,
        screenPlay, (SCREEN_W / 4) - 180, (SCREEN_H / 4) + 300)
pygame.display.update()
holdPlayerAction()


maxScoore = 0
while True:
    # blucle del juego
    enemies = []
    clouds = []
    scoore = 0
    playerHitBox.topleft = (SCREEN_W / 2, SCREEN_H - 50)
    moveLeft = moveRight = moveUp = moveDown = False
    rewind = slow = False
    enemyAddCounter = 0
    vfItemAddCounter = 0
    pygame.mixer.music.play(-1, 0.0)

    while True:  # blucle de la partida
        scoore += 1  # incrementa el puntaje

        # blucle de acciones del jugador
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()

            if event.type == KEYDOWN:
                if event.key == ord('z'):
                    rewind = True
                if event.key == ord('x'):
                    slow = True
                if event.key == K_LEFT or event.key == ord('a'):
                    moveRight = False
                    moveLeft = True
                if event.key == K_RIGHT or event.key == ord('d'):
                    moveLeft = False
                    moveRight = True
                if event.key == K_UP or event.key == ord('w'):
                    moveDown = False
                    moveUp = True
                if event.key == K_DOWN or event.key == ord('s'):
                    moveUp = False
                    moveDown = True

            if event.type == KEYUP:
                if event.key == ord('z'):
                    rewind = False
                    scoore = 0
                if event.key == ord('x'):
                    slow = False
                    scoore = 0
                if event.key == K_ESCAPE:
                    terminate()

                if event.key == K_LEFT or event.key == ord('a'):
                    moveLeft = False
                if event.key == K_RIGHT or event.key == ord('d'):
                    moveRight = False
                if event.key == K_UP or event.key == ord('w'):
                    moveUp = False
                if event.key == K_DOWN or event.key == ord('s'):
                    moveDown = False

            if event.type == MOUSEMOTION:
                # Si se mueve el ratón, el jugador se mueve adonde el cursor esté.
                playerHitBox.move_ip(
                    event.pos[0] - playerHitBox.centerx, event.pos[1] - playerHitBox.centery)

        # Añade enemigos en la parte superior de la pantalla, de ser necesarios.
        if not rewind and not slow:
            enemyAddCounter += 1
        if enemyAddCounter == RATENEWENEMY:
            enemyAddCounter = 0
            # Establece la probabilidad de aparición de los enemigos más difíciles (misiles)
            if (random.randint(0, 100) <= 30):
                # Rocket Size
                rocketWidth = random.randint(WMIN_ROCKET, WMAX_ROCKET)
                rocketHeight = rocketWidth/(40/143)
                newEnemy = {'rect': pygame.Rect(random.randint(0, SCREEN_W-rocketWidth), 0 - rocketHeight, (rocketWidth -4), rocketHeight),
                            'speed': random.randint(MIN_SPEED_ENEMY, MAX_SPEED_ENEMY),
                            'surface': pygame.transform.scale(rocketImg, (rocketWidth, rocketHeight)),
                            }
            else:
                plasmaSize = random.randint(WMIN_PLASMA, WMAX_PLASMA)
                newEnemy = {'rect': pygame.Rect(random.randint(0, SCREEN_W-plasmaSize), 0 - plasmaSize, (plasmaSize - 3), (plasmaSize - 3)),
                         'speed': random.randint(MIN_SPEED_ENEMY, MAX_SPEED_ENEMY) + 2,
                         'surface': pygame.transform.scale(plasmaImg, (plasmaSize, plasmaSize)),
                         }
            enemies.append(newEnemy)

        # Añade nubes (objeto distractor) en la parte superior de la pantalla
        if not rewind and not slow:
            vfItemAddCounter += 1
        if vfItemAddCounter == RATENEWVXITEM:
            vfItemAddCounter = 0
            cloudSize = random.randint(WMIN_VXITEM, WMAX_VXITEM)
            newVxItem = {'rect': pygame.Rect(random.randint(0, SCREEN_W-cloudSize), 0 - cloudSize, cloudSize, cloudSize),
                         'speed': random.randint(MIN_SPEED_VXITEM, MAX_SPEED_VXITEM),
                         'surface': pygame.transform.scale(cloudImg, (cloudSize, cloudSize)),
                         }
            clouds.append(newVxItem)

        # Limita el movimiento del jugador de acuerdo con el tamaño de la pantalla de juego y de acuerdo con la taza de velocidad del jugador
        if moveLeft and playerHitBox.left > 0:
            playerHitBox.move_ip(-1 * RATE_PLAYER_SPEED, 0)
        if moveRight and playerHitBox.right < SCREEN_W:
            playerHitBox.move_ip(RATE_PLAYER_SPEED, 0)
        if moveUp and playerHitBox.top > 0:
            playerHitBox.move_ip(0, -1 * RATE_PLAYER_SPEED)
        if moveDown and playerHitBox.bottom < SCREEN_H:
            playerHitBox.move_ip(0, RATE_PLAYER_SPEED)

        # Mueve el cursor a la ubicacion del jugador.
        pygame.mouse.set_pos(playerHitBox.centerx,
                             playerHitBox.centery)

        # Mueve los enemigos hacia abajo.
        for b in enemies:
            if not rewind and not slow:
                b['rect'].move_ip(0, b['speed'])
            elif rewind:
                b['rect'].move_ip(0, -5)
            elif slow:
                b['rect'].move_ip(0, 1)
        # Mueve las nubes hacia abajo.
        for b in clouds:
            b['rect'].move_ip(0, b['speed'])

        # Elimina los enemigos que han caido por fuera de la pantalla
        for b in enemies[:]:
            if b['rect'].top > SCREEN_H:
                enemies.remove(b)

        # Elimina las nubes que han caido por fuera de la pantalla
        for b in clouds[:]:
            if b['rect'].top > SCREEN_H:
                clouds.remove(b)

        # Dibuja el mundo del juego en la ventana (fondo)
        screenPlay.fill(BG_COLOR)

        # Dibuja el puntaje actual y el puntaje máximo
        drawTxt('Puntos: %s' % (scoore), font, screenPlay, 10, 0)
        drawTxt('Record #1: %s' % (maxScoore),
                font, screenPlay, 10, 40)

        # Dibuja al jugador
        screenPlay.blit(playerImage, playerHitBox)

        # Dibuja cada misil
        for b in enemies:
            screenPlay.blit(b['surface'], b['rect'])

        # Dibuja cada nube
        for b in clouds:
            screenPlay.blit(b['surface'], b['rect'])
        pygame.display.update()

        if playerDefeated(playerHitBox, enemies):
            if scoore > maxScoore:
                maxScoore = scoore  # Establece nuevo puntaje máximo
            break

        mainClock.tick(FPS)

    # Frena el juego y muestra "Juego Terminado"
    pygame.mixer.music.stop()
    gameOverSound.play()

    drawTxt('Juego Terminado', font, screenPlay,
            (SCREEN_W / 3)-40, (SCREEN_H / 3), TEXT_COLOR2)
    drawTxt('Presione una tecla para repetir.', font, screenPlay,
            (SCREEN_W / 3) - 150, (SCREEN_H / 3) + 50, TEXT_COLOR2)
    pygame.display.update()
    holdPlayerAction()

    gameOverSound.stop()
