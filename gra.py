import pygame
import random
import time
import sys
import math

# initiation pygame
pygame.init()
#mouse disable
pygame.mouse.set_visible(False)
#resolution
window_width = 1920
window_height = 1080
window = pygame.display.set_mode((window_width, window_height))
#font in the game
font = pygame.font.Font(None, 36)
#start player position 
x = 0
y = 0
#gold
points_counter = 100
#level
level = 48
#number of enemies when game started
number_devils = 0
number_fasts = 0
number_mutants = 0
number_ghosts = 0
#number of obstacless when game started
number_obstacles = 8
#max number of obstacles
max_obstacles = 18
#bullets in magazine
magazine = 100
#glag for gun hide/pick
gun_on = False
#basic player speed
speed = 15
#max player speed
max_speed = 15
#flags for eliminate double click in abilities
p_key_pressed = False
p_key_released = True
o_key_pressed = False
o_key_released = True
i_key_pressed = False
i_key_released = True
m_key_pressed = False
m_key_released = True
u_key_pressed = False
u_key_released = True
r_key_pressed = False
r_key_released = True
#flag for shield active/dont active
powershield = False
#boss hp
boss_hp = 50
#the flag checks if there is a boss fight
bs = False
#lists
destroyed_obstacles_list = []
bullets_list = []
dead_enemy_list = []
boss_list = []
dead_boss_list = []
obstacles_list =[]
enemy_list=[]

#intro textures
menu = pygame.image.load("textures/menu.png")
intro1 = pygame.image.load("textures/intro.png")
intro2 = pygame.image.load("textures/intro2.png")
intro3 = pygame.image.load("textures/intro3.png")
olchastudio = pygame.image.load("textures/olchastudio.png")
#backgrounds textures
background1 = pygame.image.load('textures/tlo.jpg')
background2 = pygame.image.load('textures/tlo2.jpg')
background3 = pygame.image.load('textures/tlo3.jpg')
background4 = pygame.image.load('textures/tlo4.1.jpg')
#scaling background textures
background1 = pygame.transform.scale(background1, window.get_size())
background2 = pygame.transform.scale(background2, window.get_size())
background3 = pygame.transform.scale(background3, window.get_size())
background4 = pygame.transform.scale(background4, window.get_size())
#list of background textures
background_list = [background1, background2, background3]
#default background
background = background1

#choose random background without backgorund4
#set background 4 in 50 lvl (boss fight)
def random_background():
    if level % 50 == 0:
        background = background4
    else:
        background = random.choice(background_list)
    return background

#all player textures scaled to 40x40 px

#player basic texture:
player1_texture = pygame.transform.scale(
    pygame.image.load('textures/player.png'), (40, 40))
#playe rect
player1_rect = player1_texture.get_rect()
#player mask
player1_mask = pygame.mask.from_surface(player1_texture)
#player texture with shield
player1_texture_shield = pygame.image.load('textures/playershield1.png')

#player texture with gun adaptate to player direction
player_plazma_left_texture = pygame.transform.scale(
    pygame.image.load('textures/playerplazmaL.png'), (40, 40))

player_plazma_right_texture = pygame.transform.scale(
    pygame.image.load('textures/playerplazmaR.png'), (40, 40))

player_plazma_top_texture = pygame.transform.scale(
    pygame.image.load('textures/playerplazmaT.png'), (40, 40))

player_plazma_down_texture = pygame.transform.scale(
    pygame.image.load('textures/playerplazmaB.png'), (40, 40))

#player texture with gun and shield adaptate to player direction
player_plazma_left_shield_texture = pygame.transform.scale(
    pygame.image.load('textures/playerpalzmaLS.png'), (40, 40))

player_plazma_right_shield_texture = pygame.transform.scale(
    pygame.image.load('textures/playerpalzmaPS.png'), (40, 40))

player_plazma_top_shield_texture = pygame.transform.scale(
    pygame.image.load('textures/playerplazmaTS.png'), (40, 40))

player_plazma_down_shield_texture = pygame.transform.scale(
    pygame.image.load('textures/playerpalzmaDS.png'), (40, 40))

#player dead animation
player_dead_animation = [pygame.image.load('textures/playerdead1.png'), pygame.image.load(
    'textures/playerdead2.png'), pygame.image.load('textures/playerdead3.png')]

#last player texture
last_texture = player1_texture
#last player texture with shield
last_texture_with_shield = player1_texture

#bullet speed
bullet_speed = 70
#basic bullet direction
bullet_direction = 'right'
#flag checks a bullet are shooted
bullet_fired = True
#bullet right,left size
bullet_width = 15
bullet_height = 5
#bullet top,down size
bullet2_width = 5
bullet2_height = 15

#bullet textures adaptate to bullet direction
bullet_texture_right = pygame.transform.scale(
    pygame.image.load('textures/bulletR.png'), (bullet_width, bullet_height))

bullet_textureL = pygame.transform.scale(
    pygame.image.load('textures/bulletL.png'), (bullet_width, bullet_height))

bullet_textureT = pygame.transform.scale(
    pygame.image.load('textures/bulletT.png'), (bullet2_width, bullet2_height))

bullet_textureD = pygame.transform.scale(
    pygame.image.load('textures/bulletD.png'), (bullet2_width, bullet2_height))

# bullet explosion textures
bullet_boom1_texture = pygame.transform.scale(
    pygame.image.load('textures/bulletboom1.png'), (20, 20))

bullet_boom2_texture = pygame.transform.scale(
    pygame.image.load('textures/bulletboom2.png'), (20, 20))

bullet_boom3_texture = pygame.transform.scale(
    pygame.image.load('textures/bulletboom3.png'), (20, 20))

# bullet explosion animation
bullet_boom_list = [bullet_boom1_texture,
                    bullet_boom2_texture, 
                    bullet_boom3_texture]

# monsters textures

#devil size
devil_width = 50
devil_height = 50
#devil speed
devil_speed = 6
#devil collision parametr
devil_collision = 50
#devil texture
devil_texture = pygame.transform.scale(
    pygame.image.load('textures/enemy.png'), (devil_width, devil_height))
#devil rect
devil_rect = devil_texture.get_rect()
#devil death animation (killed by shield)
devil_dead_animation = [pygame.transform.scale(pygame.image.load('textures/devildead1.png'), (devil_width, devil_height)), pygame.transform.scale(pygame.image.load(
    'textures/devildead2.png'), (devil_width, devil_height)), pygame.transform.scale(pygame.image.load('textures/devildead3.png'), (devil_width, devil_height))]
