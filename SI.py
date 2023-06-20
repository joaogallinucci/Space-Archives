import pygame
from pygame.locals import *
from sys import exit
import random
import os

pygame.init()
pygame.mixer.init()

images = []
sounds = []
player = []
aliens = []
background = []
bullets = []
bulletside = 1
bulletdelay = 8
archives = []
executor = []
gameover = []

window = pygame.display.set_mode((500, 700))

def Main():
    global executor

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    if executor[0] != 0:
        Clock()
    if executor[1] != 0:
        BackgroundMoviment()
    if executor[2] != 0:
        ShootDelay()
    if executor[3] != 0:
        AlienMoviment()
    if executor[4] != 0:
        Shoots()
    if executor[5] != 0:
        PlayerMoviment()
    if executor[6] != 0:
        Collider()
    if executor[8] != 0:
        GameOverAnimator()
    if executor[7] != 0:
        Video()

def Clock():
    clock = pygame.time.Clock()
    clock.tick(30)

def PlayerMoviment():
    global player
    
    if pygame.key.get_pressed()[K_a]:
        player[0] = player[0] - player[2]
    
    if pygame.key.get_pressed()[K_d]:
        player[0] = player[0] + player[2]
    
    if pygame.key.get_pressed()[K_w]:
        player[1] = player[1] - player[2]
    
    if pygame.key.get_pressed()[K_s]:
        player[1] = player[1] + player[2]
    
    if pygame.key.get_pressed()[K_e]:
        CreateShoot()
    
    if player[0] > 418:
        player[0] = 418
    
    if player[0] < -11:
        player[0] = -11
    
    if player[1] < -13:
        player[1] = -13
    
    if player[1] > 613:
        player[1] = 613
    
def BackgroundMoviment():
    global background
    
    background[1] = background[1] + background[2]
    background[4] = background[4] + background[2]
    
    if background[1] >= 700:
        background[1] = background[4] - 700
    
    if background[4] >= 700:
        background[4] = background[1] - 700

def CreateShoot():
    global bullets, player, bulletside, bulletdelay, sounds
    
    bullet = []
    v = 8
    
    if bulletdelay == 0:
        if bulletside == -1:
            bullet.append(player[0] + 3)
            bullet.append(player[1] - 26)
            bullet.append(v)
    
        if bulletside == 1:
            bullet.append(player[0] + 62)
            bullet.append(player[1] - 26)
            bullet.append(v)
    
        bulletside = bulletside * -1
        
        bulletdelay = 8
    
        bullets.append(bullet)
        sounds[0].play()

def ShootDelay():
    global bulletdelay
    
    if bulletdelay > 0:
        bulletdelay = bulletdelay - 1

def Shoots():
    global bullets
    
    ram1 = []
    
    for bullet in bullets:
        x = bullet[0]
        y = bullet[1]
        v = bullet[2]
        
        y = y - v
        
        if y <= -40:
            pass
        else:
            ram2 = []
            ram2.append(x)
            ram2.append(y)
            ram2.append(v)
            
            ram1.append(ram2)
    
    bullets = ram1

def AlienGenerator():
    global archives, aliens
    
    m = 0
    
    for archive in archives:
        if archive == 'player.png':
            m = 1
        if archive == 'alien-1.png':
            m = 1
        if archive == 'stars.jpeg':
            m = 1
        if archive == 'bullet.png':
            m = 1
        if archive == 'SI.py':
            m = 1
        if archive == 'SI.exe':
            m = 1
        if archive == 'lifebar.png':
            m = 1
        if archive == 'gameover.png':
            m = 1
        if archive == 'shootsound.mp3':
            m = 1
        if archive == 'gameoversound.mp3':
            m = 1
        if archive == 'playerhurt.mp3':
            m = 1
        
        if m == 0:
            alien = []
            
            # Definindo eixo x do alien
            alien.append(random.randint(0, 300))
            
            # Definindo eixo y do alien
            alien.append(random.randint(-700, 0))
            
            # Definindo velocidade do alien
            alien.append(6)
            
            # Definindo arquivo do alien
            alien.append(archive)
            
            aliens.append(alien)
        
        m = 0

def AlienMoviment():
    global aliens
    
    ram1 = []
    
    for alien in aliens:
        x = alien[0]
        y = alien[1]
        v = alien[2]
        a = alien[3]
        
        y = y + v
        
        if y >= 700:
            y = random.randint(-700, 0)
            x = random.randint(0, 300)
        
        ram2 = []
        ram2.append(x)
        ram2.append(y)
        ram2.append(v)
        ram2.append(a)
        
        ram1.append(ram2)
    
    aliens = ram1

def AlienKill(target):
    global aliens
    
    os.remove(target[3])
    
    ram1 = []
    
    for alien in aliens:
        if alien[3] == target[3]:
            pass
        else:
            ram1.append(alien)
    
    aliens = ram1

