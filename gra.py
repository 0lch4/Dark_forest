import pygame
import random
import time

# tworzenie wyswietlacza
pygame.init()
widthWindow = 1920
heightWindow = 1080
window = pygame.display.set_mode((widthWindow, heightWindow))
points_counter = -1
font = pygame.font.Font(None, 36)

x = 100
y = 100
o_key_pressed = False
o_key_released = True

background = pygame.image.load('textures/tlo.jpg')
background = pygame.transform.scale(background, window.get_size())

player1_texture = pygame.transform.scale(
    pygame.image.load('textures/player.png'), (50, 50))
player1_rect = player1_texture.get_rect()
player1_rect.x = x
player1_rect.y = y

treeWidth = 70
treeHeight = 100
tree_texture = pygame.transform.scale(
    pygame.image.load('textures/drzewo.png'), (treeWidth, treeHeight))
tree_rect = tree_texture.get_rect

stoneWidth = 50
stoneHeight = 50
stone_texture = pygame.transform.scale(
    pygame.image.load('textures/kamien.png'), (stoneWidth, stoneHeight))
stone_rect = stone_texture.get_rect

goldWidth = 20
goldHeight = 20
gold_texture = pygame.transform.scale(
    pygame.image.load('textures/gold.png'), (goldWidth, goldHeight))
gold_rect = gold_texture.get_rect


class Board:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, surface):
        surface.blit(self.rect)


def boards():
    boards_list = []

    def down():
        down = Board(1, 1, 1920, 1)
        boards_list.append(down)

    def up():
        up = Board(1, 1080, 1920, 1)
        boards_list.append(up)

    def left():
        left = Board(1, 1, 1, 1080)
        boards_list.append(left)

    def right():
        right = Board(1920, 1, 1, 1080)
        boards_list.append(right)

    return boards_list


board_list = boards()


class Obstacle:
    def __init__(self, x, y, width, height, texture):
        self.rect = pygame.Rect(x, y, width, height)
        self.texture = texture

    def draw(self, surface):
        surface.blit(self.texture, self.rect)


def load(quantity, object):
    for i in range(quantity):
        x = random.randint(0, widthWindow)
        y = random.randint(0, heightWindow)
        object(x, y)


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

    tree = load(50, tree)

    stone = load(50,  stone)

    return obstacles_list


obstacles_list = obstacles()


def points():
    gold_list = []

    def gold(xgold, ygold):
        global points_counter
        gold = Obstacle(xgold, ygold, goldWidth,
                        goldHeight, gold_texture)
        gold_list.append(gold)
        points_counter += 1

    gold = load(1, gold)

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

    speed = 15
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

    for i in gold_list:
        if player1_rect.colliderect(i.rect):
            generate_new_obstacles()
            generate_new_gold()
        else:
            for i in obstacles_list:
                if player1_rect.colliderect(i.rect):
                    if x < i.rect.left:
                        x = i.rect.left - 50
                    elif x > i.rect.right:
                        x = i.rect.right
                    elif y < i.rect.top:
                        y = i.rect.top - 50
                    else:
                        y = i.rect.bottom

    if o_key_pressed:
        generate_new_obstacles()

    window.blit(background, (0, 0))

    for gol in gold_list:
        gol.draw(window)

    for obj in obstacles_list:
        obj.draw(window)

    for obj in board_list:
        obj.draw(window)

    window.blit(player1_texture, player1_rect)
    player1_rect = pygame.rect.Rect(x, y, 50, 50)

    points_text = font.render(
        f'Punkty: {points_counter}', True, (255, 255, 255))
    window.blit(points_text, (10, 10))

    pygame.display.update()