#devil death animation (killed by gun)
devil_bullet_dead_animation = [pygame.transform.scale(pygame.image.load('textures/devildead1v2.png'), (devil_width, devil_height)), pygame.transform.scale(pygame.image.load(
    'textures/devildead2v2.png'), (devil_width, devil_height)), pygame.transform.scale(pygame.image.load('textures/devildead3v2.png'), (devil_width, devil_height))]
#devil corpses texture (killed by gun)
devil_bullet_corpses = pygame.transform.scale(pygame.image.load(
    'textures/devildead3v2.png'), (devil_width, devil_height))
#devil corpses texture (killed by shield)
devil_corpses = pygame.transform.scale(pygame.image.load(
    'textures/devildead3.png'), (devil_width, devil_height))

#fast size
fast_width = 40
fast_height = 40
#fast speed
fast_speed = 15
#fast collision parametr
fast_collison = 40
#fast texture
fast_texture = pygame.transform.scale(
    pygame.image.load('textures/fast.png'), (fast_width, fast_height))
#fast rect
fast_rect = fast_texture.get_rect()
#fast death animation (killed by shield)
fast_dead_animation = [pygame.transform.scale(pygame.image.load('textures/fastdead1.png'), (fast_width, fast_height)), pygame.transform.scale(pygame.image.load(
    'textures/fastdead2.png'), (fast_width, fast_height)), pygame.transform.scale(pygame.image.load('textures/fastdead3.png'), (fast_width, fast_height))]
#fast death animation (killed by gun)
fast_bullet_dead_animation = [pygame.transform.scale(pygame.image.load('textures/fastdead1v2.png'), (fast_width, fast_height)), pygame.transform.scale(pygame.image.load(
    'textures/fastdead2v2.png'), (60, 60)), pygame.transform.scale(pygame.image.load('textures/fastdead3v2.png'), (60, 60))]
#fast corpses texture
fast_corpses = pygame.transform.scale(pygame.image.load(
    'textures/fastdead3v2.png'), (100, 100))

#mutant size
mutant_width = 100
mutant_height = 100
#mutant speed
mutant_speed = 3
#mutant collision parametr
mutant_collision = 100
#mutant texture left direction
mutant_texture_left_direction = pygame.transform.scale(
    pygame.image.load('textures/mutantL.png'), (mutant_width, mutant_height))
#mutant texture right direction
mutant_texture_right_direction = pygame.transform.scale(
    pygame.image.load('textures/mutantR.png'), (mutant_width, mutant_height))
#mutant rect
mutant_rect = mutant_texture_left_direction.get_rect()
#mutant corpses (killed by gun)
mutant_corpses_bullet = pygame.transform.scale(pygame.image.load(
    'textures/mutantdead3L.png'), (mutant_width, mutant_height))
#mutant corpses (killed by shield)
mutant_corpses_shield = pygame.transform.scale(pygame.image.load(
    'textures/mutantL.dead3v3.png'), (mutant_width, mutant_height))
#mutant death animation (killed by shield)
mutant_bullet_dead_animation = [pygame.transform.scale(pygame.image.load('textures/mutantdead1L.png'), (mutant_width, mutant_height)), pygame.transform.scale(pygame.image.load(
    'textures/mutantdead2L.png'), (mutant_width, mutant_height)), pygame.transform.scale(pygame.image.load('textures/mutantdead3L.png'), (mutant_width, mutant_height))]
#mutant death animation (killed by gun)
mutant_shield_dead_animation = [pygame.transform.scale(pygame.image.load('textures/mutantL.dead1v3.png'), (mutant_width, mutant_height)), pygame.transform.scale(pygame.image.load(
    'textures/mutantL.dead2v3.png'), (mutant_width, mutant_height)), pygame.transform.scale(pygame.image.load('textures/mutantL.dead3v3.png'), (mutant_width, mutant_height))]

#ghost size
ghost_width = 50
ghost_height = 50
#ghost speed
ghost_speed = 10
#ghost collision parametr
ghost_collision = 50
#ghost texture left direction
ghost_texture_left_direction = pygame.transform.scale(
    pygame.image.load('textures/ghostL.png'), (ghost_width, ghost_height))
#ghost texture right direction
ghost_texture_right_direction = pygame.transform.scale(
    pygame.image.load('textures/ghostR.png'), (ghost_width, ghost_height))
#ghost rect
ghost_rect = ghost_texture_left_direction.get_rect()
#ghost death animation
ghost_dead_animation = [pygame.transform.scale(pygame.image.load('textures/ghostdead1L.png'), (ghost_width, ghost_height)), pygame.transform.scale(pygame.image.load(
    'textures/ghostdead2L.png'), (ghost_width, ghost_height)), pygame.transform.scale(pygame.image.load('textures/ghostdead3L.png'), (ghost_width, ghost_height))]
#ghost corpses
ghost_corpses = pygame.transform.scale(pygame.image.load(
    'textures/ghostdead3L.png'), (ghost_width, ghost_height))

#boss texture
boss_texture = pygame.transform.scale(
    pygame.image.load('textures/boss.png'), (300, 300))
#boss rect
boss_rect = boss_texture.get_rect()
#boss death animation
boss_dead_animation = [pygame.transform.scale(pygame.image.load('textures/bossdead1.png'), (300, 300)), pygame.transform.scale(
    pygame.image.load('textures/bossdead2.png'), (300, 300)), pygame.transform.scale(pygame.image.load('textures/bossdead3.png'), (300, 300))]
#boss corpses
boss_corpses = pygame.transform.scale(
    pygame.image.load('textures/bossdead3c.png'), (300, 300))

# obstacles textures

#tree size
tree_width = 70
tree_height = 100
#tree texture
tree_texture = pygame.transform.scale(
    pygame.image.load('textures/drzewo.png'), (tree_width, tree_height))
#tree rect
tree_rect = tree_texture.get_rect()

#stone size
stone_width = 50
stone_height = 50
#stone texture
stone_texture = pygame.transform.scale(
    pygame.image.load('textures/kamien.png'), (stone_width, stone_height))
#stone rect
stone_rect = stone_texture.get_rect()

#bush size
bush_width = 40
bush_height = 40
#bush texture
bush_texture = pygame.transform.scale(
    pygame.image.load('textures/krzak.png'), (bush_width, bush_height))
#bush rect
bush_rect = bush_texture.get_rect()

#bones size
bones_width = 70
bones_height = 30
#bones texture
bones_texture = pygame.transform.scale(
    pygame.image.load('textures/bones.png'), (bones_width, bones_height))