def Collider():
    global player, bullets, aliens, gameover, executor, sounds
    
    playercollider = 0
    bulletcolliders = []
    alienscolliders = []
    
    # Definindo collider do player
    playercollider = pygame.draw.rect(window, (255, 255, 255), (player[0] + 14, player[1] + 16, 68, 60))
    
    # Definindo collider das balas
    for bullet in bullets:
        bulletcolliders.append(pygame.draw.rect(window, (255, 255, 255), (bullet[0] + 5, bullet[1] + 12, 20, 30)))
    
    # Definindo collider do alien
    for alien in aliens:
        alienscolliders.append(pygame.draw.rect(window, (255, 255, 255), (alien[0] + 3, alien[1] + 5, 45, 40)))
    
    b = 0
    a = 0
    for bullet in bulletcolliders:
        a = 0
        for alien in alienscolliders:
            if bullet.colliderect(alien):
                AlienKill(aliens[a])
                
                ram1 = []
                c = 0
                for bulletobject in bullets:
                    if c == b:
                        pass
                    else:
                        print(bulletobject)
                        ram1.append(bulletobject)
                    c = c + 1
                bullets = ram1
            a = a + 1
        b = b + 1
    
    a = 0
    for alien in alienscolliders:
        if alien.colliderect(playercollider):
            AlienKill(aliens[a])
            sounds[2].play()
            if player[3] == 50:
                sounds[1].play()
                player[3] = 0
                gameover[0] = 1
                executor[2] = 0
                executor[5] = 0
                executor[8] = 1
            if player[3] == 100:
                player[3] = 50
        a = a + 1

def GameOverAnimator():
    global gameover
    
    if gameover[1] == 0:
        if gameover[0] == 1:
            gameover[0] = 2
            gameover[1] = 8
        else:
            gameover[0] = 1
            gameover[1] = 8
    else:
        gameover[1] = gameover[1] - 1

def Video():
    global images, player, background, bullets, aliens, gameover
    
    # Background
    window.blit(images[2], (background[3], background[4]))
    window.blit(images[2], (background[0], background[1]))
    
    # Aliens
    for alien in aliens:
        window.blit(images[1], (alien[0], alien[1]))
    
    # Balas
    for bullet in bullets:
        window.blit(images[3], (bullet[0], bullet[1]))
    
    if gameover[0] == 0:
        # Lifebar do player
        if player[3] == 100:
            pygame.draw.rect(window, (0, 255, 0), (player[0] + 22, player[1] + 90, 60, 14))
        if player[3] == 50:
            pygame.draw.rect(window, (255, 255, 0), (player[0] + 22, player[1] + 90, 30, 14))
        if player[3] == 0:
            pass
        window.blit(images[4], (player[0], player[1] + 76))
        
        # Player
        window.blit(images[0], (player[0], player[1]))
    if gameover[0] == 1:
        window.blit(images[5], (125, 215))

def Init():
    global images, player, background, archives, sounds, executor, gameover
    
    # Definindo a imagem do player / id 0
    images.append(pygame.transform.scale(pygame.image.load("player.png"), (90, 90)))
    
    # Definindo imagem do alien 1 / id 1
    images.append(pygame.transform.scale(pygame.image.load("alien-1.png"), (50, 50)))
    
    # Definindo imagem do fundo / id 2
    images.append(pygame.transform.scale(pygame.image.load("stars.jpeg"), (500, 700)))
    
    # Definindo imagem da bala / id 3
    images.append(pygame.transform.scale(pygame.image.load("bullet.png"), (30, 50)))
    
    # Definindo imagem da lifebar / id 4
    images.append(pygame.transform.scale(pygame.image.load("lifebar.png"), (95, 42)))
    
    # Definindo imagem de gameover / id 5
    images.append(pygame.transform.scale(pygame.image.load("gameover.png"), (250, 250)))
    
    # Definindo eixo x do player / id 0
    player.append(198)
    
    # Definindo eixo y do player / id 1
    player.append(312)
    
    # Definindo velocidade do player / id 2
    player.append(6)
    
    # Definindo a lifebar do player / id 3
    player.append(100)
    
    # Definindo eixo x do background 1 / id 0
    background.append(0)
    
    # Definindo eixo y do background 1 / id 1
    background.append(0)
    
    # Definindo velocidade do background 1 / id 2
    background.append(5)
    
    # Definindo eixo x do background 2 / id 3
    background.append(0)
    
    # Definindo eixo y do background 2 / id 4
    background.append(-700)
    
    # Definindo a lista de arquivos
    archives = os.listdir()
    
    # Definindo som do tiro / id 0
    sounds.append(pygame.mixer.Sound('shootsound.mp3'))
    
    # Definindo som do game over / id 1
    sounds.append(pygame.mixer.Sound('gameoversound.mp3'))
    
    # Definindo som do player hurt / id 2
    sounds.append(pygame.mixer.Sound('playerhurt.mp3'))
    
    # Definindo execucao do Clock / id 0
    executor.append(1)
    
    # Definindo execucao do BackgroundMoviment / id 1
    executor.append(1)
    
    # Definindo execucao do ShootDelay / id 2
    executor.append(1)
    
    # Definindo execucao do AlienMoviment / id 3
    executor.append(1)
    
    # Definindo execucao do Shoots / id 4
    executor.append(1)
    
    # Definindo execucao do PlayerMoviment / id 5
    executor.append(1)
    
    # Definindo execucao do Collider / id 6
    executor.append(1)
    
    # Definindo execucao do Video / id 7
    executor.append(1)
    
    # Definindo GameOverAnimator / id 8
    executor.append(0)
    
    # Definindo gameover como false / id 0
    gameover.append(0)
    
    # Definindo contador do gameover / id 1
    gameover.append(0)

Init()
AlienGenerator()
while True:    
    window.fill((0,0,0))
    Main()
    pygame.display.flip()
