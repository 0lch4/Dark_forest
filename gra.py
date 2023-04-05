import pygame
import random
import time

# tworzenie wyswietlacza
pygame.init()
widthWindow = 1920
heightWindow = 1080
window = pygame.display.set_mode((widthWindow, heightWindow))
points_counter = -1
number_of_enemies = 1
font = pygame.font.Font(None, 36)
x = 100
y = 100
o_key_pressed = False
o_key_released = True

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

enemyWidth = 50
enemyHeight = 50
enemy_texture = pygame.transform.scale(
    pygame.image.load('textures/enemy.png'), (enemyWidth, enemyHeight))
enemy_rect = enemy_texture.get_rect()


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


def load(quantity, object, lista, rect):
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
        object(x, y)


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

    load(50, tree, obstacles_list, tree_rect)
    load(50, stone, obstacles_list, stone_rect)

    return obstacles_list


obstacles_list = obstacles()


class Enemy:
    def __init__(self, x, y, width, height, texture):
        self.rect = pygame.Rect(x, y, width, height)
        self.texture = texture
        self.speed = 5
        self.direction = (1, 0)

    def update(self, obstacles_list):
        self.rect.x += self.speed * self.direction[0]
        self.rect.y += self.speed * self.direction[1]

        # Sprawdź, czy przeciwnik koliduje z przeszkodami
        for i in obstacles_list:
            if self.rect.colliderect(i.rect):
                if self.rect.x < i.rect.left:
                    self.rect.x = i.rect.left - 50
                elif self.rect.x > i.rect.right:
                    self.rect.x = i.rect.right
                elif self.rect.y < i.rect.top:
                    self.rect.y = i.rect.top - 50
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

    def enemy(xenemy, yenemy):
        enemy = Enemy(xenemy, yenemy, enemyWidth,
                      enemyHeight, enemy_texture)
        enemy_list.append(enemy)

    load(number_of_enemies, enemy, obstacles_list, enemy_rect)

    return enemy_list


enemy_list = enemies()


def points():
    gold_list = []

    def gold(xgold, ygold):
        global points_counter
        global number_of_enemies
        gold = Obstacle(xgold, ygold, goldWidth,
                        goldHeight, gold_texture)
        gold_list.append(gold)
        points_counter += 1

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


run = True
while run:
    pygame.time.Clock().tick(60)
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if keys[pygame.K_ESCAPE]:
            run = False

    speed = 10
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
            o_key_pressed = True
            time.sleep(1)
            o_key_released = False
        else:
            o_key_pressed = False
            o_key_released = True

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

    window.blit(background, (0, 0))

    for gol in gold_list:
        gol.draw(window)

    for obj in obstacles_list:
        obj.draw(window)

    for obj in borders_list:
        obj.draw(window)

    window.blit(player1_texture, player1_rect)
    player1_rect = pygame.rect.Rect(x, y, 40, 40)

    for enemy in enemy_list:
        enemy.update(obstacles_list)
        window.blit(enemy.texture, enemy.rect)

    points_text = font.render(
        f'Punkty: {points_counter}', True, (255, 255, 255))
    window.blit(points_text, (10, 10))

    pygame.display.update()