#bones rect
bones_rect = bones_texture.get_rect()

#sarna size
sarna_width = 50
sarna_height = 30
#sarna texture
sarna_texture = pygame.transform.scale(
    pygame.image.load('textures/sarna.png'), (bones_width, bones_height))
#sarna rect
sarna_rect = sarna_texture.get_rect()

#dead tree size
dead_tree_width = 70
dead_tree_height = 100
#dead tree texture
dead_tree_texture = pygame.transform.scale(
    pygame.image.load('textures/deadtree.png'), (dead_tree_width, dead_tree_height))
#dead tree rect
dead_tree_rect = dead_tree_texture.get_rect()

#obstacle destruction animation
obstacle_destroy_animation = [pygame.transform.scale(pygame.image.load('textures/destroyednature1.png'), (50, 50)), pygame.transform.scale(
    pygame.image.load('textures/destroyednature2.png'), (50, 50)), pygame.transform.scale(pygame.image.load('textures/destroyednature3.png'), (50, 50))]
#destroyed obstacle texture 
destroyed_obstacle_texture = pygame.transform.scale(
    pygame.image.load('textures/destroyednature3.png'), (50, 50))


# sounds

intro_sound = pygame.mixer.Sound('sounds/intro.mp3')
#steps sound
steps_sound = pygame.mixer.Sound('sounds/kroki.mp3')
#next level sound
next_level_sound = pygame.mixer.Sound('sounds/pickup.mp3')
#earn gold sound
gold_sound = pygame.mixer.Sound('sounds/gold.mp3')
#death sounds
player_death_sound = pygame.mixer.Sound('sounds/playerdead.mp3')
devil_death_sound = pygame.mixer.Sound('sounds/devildead.mp3')
devil_death_sound.set_volume(0.5)
fast_death_sound = pygame.mixer.Sound('sounds/fastdead.mp3')
fast_death_sound.set_volume(0.3)
mutant_death_sound = pygame.mixer.Sound('sounds/mutantdead.mp3')
ghost_death_sound = pygame.mixer.Sound('sounds/ghostdead.mp3')
boss_death_sound = pygame.mixer.Sound('sounds/boss_death.mp3')
#obstacle destruction sound
destruction_sound = pygame.mixer.Sound('sounds/destruction.mp3')
destruction_sound.set_volume(0.2)
boss_death_sound.set_volume(0.2)
#immersive mounsters sounds (playing when player is close to monster)
monsters1_sound = pygame.mixer.Sound('sounds/monsters.mp3')
monsters1_sound.set_volume(0.5)
monsters2_sound = pygame.mixer.Sound('sounds/monsters2.mp3')
monsters2_sound.set_volume(0.5)
monsters_sounds = [monsters1_sound, monsters2_sound]
#boss sound
boss_sound = pygame.mixer.Sound('sounds/boss_sound.mp3')
boss_sound.set_volume(0.5)
#pick/hide gun sound
gun_sound = pygame.mixer.Sound('sounds/gunsound.mp3')
gun_sound.set_volume(0.6)
#buy ammo sound
reload_sound = pygame.mixer.Sound('sounds/reload.mp3')
reload_sound.set_volume(0.2)
#buy speed boost sound
speed_sound = pygame.mixer.Sound('sounds/speed.mp3')
speed_sound.set_volume(0.5)
#bouy shield sound
shield_sound = pygame.mixer.Sound('sounds/shield.mp3')
shield_sound.set_volume(0.5)
#buy refresh sound
refresh_sound = pygame.mixer.Sound('sounds/refresh.mp3')
refresh_sound.set_volume(0.5)

#playing sound only when nothing is playing
def play_sound(sound):
    if not pygame.mixer.get_busy():
        sound.play()

#stop sound
def stop_sound(sound):
    sound.stop()

#game intro
def start():
    pass
'''
    #shows all intro slaids and play intro music refresh screen beetween intro slaids
    window.blit(olchastudio, (1, 1))
    intro_sound.play()
    pygame.display.update()
    time.sleep(4.4)
    window.blit(intro1, (1, 1))
    pygame.display.update()
    time.sleep(2.4)
    window.blit(intro2, (1, 1))
    pygame.display.update()
    time.sleep(4.6)
    window.blit(intro3, (1, 1))
    pygame.display.update()
    time.sleep(4)
    window.blit(menu, (1, 1))
    pygame.display.update()
    waiting = True
    #game was started when player press space
    while waiting:
        play_sound(intro_sound)
        for i in pygame.event.get():
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                waiting = False
                stop_sound(intro_sound)'''

#loading objects in the map:enemies,obstacles,corpses itd

def collision(lista,rect,x,y):
        collision = True
        while collision:
            collision = False
            for i in lista:
                if rect.move(x, y).colliderect(i.rect) or rect.move(x, y).colliderect(player1_rect):
                    collision = True
                    break
                elif math.dist((x, y), player1_rect.center) < 200:
                    collision = True
                    break
            if collision:
                x = random.randint(20, window_width-90)
                y = random.randint(20, window_height-150)
        return x,y
                

def load(quantity, objectt, lista, rect):
    for i in range(quantity):
        if lista == obstacles_list:        
            if background == background1 or background==background3:
                x = random.randint(20, window_width-20)
                y = random.randint(20, window_height-20)
            elif background == background2:
                #obstacles dont spawn on skull
                x = random.randint(20, window_width-90)
                y = random.randint(20, window_height-150)
        else:
            x = random.randint(20, window_width-90)
            y = random.randint(20, window_height-150)
            
        if lista == enemy_list:
            x = random.randint(50, window_width-50)
            y = random.randint(50, window_height-50)
                        
        if background != background4:
            x,y = collision(lista,rect,x,y)    
            objectt(x, y)
        else:
            x = random.randint(50, window_width-50)
            y = random.randint(50, window_height-50)
            x,y = collision(lista,rect,x,y)    
            objectt(x, y)


