import pygame
import random
import time

pygame.init()
widthWindow = 1920
heightWindow = 1080
window = pygame.display.set_mode((widthWindow, heightWindow))
points_counter = -1
level = 0
number_devils = 0
number_fasts = 0
number_mutants = 0
number_ghosts = 0
number_obstacles = 15
font = pygame.font.Font(None, 36)
x = 100
y = 100
p_key_pressed = False
p_key_released = True
o_key_pressed = False
o_key_released = True
speed = 8
max_speed = 15

background = pygame.image.load('textures/tlo.jpg')
background = pygame.transform.scale(background, window.get_size())

player1_texture = pygame.transform.scale(
    pygame.image.load('textures/player.png'), (40, 40))
player1_rect = player1_texture.get_rect()
player1_rect.x = x
player1_rect.y = y

treeWidth = 70
treeHeight = 100
tree_texture = pygame.transform.scale(
    pygame.image.load('textures/drzewo.png'), (treeWidth, treeHeight))
tree_rect = tree_texture.get_rect()

stoneWidth = 50
stoneHeight = 50
stone_texture = pygame.transform.scale(
    pygame.image.load('textures/kamien.png'), (stoneWidth, stoneHeight))
stone_rect = stone_texture.get_rect()

goldWidth = 20
goldHeight = 20
gold_texture = pygame.transform.scale(
    pygame.image.load('textures/gold.png'), (goldWidth, goldHeight))
gold_rect = gold_texture.get_rect()


bushWidth = 40
bushHeight = 40
bush_texture = pygame.transform.scale(
    pygame.image.load('textures/krzak.png'), (bushWidth, bushHeight))
bush_rect = bush_texture.get_rect()

devilWidth = 50
devilHeight = 50
devilSpeed = 5
devilCollision = 50
devil_texture = pygame.transform.scale(
    pygame.image.load('textures/enemy.png'), (devilWidth, devilHeight))
devil_rect = devil_texture.get_rect()

fastWidth = 40
fastHeight = 40
fastSpeed = 15
fastCollision = 40
fast_texture = pygame.transform.scale(
    pygame.image.load('textures/fast.png'), (fastWidth, fastHeight))
fast_rect = fast_texture.get_rect()

mutantWidth = 100
mutantHeight = 100
mutantSpeed = 2
mutantCollision = 100
mutant_texture = pygame.transform.scale(
    pygame.image.load('textures/mutant.png'), (mutantWidth, mutantHeight))
mutant_rect = mutant_texture.get_rect()

ghostWidth = 50
ghostHeight = 50
ghostSpeed = 10
ghostCollision = 50
ghost_texture = pygame.transform.scale(
    pygame.image.load('textures/ghost.png'), (ghostWidth, ghostHeight))
ghost_rect = ghost_texture.get_rect()


def start():
    start_width, start_height = 1920, 1080
    start_surface = pygame.Surface((start_width, start_height))
    start_surface.fill((123, 203, 237))
    tekst = pygame.font.Font(None, 50)
    tekst_lines = ["Welcome in Coin Game",
                   "Move: W,A,S,D", "Buy refresh: O", "Buy speed boost: P", "End: ESCAPE", "press space to continue"]
    tekst_color = 0, 0, 0
    tekst_height = 0
    for i in tekst_lines:
        tekst_surface = tekst.render(i, True, tekst_color)
        tekst_x = 700
        tekst_y = 390 + tekst_height
        start_surface.blit(tekst_surface, (tekst_x, tekst_y))
        tekst_height += tekst_surface.get_height() + 40

    start_x = 1
    start_y = 1
    window.blit(start_surface, (start_x, start_y))
    pygame.display.update()
    waiting = True
    while waiting:
        for i in pygame.event.get():
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                waiting = False


def end():
    end_width, end_height = 960, 540
    end_surface = pygame.Surface((end_width, end_height))
    end_texture = pygame.transform.scale(pygame.image.load(
        "textures/end.png"), (end_width, end_height))
    end_texture_rect = end_texture.get_rect()
    end_surface.blit(end_texture, end_texture_rect)
    end_x = (widthWindow) / 4
    end_y = (heightWindow) / 4
    window.blit(end_surface, (end_x, end_y))
    pygame.display.update()


def speed_boost():
    speed_width, speed_height = 200, 100
    speed_surface = pygame.Surface((speed_width, speed_height))
    speed_surface.fill((123, 203, 237))
    tekst_font = pygame.font.Font(None, 24)
    if speed < 15:
        tekst_surface = tekst_font.render("You use TURBO", True, (0, 0, 0))
    else:
        tekst_surface = tekst_font.render(
            "You have MAX speed", True, (0, 0, 0))
    tekst_x = (speed_width - tekst_surface.get_width()) / 2
    tekst_y = (speed_height - tekst_surface.get_height()) / 2
    speed_surface.blit(tekst_surface, (tekst_x, tekst_y))
    speed_x = (widthWindow - speed_width) / 2
    speed_y = (heightWindow - speed_height) / 2
    window.blit(speed_surface, (speed_x, speed_y))
    pygame.display.update()
    time.sleep(1)


