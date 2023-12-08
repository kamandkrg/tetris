import pygame
import random
from shapes import shapes
pygame.init()
win = pygame.display.set_mode((500, 800))
pygame.display.set_caption('snake')
run = True

# img = pygame. image. load('background.png')
# img. convert()
# rect = img. get_rect()
# rect. center = 500//2, 800//2
x_location_adding = 0
y_location_adding = 0
a = 0
b = 0
k = 0
all_locations = []
random_shape = random.choice(shapes)

def barkhord_chap(all_locations):
    for locations in all_locations:
        if locations[0] <= 0:
            return True
def barkhord_rast(all_locations):
    for locations in all_locations:
        if locations[0] >= 480:
            return True
def barkhord_paiin(all_locations):
    for locations in all_locations:
        if locations[1] >= 780:
            return True
while run:
    pygame.time.delay(150)
    event = pygame.event.get()
    for even in event:
        if even.type == pygame.QUIT:
            run = False
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        x_location_adding -=20
        if barkhord_chap(all_locations):
            x_location_adding +=20
    elif key[pygame.K_RIGHT]:
        x_location_adding +=20
        if barkhord_rast(all_locations):
            x_location_adding -=20
    elif key[pygame.K_DOWN]:
        y_location_adding += 20
        if barkhord_paiin(all_locations):
            y_location_adding -=20
    elif key[pygame.K_UP]:
        a+=1
        b = a % len(random_shape)
    all_locations.clear()        
    win.fill((0,0,0))
    # win. blit(img, rect)
    y_location = 0
    for i in random_shape[b]:
        y_location+=20
        x_location = 200
        for j in i:
            if j == 1:
                pygame.draw.rect(win, (255, 255, 255), (x_location + x_location_adding, y_location+ y_location_adding, 20, 20))
                all_locations.append([x_location + x_location_adding, y_location+ y_location_adding])
            x_location+=20
    # print(all_locations[k])
    
    # y_location_adding += 20
    # if barkhord(k, all_locations):
    #     print('barkhord')
    
    pygame.display.update()
    