class Boss:
    def __init__(self, x, y, width, height, texture, speed, collision):
        self.rect = pygame.Rect(x, y, width, height)
        self.texture = texture
        self.speed = speed
        self.collision = collision
        self.direction = (1, 0)
        self.mask = pygame.mask.from_surface(texture)
        self.prev_pos = self.rect.copy()
        self.x = self.rect.x
        self.y = self.rect.y

    def update(self):
        self.prev_pos = self.rect.copy()
        self.x, self.y = self.rect.x, self.rect.y
        self.rect.x += self.speed * self.direction[0]
        self.rect.y += self.speed * self.direction[1]

        for i in borders_list:
            if self.rect.colliderect(i.rect):
                self.rect = self.prev_pos
                break
            
        for i in enemy_list:
            offset = (self.rect.x - i.x,
            self.rect.y - i.y)
            if i.mask.overlap(mask, offset):   
                i.rect = i.prev_pos
                
            
        if random.random() < 0.05:
            self.change_direction()

    def change_direction(self):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        new_direction = self.direction
        while new_direction == self.direction:
            new_direction = random.choice(directions)
        self.direction = new_direction

    def draw(self, surface):
        surface.blit(self.texture, self.rect)

    def delete(self):
        boss_list.remove(self)
        dead_boss_list.append(self)
        del self


def boss():
    global bs
    boss_list = []
    if level % 48 == 0:
        boss = Boss(500, 500, 300, 300, boss_texture, 1, 300)
        boss_list.append(boss)
        bs = True

    return boss_list


boss_list = boss()


def deadscreen():
    dead = pygame.image.load("textures/deadscreen.png")
    global level
    global points_counter
    global number_devils
    global number_fasts
    global number_mutants
    global number_ghosts
    global number_obstacles
    global p_key_pressed
    global p_key_released
    global o_key_pressed
    global o_key_released
    global i_key_pressed
    global i_key_released
    global m_key_pressed
    global m_key_released
    global powershield
    global speed
    global x
    global y
    global magazine
    global background
    global background1
    global gun_on
    waiting = True
    w8 = True
    end_width, end_height = window_width, window_height
    end_surface = pygame.Surface((end_width, end_height))
    end_texture = pygame.transform.scale(pygame.image.load(
        "textures/end.png"), (end_width, end_height))
    end_texture_rect = end_texture.get_rect()
    end_surface.blit(end_texture, end_texture_rect)
    end_x = 0
    end_y = 0
    window.blit(end_surface, (end_x, end_y))
    pygame.display.update()
    time.sleep(2)
    window.blit(dead, (0, 0))
    Dfont = pygame.font.Font('font/snap.ttf', 100)

    with open('best_score.txt', 'r') as f:
        best_score = int(f.read())

    if level > best_score:
        with open('best_score.txt', 'w') as f:
            f.write(str(level))
        points2_text = Dfont.render(
            f'Your record {level} levels', True, (255, 0, 0))
        window.blit(points2_text, (window_width/4-80, window_height/4+100))
    else:
        points2_text = Dfont.render(
            f'Your record: {best_score} levels', True, (255, 0, 0))
        window.blit(points2_text, (window_width/4-80, window_height/4+100))

    points_text = Dfont.render(
        f'You survived: {level} levels', True, (255, 0, 0))
    window.blit(points_text, (window_width/4 - 80, window_height/4))

    pygame.display.update()
    while waiting:
        for i in pygame.event.get():
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                waiting = False
                window.blit(menu, (1, 1))
                pygame.display.update()
                while w8:
                    for i in pygame.event.get():
                        keys = pygame.key.get_pressed()
                        if keys[pygame.K_SPACE]:
                            time.sleep(0.5)
                            points_counter = 0
                            number_devils = 0
                            number_fasts = 0
                            number_mutants = 0
                            number_ghosts = 0
                            number_obstacles = 8
                            p_key_pressed = False
                            p_key_released = True
                            o_key_pressed = False
                            o_key_released = True
                            i_key_pressed = False
                            i_key_released = True
                            m_key_pressed = False
                            m_key_released = True
                            powershield = False
                            background = background1
                            speed = 8
                            level = 0
                            gun_on = False
                            magazine = 0
                            w8 = False
                            right.color = (255, 0, 0)
                            pygame.display.update()
                            break
            elif keys[pygame.K_ESCAPE]:
                sys.exit()


def pause():
    pauza = pygame.image.load("textures/pauza.png")
    waiting = True
    while waiting:
        window.blit(pauza, (1, 1))
        pygame.display.update()
        for i in pygame.event.get():
            keys = pygame.key.get_pressed()
            if keys[pygame.K_m]:
                waiting = False
                time.sleep(0.5)


def gun1():
    gun_sound.play()
    shield_banner = pygame.transform.scale(
        pygame.image.load("textures/gunpick.png"), (300, 200))
    window.blit(shield_banner, (window_width/2 - 140, window_height/2 - 140))
    pygame.display.update()
    time.sleep(0.5)


def gun2():
    gun_sound.play()
    shield_banner = pygame.transform.scale(
        pygame.image.load("textures/gunhide.png"), (300, 200))
    window.blit(shield_banner, (window_width/2 - 140, window_height/2 - 140))
    pygame.display.update()
    time.sleep(0.5)


def speed_boost():
    speed_boost_banner = pygame.transform.scale(
        pygame.image.load("textures/turbo.png"), (300, 200))
    max_speed_banner = pygame.transform.scale(
        pygame.image.load("textures/maxspeed.png"), (300, 200))
    if speed < 15:
        speed_sound.play()
        window.blit(speed_boost_banner,
                    (window_width/2-140, window_height/2-140))
    else:
        window.blit(max_speed_banner, (window_width /
                    2 - 140, window_height/2 - 140))
    pygame.display.update()
    time.sleep(1)


def refresh():
    refresh_sound.play()
    refresh_banner = pygame.transform.scale(
        pygame.image.load("textures/refresh.png"), (300, 200))
    window.blit(refresh_banner, (window_width/2 - 140, window_height/2 - 140))
    pygame.display.update()
    time.sleep(1)


def shield():
    shield_sound.play()
    shield_banner = pygame.transform.scale(
        pygame.image.load("textures/shield.png"), (300, 200))
    window.blit(shield_banner, (window_width/2 - 140, window_height/2 - 140))
    pygame.display.update()
    time.sleep(1)


def reeload():
    reload_sound.play()
    refresh_banner = pygame.transform.scale(
        pygame.image.load("textures/reload.png"), (300, 200))
    window.blit(refresh_banner, (window_width/2 - 140, window_height/2 - 140))
    pygame.display.update()
    time.sleep(1)


class Border:
    def __init__(self, x, y, width, height, color=(255, 0, 0)):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)


def borders():
    borders_list = []
    global right

    up = Border(1, 1, window_width, 1)
    borders_list.append(up)

    down = Border(1, window_height-1, window_width, 1)
    borders_list.append(down)

    left = Border(1, 1, 1, window_height)
    borders_list.append(left)

    right = Border(window_width-1, 1, 1, window_height, (255, 0, 0))
    borders_list.append(right)

    return borders_list