def refresh():
    refresh_width, refresh_height = 200, 100
    refresh_surface = pygame.Surface((refresh_width, refresh_height))
    refresh_surface.fill((123, 203, 237))
    tekst_font = pygame.font.Font(None, 24)
    tekst_surface = tekst_font.render("You use Refresh", True, (0, 0, 0))
    tekst_x = (refresh_width - tekst_surface.get_width()) / 2
    tekst_y = (refresh_height - tekst_surface.get_height()) / 2
    refresh_surface.blit(tekst_surface, (tekst_x, tekst_y))
    refresh_x = (widthWindow - refresh_width) / 2
    refresh_y = (heightWindow - refresh_height) / 2
    window.blit(refresh_surface, (refresh_x, refresh_y))
    pygame.display.update()
    time.sleep(1)


def load(quantity, objectt, lista, rect):
    for i in range(quantity):
        x = random.randint(0, widthWindow)
        y = random.randint(0, heightWindow)
        collision = True
        while collision:
            collision = False
            for o in lista:
                if rect.move(x, y).colliderect(o.rect):
                    collision = True
                    x = random.randint(0, widthWindow)
                    y = random.randint(0, heightWindow)
                    break
        objectt(x, y)


class Border:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 255, 255), self.rect)


def borders():
    borders_list = []

    up = Border(1, 1, 1920, 1)
    borders_list.append(up)

    down = Border(1, 1079, 1920, 1)
    borders_list.append(down)

    left = Border(1, 1, 1, 1080)
    borders_list.append(left)

    right = Border(1919, 1, 1, 1080)
    borders_list.append(right)

    return borders_list


borders_list = borders()


class Obstacle:
    def __init__(self, x, y, width, height, texture):
        self.rect = pygame.Rect(x, y, width, height)
        self.texture = texture

    def draw(self, surface):
        surface.blit(self.texture, self.rect)


def obstacles():
    obstacles_list = []

    def tree(xtree, ytree):
        tree = Obstacle(xtree, ytree, treeWidth,
                        treeHeight, tree_texture)
        obstacles_list.append(tree)

    def stone(xstone, ystone):
        stone = Obstacle(xstone, ystone, stoneWidth,
                         stoneHeight, stone_texture)
        obstacles_list.append(stone)

    def bush(xbush, ybush):
        bush = Obstacle(xbush, ybush, bushWidth,
                        bushHeight, bush_texture)
        obstacles_list.append(bush)

    load(number_obstacles, tree, obstacles_list, tree_rect)
    load(number_obstacles, stone, obstacles_list, stone_rect)
    load(number_obstacles, bush, obstacles_list, bush_rect)

    return obstacles_list


obstacles_list = obstacles()


class Enemy:
    def __init__(self, x, y, width, height, texture, speed, collison, enemy_type):
        self.rect = pygame.Rect(x, y, width, height)
        self.texture = texture
        self.speed = speed
        self.collison = collison
        self.direction = (1, 0)
        self.type = enemy_type

    def update(self, obstacles_list):
        self.rect.x += self.speed * self.direction[0]
        self.rect.y += self.speed * self.direction[1]

        # Sprawdź, czy przeciwnik koliduje z przeszkodami
        for i in obstacles_list:
            if self.type == 'ghost':
                continue
            if self.rect.colliderect(i.rect):
                if self.rect.x < i.rect.left:
                    self.rect.x = i.rect.left - self.collison
                elif self.rect.x > i.rect.right:
                    self.rect.x = i.rect.right
                elif self.rect.y < i.rect.top:
                    self.rect.y = i.rect.top - self.collison
                else:
                    self.rect.y = i.rect.bottom

        for i in borders_list:
            if self.rect.colliderect(i):
                if i == borders_list[0]:
                    self.rect.y = + 5
                elif i == borders_list[1]:
                    self.rect.y = - 55
                elif i == borders_list[2]:
                    self.rect.x = + 5
                elif i == borders_list[3]:
                    self.rect.x = - 55

        if self.rect.colliderect(player1_rect):
            end()
            time.sleep(2)
            quit()

        if random.random() < 0.05:
            self.change_direction()

    def change_direction(self):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        new_direction = self.direction
        while new_direction == self.direction:
            new_direction = random.choice(directions)
        self.direction = new_direction


