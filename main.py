import pygame
import random
from shapes import SHAPES
pygame.init()
win = pygame.display.set_mode((500, 800))
pygame.display.set_caption('tetris')
colors = [(255,0,0),(0,255,0),(255,255,0),(255,0,255),(0,255,255), (150,0,0), (0,0,255), (193,195,194), (255,255,255)]
# img = pygame. image. load('background.png')
# img. convert()
# rect = img. get_rect()
# rect. center = 500//2, 800//2
x_location_adding = 0
y_location_adding = 0
a = 4
locations = []
all_locations = []
random_color = (random.choice(colors))
random_shape = random.choice(list(SHAPES.values()))
shape = list(random_shape)
random_colors = [[random_color, len(shape)]]
run = True

def barkhord_chap(locations):
    for location in locations:
        if location[0] <= -40:
            return True
    for i in all_locations:
        for j in locations:
            if i[0] + 20 == j[0] and i[1] == j[1]:
                return True
def barkhord_rast(locations):
    for location in locations:
        if location[0] >= 440:
            return True
    for i in all_locations:
        for j in locations:
            if i[0] - 20 == j[0] and i[1] == j[1]:
                return True
def barkhord_paiin(locations, all_locations):
    for location in locations:
        if location[1] >= 780:
            return True
    for i in all_locations:
        for j in locations:
            if i[0] == j[0] and i[1]-20 == j[1]:
                return True
def barkhord_payin(locations):
    for location in locations:
        if location[1] >= 760:
            return True
    for i in all_locations:
        for j in locations:
            if i[0] == j[0] and i[1]-40 == j[1]:
                return True
def radif_kamel(all_locations):
    for i in range(780, 60, -20):

        pass
while run:
    pygame.time.delay(150)
    event = pygame.event.get()
    for even in event:
        if even.type == pygame.QUIT:
            run = False
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        x_location_adding -=20
        if barkhord_chap(locations):
            x_location_adding +=20
    elif key[pygame.K_RIGHT]:
        x_location_adding +=20
        if barkhord_rast(locations):
            x_location_adding -=20
    elif key[pygame.K_DOWN]:
        y_location_adding += 20
        if barkhord_payin(locations):
            y_location_adding -=20
    elif key[pygame.K_UP]:
        a += 1 
        shape.clear()
        if a % 4 == 0:
            shape = list(random_shape)
        elif a % 4 == 1:
            for i in random_shape:
                shape.append([-i[1],i[0]])
        elif a % 4 == 2:
            for i in random_shape:
                shape.append([-i[0],-i[1]])
        elif a % 4 == 3:
            for i in random_shape:
                shape.append([i[1],-i[0]])
    locations.clear()
    win.fill((0,0,0))
    k = 0
    c = random_colors[0][1]
    for i in range(len(all_locations)):
        pygame.draw.rect(win, random_colors[k][0], (all_locations[i][0]+40, all_locations[i][1], 20, 20))
        if i == c-1:
            c = 0   
            k+=1    
            for i in range(k+1):
                c += random_colors[i][1]
    for i in shape:
        pygame.draw.rect(win, random_color, (i[0] * 20 + 240 + x_location_adding, i[1] * 20 + 20+ y_location_adding, 20, 20))
        locations.append([i[0] * 20 + 200 + x_location_adding, i[1] * 20 + 20+ y_location_adding])
    for i in range(40):
        for j in range(25):
            pygame.draw.rect(win, (0, 100, 200), (j*20, i*20, 20, 20),1)

    if barkhord_paiin(locations,all_locations):
        random_color = random.choice(colors)
        random_shape = list(random.choice(list(SHAPES.values())))
        shape = list(random_shape)
        random_colors.append([random_color, len(shape)])
        x_location_adding , y_location_adding = 0,0
        a = 4
        for i in locations:
            all_locations.append(i)
    else:
        y_location_adding += 20
    
    pygame.display.update()