borders_list = borders()


class Obstacle:
    def __init__(self, x, y, width, height, texture):
        self.rect = pygame.Rect(x, y, width, height)
        self.texture = texture
        self.mask = pygame.mask.from_surface(texture)

    def draw(self, surface):
        surface.blit(self.texture, self.rect)

    def delete(self):
        destroyed_obstacles_list.append(self)
        obstacles_list.remove(self)
        del self


def obstacles():
    obstacles_list = []

    def tree(xtree, ytree):
        tree = Obstacle(xtree, ytree, tree_width,
                        tree_height, tree_texture)
        obstacles_list.append(tree)

    def stone(xstone, ystone):
        stone = Obstacle(xstone, ystone, stone_width,
                         stone_height, stone_texture)
        obstacles_list.append(stone)

    def bush(xbush, ybush):
        bush = Obstacle(xbush, ybush, bush_width,
                        bush_height, bush_texture)
        obstacles_list.append(bush)

    def bones(xbones, ybones):
        bones = Obstacle(xbones, ybones, bones_width,
                         bones_height, bones_texture)
        obstacles_list.append(bones)

    def sarna(xsarna, ysarna):
        sarna = Obstacle(xsarna, ysarna, sarna_width,
                         sarna_height, sarna_texture)
        obstacles_list.append(sarna)

    def deadtree(xdeadtree, ydeadtree):
        deadtree = Obstacle(xdeadtree, ydeadtree, dead_tree_width,
                            dead_tree_height, dead_tree_texture)
        obstacles_list.append(deadtree)

    if background == background1:
        load(number_obstacles, tree, obstacles_list, tree_rect)
        load(number_obstacles-4, sarna, obstacles_list, sarna_rect)
        load(number_obstacles-2, bush, obstacles_list, bush_rect)
        load(number_obstacles-6, stone, obstacles_list, stone_rect)

    if background == background2:
        load(number_obstacles, deadtree, obstacles_list, dead_tree_rect)
        load(number_obstacles-2, bones, obstacles_list, bones_rect)
        load(number_obstacles-1, stone, obstacles_list, stone_rect)
        load(number_obstacles-2, sarna, obstacles_list, sarna_rect)

    if background == background3:
        load(number_obstacles+4, deadtree, obstacles_list, dead_tree_rect)
        load(number_obstacles+6, bones, obstacles_list, bones_rect)
        load(number_obstacles-2, sarna, obstacles_list, sarna_rect)
    if background == background4:
        pass

    return obstacles_list


obstacles_list = obstacles()


class Enemy:
    def __init__(self, x, y, width, height, texture, speed, collision, enemy_type):
        self.rect = pygame.Rect(x, y, width, height)
        self.texture = texture
        self.speed = speed
        self.collision = collision
        self.direction = (1, 0)
        self.type = enemy_type
        self.mask = pygame.mask.from_surface(texture)
        self.prev_pos = self.rect.copy()
        self.x = self.rect.x
        self.y = self.rect.y

    def update(self, obstacles_list):
        self.prev_pos = self.rect.copy()
        self.x, self.y = self.rect.x, self.rect.y
        self.rect.x += self.speed * self.direction[0]
        self.rect.y += self.speed * self.direction[1]

        for i in obstacles_list:
            if self.type == 'ghost':
                continue
            if self.rect.colliderect(i.rect):
                self.rect = self.prev_pos
                break

        for i in borders_list:
            if self.rect.colliderect(i.rect):
                self.rect = self.prev_pos
                break

        if random.random() < 0.05:
            self.change_direction()

    def change_direction(self):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        new_direction = self.direction
        while new_direction == self.direction:
            new_direction = random.choice(directions)
        self.direction = new_direction

    def mirror(self, L, R):
        self.L = L
        self.R = R
        new_direction = self.direction
        if self.type == 'mutant':
            if new_direction == (1, 0):
                self.texture = R
            elif new_direction == (-1, 0):
                self.texture = L
        elif self.type == 'ghost':
            if new_direction == (1, 0):
                self.texture = R
            elif new_direction == (-1, 0):
                self.texture = L

    def draw(self, surface):
        surface.blit(self.texture, self.rect)

    def delete(self):
        dead_enemy_list.append(self)
        enemy_list.remove(self)
        del self


def enemies():
    global boss_spawned
    enemy_list = []

    def devil(xdevil, ydevil):
        devil = Enemy(xdevil, ydevil, devil_width,
                      devil_height, devil_texture, devil_speed, devil_collision, 'devil')
        enemy_list.append(devil)

    def fast(xfast, yfast):
        fast = Enemy(xfast, yfast, fast_width,
                     fast_height, fast_texture, fast_speed, fast_collison, 'fast')
        enemy_list.append(fast)

    def mutant(xmutant, ymutant):
        mutant = Enemy(xmutant, ymutant, mutant_width,
                       mutant_height, mutant_texture_left_direction, mutant_speed, mutant_collision, 'mutant')
        enemy_list.append(mutant)

    def ghost(xghost, yghost):
        ghost = Enemy(xghost, yghost, ghost_width,
                      ghost_height, ghost_texture_left_direction, ghost_speed, ghost_collision, 'ghost')
        enemy_list.append(ghost)

    if background != background4:
        if level % 5 == 0:
            load(number_ghosts, ghost, obstacles_list, ghost_rect)
        elif level % 4 == 0:
            load(number_mutants, mutant, obstacles_list, mutant_rect)
        elif level % 3 == 0:
            load(number_fasts, fast, obstacles_list, fast_rect)
        else:
            load(number_devils, devil, obstacles_list, devil_rect)

    if background == background4:
        if boss_hp == 40:
            load(10, devil,enemy_list,devil_rect)
            load(5, mutant,enemy_list,mutant_rect)
        if boss_hp == 30:
            load(6, mutant,enemy_list,mutant_rect)
            load(7, ghost,enemy_list,ghost_rect)
            load(5, devil,enemy_list,devil_rect)
        if boss_hp == 20:
            load(10, fast,enemy_list,fast_rect)
            load(10, mutant,enemy_list,mutant_rect)
        if boss_hp == 10:
            load(40, devil,enemy_list,devil_rect)

    return enemy_list


enemy_list = enemies()