def enemies():
    enemy_list = []

    def devil(xdevil, ydevil):
        devil = Enemy(xdevil, ydevil, devilWidth,
                      devilHeight, devil_texture, devilSpeed, devilCollision, 'devil')
        enemy_list.append(devil)

    def fast(xfast, yfast):
        fast = Enemy(xfast, yfast, fastWidth,
                     fastHeight, fast_texture, fastSpeed, fastCollision, 'fast')
        enemy_list.append(fast)

    def mutant(xmutant, ymutant):
        mutant = Enemy(xmutant, ymutant, mutantWidth,
                       mutantHeight, mutant_texture, mutantSpeed, mutantCollision, 'mutant')
        enemy_list.append(mutant)

    def ghost(xghost, yghost):
        ghost = Enemy(xghost, yghost, ghostWidth,
                      ghostHeight, ghost_texture, ghostSpeed, ghostCollision, 'ghost')
        enemy_list.append(ghost)

    if level % 5 == 0:
        load(number_ghosts, ghost, obstacles_list, ghost_rect)
    elif level % 4 == 0:
        load(number_mutants, mutant, obstacles_list, mutant_rect)
    elif level % 3 == 0:
        load(number_fasts, fast, obstacles_list, fast_rect)
    else:
        load(number_devils, devil, obstacles_list, devil_rect)

    return enemy_list


enemy_list = enemies()


def points():
    gold_list = []

    def gold(xgold, ygold):
        global points_counter
        global number_devils
        global number_fasts
        global number_mutants
        global number_obstacles
        global number_ghosts
        global level
        gold = Obstacle(xgold, ygold, goldWidth,
                        goldHeight, gold_texture)
        gold_list.append(gold)
        points_counter += 1
        number_obstacles += 1
        level += 1
        if level % 2 == 0:
            number_devils += 1
        if level % 3 == 0:
            number_fasts += 1
        if level % 4 == 0:
            number_mutants += 1
        if level % 5 == 0:
            number_ghosts += 1

    gold = load(1, gold, obstacles_list, gold_rect)
    return gold_list


gold_list = points()


def generate_new_obstacles():
    global obstacles_list
    obstacles_list.clear()
    obstacles_list = obstacles()


def generate_new_gold():
    global gold_list
    gold_list.clear()
    gold_list = points()


def generate_new_enemy():
    global enemy_list
    enemy_list = enemies()


start()

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
        xx += speed
    if keys[pygame.K_a]:
        xx -= speed
    if keys[pygame.K_s]:
        yy += speed
    if keys[pygame.K_w]:
        yy -= speed

    if keys[pygame.K_o]:
        if o_key_released:
            if points_counter > 0:
                o_key_pressed = True
                refresh()
            o_key_released = False
        else:
            o_key_pressed = False
            o_key_released = True

    if keys[pygame.K_p]:
        if p_key_released:
            p_key_pressed = True
            if speed <= max_speed and points_counter > 0:
                speed_boost()
                speed += 1
                points_counter -= 1
            elif speed == max_speed:
                speed_boost()
            p_key_released = False
        else:
            p_key_pressed = False
            p_key_released = True

    old_x, old_y = x, y
    x += xx
    y += yy

    for i in borders_list:
        if player1_rect.colliderect(i):
            if i == borders_list[0]:
                y = i.rect.top + 5
            elif i == borders_list[1]:
                y = i.rect.bottom - 45
            elif i == borders_list[2]:
                x = i.rect.left + 5
            elif i == borders_list[3]:
                x = i.rect.right - 45

    for i in gold_list:
        if player1_rect.colliderect(i.rect):
            generate_new_obstacles()
            generate_new_gold()
            generate_new_enemy()
        else:
            for i in obstacles_list:
                if player1_rect.colliderect(i.rect):
                    if x < i.rect.left:
                        x = i.rect.left - 40
                    elif x > i.rect.right:
                        x = i.rect.right
                    elif y < i.rect.top:
                        y = i.rect.top - 40
                    else:
                        y = i.rect.bottom

    if o_key_pressed:
        generate_new_obstacles()
        generate_new_gold()
        points_counter -= 2

    window.blit(background, (0, 0))

    for gol in gold_list:
        gol.draw(window)

    for obj in obstacles_list:
        obj.draw(window)

    for border in borders_list:
        border.draw(window)

    window.blit(player1_texture, player1_rect)
    player1_rect = pygame.rect.Rect(x, y, 40, 40)

    for enemy in enemy_list:
        enemy.update(obstacles_list)
        window.blit(enemy.texture, enemy.rect)

    points_text = font.render(
        f'Coins: {points_counter}', True, (255, 255, 255))
    window.blit(points_text, (1810, 10))
    points_text = font.render(
        f'Level: {level}', True, (255, 255, 255))
    window.blit(points_text, (10, 10))

    pygame.display.update()