class Bullet:
    def __init__(self, x, y, speed, bullet_width, bullet_height, direction, texture):
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = direction
        self.texture = texture
        self.bullet_height = bullet_height
        self.bullet_width = bullet_width
        self.rect = pygame.Rect(x, y, bullet_width, bullet_height)

    def update(self):
        if self.direction == 'left':
            self.rect.move_ip(-self.speed, 0)
        elif self.direction == 'right':
            self.rect.move_ip(self.speed, 0)
        elif self.direction == 'top':
            self.rect.move_ip(0, -self.speed)
        elif self.direction == 'down':
            self.rect.move_ip(0, self.speed)

    def draw(self, window):
        window.blit(self.texture, (self.rect.x, self.rect.y))

    def delete(self):
        bullets_list.remove(self)
        del self


def points():
    gold_list = []

    goldWidth = 20
    goldHeight = 20
    gold_texture = pygame.transform.scale(
        pygame.image.load('textures/gold.png'), (goldWidth, goldHeight))
    gold_rect = gold_texture.get_rect()

    def gold(xgold, ygold):
        global points_counter
        global number_devils
        global number_fasts
        global number_mutants
        global number_obstacles
        global number_ghosts
        global level
        global bullet_fired
        gold = Obstacle(xgold, ygold, goldWidth,
                        goldHeight, gold_texture)
        gold_list.append(gold)
        if level != 0:
            next_level_sound.play()
        dead_enemy_list.clear()
        destroyed_obstacles_list.clear()
        level += 1
        if number_obstacles <= max_obstacles:
            number_obstacles += 1
        if level % 2 == 0:
            number_devils += 1
        if level % 3 == 0:
            number_fasts += 1
        if level % 4 == 0:
            number_mutants += 1
        if level % 5 == 0:
            number_ghosts += 1

    if background!=background4:
        gold = load(1, gold, obstacles_list, gold_rect)
    return gold_list


gold_list = points()


def generate_new_obstacles():
    global obstacles_list
    obstacles_list.clear()
    dead_boss_list.clear()
    obstacles_list = obstacles()


def generate_new_gold():
    global gold_list
    gold_list.clear()
    gold_list = points()
    play_sound(next_level_sound)


def generate_new_enemy():
    global enemy_list
    enemy_list = enemies()


def death_animation(death_frames, x, y):
    for i in death_frames:
        window.blit(i, (x, y))
        pygame.time.wait(50)
        pygame.display.update()


def corpses():
    for enemy in dead_enemy_list:
        if enemy.type == 'fast':
            if enemy.killed_by == 'bullet':
                window.blit(fast_corpses,
                            (enemy.rect.x-20, enemy.rect.y-20))
            elif enemy.killed_by == 'shield':
                window.blit(fast_corpses,
                            (enemy.rect.x-20, enemy.rect.y-20))
        if enemy.type == 'devil':
            if enemy.killed_by == 'bullet':
                window.blit(devil_bullet_corpses, (enemy.rect.x, enemy.rect.y))
            elif enemy.killed_by == 'shield':
                window.blit(devil_corpses, (enemy.rect.x, enemy.rect.y))
        if enemy.type == 'mutant':
            if enemy.killed_by == 'shield':
                window.blit(mutant_corpses_shield,
                            (enemy.rect.x, enemy.rect.y))
            elif enemy.killed_by == 'bullet':
                window.blit(mutant_corpses_bullet, (enemy.rect.x, enemy.rect.y))
        if enemy.type == 'ghost':
            window.blit(ghost_corpses, (enemy.rect.x, enemy.rect.y))


def status():
    global boss_hp
    font = pygame.font.Font('font/snap.ttf', 30)
    points_text = font.render(
        f'Gold: {points_counter}', True, (255, 0, 0))
    window.blit(points_text, (1750, 10))
    points_text = font.render(
        f'Level: {level}', True, (255, 0, 0))
    window.blit(points_text, (20, 10))
    points_text = font.render(
        f'Bullets: {magazine}', True, (255, 0, 0))
    window.blit(points_text, (850, 10))
    if background == background4:
        points_str = 'l' * boss_hp
        pointts_text = font.render(points_str, True, (255, 0, 0))
        window.blit(pointts_text, (700, 1000))


start()
pygame.mixer.music.load('sounds/music.mp3')
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)

run = True
while run:
    pygame.time.Clock().tick(60)
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if keys[pygame.K_ESCAPE]:
            run = False

    xx, yy = 0, 0

    if keys[pygame.K_d]:
        play_sound(steps_sound)
        xx += speed
        bullet_direction = 'right'
    elif keys[pygame.K_a]:
        play_sound(steps_sound)
        xx -= speed
        bullet_direction = 'left'
    elif keys[pygame.K_s]:
        play_sound(steps_sound)
        yy += speed
        bullet_direction = 'down'
    elif keys[pygame.K_w]:
        play_sound(steps_sound)
        yy -= speed
        bullet_direction = 'top'
    else:
        stop_sound(steps_sound)

    prev_pos = player1_rect.copy()
    player1_rect.move_ip(xx, yy)
    x, y = player1_rect.x, player1_rect.y

    for obstacle in obstacles_list:
        mask = obstacle.mask
        offset = (obstacle.rect.x - player1_rect.x,
                  obstacle.rect.y - player1_rect.y)
        if player1_mask.overlap(mask, offset):
            player1_rect = prev_pos
            x, y = player1_rect.x, player1_rect.y
            break

    if keys[pygame.K_o]:
        if o_key_released:
            if points_counter > 0:
                o_key_pressed = True
            o_key_released = False
        else:
            o_key_pressed = False
            o_key_released = True

    if keys[pygame.K_i]:
        if i_key_released:
            if points_counter >= 3:
                i_key_pressed = True
                shield()
                points_counter -= 3
                powershield = True
            i_key_released = False
        else:
            i_key_pressed = False
            i_key_released = True

    if keys[pygame.K_p]:
        if p_key_released:
            p_key_pressed = True
            if speed <= max_speed and points_counter >= 2:
                speed_boost()
                speed += 1
                points_counter -= 2
            elif speed == max_speed:
                speed_boost()
            p_key_released = False
        else:
            p_key_pressed = False
            p_key_released = True

    if keys[pygame.K_m]:
        if m_key_released:
            m_key_pressed = True
            m_key_released = False
        else:
            m_key_pressed = False
            m_key_released = True

    if keys[pygame.K_u]:
        if u_key_released:
            u_key_pressed = True
            u_key_released = False
        else:
            u_key_pressed = False
            u_key_released = True

    if keys[pygame.K_r]:
        if r_key_released:
            r_key_pressed = True
            r_key_released = False
        else:
            r_key_pressed = False
            r_key_released = True

    for i in borders_list:
        if player1_rect.colliderect(i):
            if i == borders_list[0]:
                y = i.rect.top + 5
            elif i == borders_list[1]:
                y = i.rect.bottom - 40
            elif i == borders_list[2]:
                x = i.rect.left + 5
            if right.color == (255, 0, 0):
                if i == borders_list[3]:
                    x = i.rect.right - 40

    for gold in gold_list:
        if player1_rect.colliderect(gold.rect):
            gold_sound.play()
            points_counter += 1
            right.color = (0, 255, 0)
            gold_list.remove(gold)
    if right.color == (0, 255, 0) and player1_rect.colliderect(right.rect):
        background = random_background()
        generate_new_obstacles()
        generate_new_gold()
        generate_new_enemy()
        bullet_fired = True
        right.color = (255, 0, 0)
        x = 0

    for i in obstacles_list:
        mask = i.mask
        offset = (i.rect.x - player1_rect.x, i.rect.y - player1_rect.y)
        if player1_mask.overlap(mask, offset):
            if offset[0] > 0:
                player1_rect.right = player1_rect.right - 40
            elif offset[0] < 0:
                player1_rect.left = player1_rect.left + 40
            elif offset[1] > 0:
                player1_rect.bottom = player1_rect.right - 40
            else:
                player1_rect.top = player1_rect.right + 40

    if o_key_pressed:
        refresh()
        generate_new_obstacles()
        generate_new_gold()
        points_counter -= 2
        level -= 1

    if m_key_pressed:
        pause()

    if u_key_pressed:
        if points_counter >= 2:
            magazine += 20
            points_counter -= 2
            reeload()
        else:
            u_key_pressed = False

    if r_key_pressed:
        if gun_on == False:
            gun1()
            gun_on = True
            speed -= 3
            r_key_pressed = False

        elif gun_on == True:
            gun2()
            gun_on = False
            speed += 3
            r_key_pressed = False

    window.blit(background, (0, 0))

    for gol in gold_list:
        gol.draw(window)

    for obj in obstacles_list:
        obj.draw(window)

    for border in borders_list:
        border.draw(window)

    for boss in dead_boss_list:
        window.blit(boss_corpses, (boss.rect.x, boss.rect.y))

    corpses()

    if background == background4:
        if bs == True:
            pygame.mixer.stop()
            pygame.mixer.music.load('sounds/bossfight.mp3')
            pygame.mixer.music.set_volume(0.7)
            pygame.mixer.music.play(-1)
            bs = False
        for boss in boss_list:
            mask = boss.mask
            offset = (boss.rect.x - player1_rect.x,
                      boss.rect.y - player1_rect.y)
            if abs(player1_rect.x - boss.rect.x) <= 200 and abs(player1_rect.y - boss.rect.y) <= 200:
                play_sound(boss_death_sound)
            boss.update()
            window.blit(boss.texture, boss.rect)
            if boss_hp == 0:
                stop_sound(boss_death_sound)
                boss_sound.play()
                boss.delete()
                death_animation(boss_dead_animation,
                                boss.rect.x, boss.rect.y)
                points_counter += 30
                right.color = (0, 255, 0)
                level += 1
                points_counter = 0
                number_devils = 0
                number_fasts = 0
                number_mutants = 0
                number_ghosts = 0
                pygame.mixer.music.stop()
                pygame.mixer.music.load('sounds/music.mp3')
                pygame.mixer.music.set_volume(0.4)
                pygame.mixer.music.play(-1)
                if right.color == (0, 255, 0) and player1_rect.colliderect(right.rect):
                    stop_sound(boss_sound)
                    boss_hp = 50
                    background = random_background()
                    generate_new_obstacles()
                    generate_new_gold()
                    generate_new_enemy()
                    bullet_fired = True
                    right.color = (255, 0, 0)
                    x = 0
            if player1_mask.overlap(mask, offset):
                player_death_sound.play()
                death_animation(player_dead_animation, x, y)
                time.sleep(1)
                deadscreen()
                generate_new_enemy()
                generate_new_gold()
                generate_new_obstacles()
                pygame.mixer.music.stop()
                pygame.mixer.music.load('sounds/music.mp3')
                pygame.mixer.music.set_volume(0.4)
                pygame.mixer.music.play(-1)
                break

    for obstacle in destroyed_obstacles_list:
        scaled_corpse = pygame.transform.scale(
            destroyed_obstacle_texture, (obstacle.rect.width, obstacle.rect.height))
        window.blit(scaled_corpse, (obstacle.rect.x, obstacle.rect.y))

    if powershield == False and gun_on == False:
        window.blit(player1_texture, player1_rect)
        player1_rect = pygame.rect.Rect(x, y, 40, 40)
    elif powershield == True and gun_on == False:
        window.blit(player1_texture_shield, player1_rect)
        player1_rect = pygame.rect.Rect(x, y, 40, 40)
    elif powershield == False and gun_on == True:
        if keys[pygame.K_d]:
            window.blit(player_plazma_right_texture, player1_rect)
            last_texture = player_plazma_right_texture
            player1_rect = pygame.rect.Rect(x, y, 40, 40)
        elif keys[pygame.K_a]:
            window.blit(player_plazma_left_texture, player1_rect)
            player1_rect = pygame.rect.Rect(x, y, 40, 40)
            last_texture = player_plazma_left_texture
        elif keys[pygame.K_s]:
            window.blit(player_plazma_down_texture, player1_rect)
            player1_rect = pygame.rect.Rect(x, y, 40, 40)
            last_texture = player_plazma_down_texture
        elif keys[pygame.K_w]:
            window.blit(player_plazma_top_texture, player1_rect)
            player1_rect = pygame.rect.Rect(x, y, 40, 40)
            last_texture = player_plazma_top_texture
        else:
            window.blit(last_texture, player1_rect)
            player1_rect = pygame.rect.Rect(x, y, 40, 40)
    elif powershield == True and gun_on == True:
        if keys[pygame.K_d]:
            window.blit(player_plazma_right_shield_texture, player1_rect)
            player1_rect = pygame.rect.Rect(x, y, 40, 40)
            last_texture_with_shield = player_plazma_right_shield_texture
        elif keys[pygame.K_a]:
            window.blit(player_plazma_left_shield_texture, player1_rect)
            player1_rect = pygame.rect.Rect(x, y, 40, 40)
            last_texture_with_shield = player_plazma_left_shield_texture
        elif keys[pygame.K_s]:
            window.blit(player_plazma_down_shield_texture, player1_rect)
            player1_rect = pygame.rect.Rect(x, y, 40, 40)
            last_texture_with_shield = player_plazma_down_shield_texture
        elif keys[pygame.K_w]:
            window.blit(player_plazma_top_shield_texture, player1_rect)
            player1_rect = pygame.rect.Rect(x, y, 40, 40)
            last_texture_with_shield = player_plazma_top_shield_texture
        else:
            window.blit(last_texture_with_shield, player1_rect)
            player1_rect = pygame.rect.Rect(x, y, 40, 40)
    status()

    if keys[pygame.K_SPACE] and bullet_fired == True and magazine > 0 and gun_on == True:
        if bullet_direction == 'right':
            new_bullet = Bullet(player1_rect.x, player1_rect.y, bullet_speed, bullet_width, bullet_height,
                                bullet_direction, bullet_texture_right)
            bullets_list.append(new_bullet)
            magazine -= 1
            gun_sound.play()
        elif bullet_direction == 'left':
            new_bullet = Bullet(player1_rect.x, player1_rect.y, bullet_speed, bullet_width, bullet_height,
                                bullet_direction, bullet_textureL)
            bullets_list.append(new_bullet)
            magazine -= 1
            gun_sound.play()
        elif bullet_direction == 'top':
            new_bullet = Bullet(player1_rect.x, player1_rect.y, bullet_speed, bullet2_width, bullet2_height,
                                bullet_direction, bullet_textureT)
            bullets_list.append(new_bullet)
            magazine -= 1
            gun_sound.play()
        elif bullet_direction == 'down':
            new_bullet = Bullet(player1_rect.x, player1_rect.y, bullet_speed, bullet2_width, bullet2_height,
                                bullet_direction, bullet_textureD)
            bullets_list.append(new_bullet)
            magazine -= 1
            gun_sound.play()

    for enemy in enemy_list:
        enemy.update(obstacles_list)
        if enemy.type == 'mutant':
            enemy.mirror(mutant_texture_left_direction, mutant_texture_right_direction)
        elif enemy.type == 'ghost':
            enemy.mirror(ghost_texture_left_direction, ghost_texture_right_direction)
        window.blit(enemy.texture, enemy.rect)

        if abs(player1_rect.x - enemy.rect.x) <= 200 and abs(player1_rect.y - enemy.rect.y) <= 200:
            random_monster_sound = random.choice(monsters_sounds)
            play_sound(random_monster_sound)

        if enemy.rect.colliderect(player1_rect):
            if powershield == False:
                player_death_sound.play()
                death_animation(player_dead_animation, x, y)
                time.sleep(1)
                deadscreen()
                generate_new_enemy()
                generate_new_gold()
                generate_new_obstacles()
                pygame.mixer.music.stop()
                pygame.mixer.music.load('sounds/music.mp3')
                pygame.mixer.music.set_volume(0.4)
                pygame.mixer.music.play(-1)
                break
            elif powershield == True:
                enemy.killed_by = 'shield'
                if enemy.type == 'fast':
                    fast_death_sound.play()
                    death_animation(fast_dead_animation,
                                    enemy.rect.x, enemy.rect.y)
                elif enemy.type == 'devil':
                    devil_death_sound.play()
                    death_animation(devil_dead_animation,
                                    enemy.rect.x, enemy.rect.y)
                elif enemy.type == 'mutant':
                    mutant_death_sound.play()
                    death_animation(mutant_bullet_dead_animation,
                                    enemy.rect.x, enemy.rect.y)
                elif enemy.type == 'ghost':
                    ghost_death_sound.play()
                    death_animation(ghost_dead_animation,
                                    enemy.rect.x, enemy.rect.y)
                enemy.delete()
                powershield = False

    for bullet in bullets_list:
        try:
            bullet.update()
            bullet_fired = False
            if bullet.rect.left > 2000 or bullet.rect.right < 0 or bullet.rect.top > 1200 or bullet.rect.bottom < 0:
                bullet.delete()
                bullet_fired = True
            for boss in boss_list:
                if bullet.rect.colliderect(boss.rect):
                    bullet.delete()
                    boss_hp -= 1
                    bullet_fired = True
            for obstacle in obstacles_list:
                if bullet.rect.colliderect(obstacle.rect):
                    destruction_sound.play()
                    death_animation(bullet_boom_list,
                                    bullet.rect.x, bullet.rect.y)
                    death_animation(obstacle_destroy_animation,
                                    obstacle.rect.x, obstacle.rect.y)
                    bullet.delete()
                    obstacle.delete()
                    bullet_fired = True
                    break
            for enemy in enemy_list:
                if bullet.rect.colliderect(enemy.rect):
                    enemy.killed_by = 'bullet'
                    if enemy.type == 'fast':
                        fast_death_sound.play()
                        number_fasts -= 1
                        death_animation(fast_bullet_dead_animation,
                                        enemy.rect.x, enemy.rect.y)
                    elif enemy.type == 'devil':
                        devil_death_sound.play()
                        death_animation(devil_bullet_dead_animation,
                                        enemy.rect.x, enemy.rect.y)
                        number_devils -= 1
                    elif enemy.type == 'mutant':
                        mutant_death_sound.play()
                        death_animation(mutant_shield_dead_animation,
                                        enemy.rect.x, enemy.rect.y)
                        number_mutants -= 1
                    elif enemy.type == 'ghost':
                        ghost_death_sound.play()
                        death_animation(ghost_dead_animation,
                                        enemy.rect.x, enemy.rect.y)
                        number_ghosts -= 1
                    enemy.delete()
                    bullet.delete()
                    bullet_fired = True
            bullet.draw(window)
        except:
            pass

    if boss_hp == 40:
        generate_new_enemy()
        boss_hp = 39
        for enemy in enemy_list:
            death_animation(devil_dead_animation, enemy.rect.x, enemy.rect.y)
    if boss_hp == 30:
        generate_new_enemy()
        boss_hp = 29
        for enemy in enemy_list:
            death_animation(devil_dead_animation, enemy.rect.x, enemy.rect.y)
    if boss_hp == 20:
        generate_new_enemy()
        boss_hp = 19
        for enemy in enemy_list:
            death_animation(devil_dead_animation, enemy.rect.x, enemy.rect.y)
    if boss_hp == 10:
        generate_new_enemy()
        boss_hp = 9
        for enemy in enemy_list:
            death_animation(devil_dead_animation, enemy.rect.x, enemy.rect.y)

    pygame.display.update()
