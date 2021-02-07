import pygame
import random
import math
from sort import SelectionSort
from Bar import Bar


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

size = (512, 512)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Sorting")

random_list = [i for i in range(512)]
random.shuffle(random_list)
all_sprites_list = pygame.sprite.Group()

running = True

# Create a list of bars
def draw_bars():
    # width is the result of taking the screen's width 
    # divide by the length of the random_list
    width = int(size[0] / len(random_list))
    for i in range(len(random_list)):
        # Height of a bar is the value of the number         
        height = random_list[i]
        # Create a bar
        bar = Bar(BLUE, width, height)
        # x-coordinate of the bar
        bar.rect.x = i * width
        # Since pygame starts drawing fomr top left,
        # we need to adjust the y-coordinate to start
        # from bottom left
        bar.rect.y = size[1] - random_list[i]
        # Draw the bar
        pygame.draw.rect(screen, BLUE, [bar.rect.x, bar.rect.y, width, height])
        all_sprites_list.add(bar)

def init_setup():
    draw_bars()
    screen.fill(WHITE)
    all_sprites_list.draw(screen)
    pygame.display.flip()

def redraw_bars():
    pygame.time.delay(100)
    all_sprites_list.empty()
    draw_bars()
    screen.fill(WHITE)
    all_sprites_list.draw(screen)
    pygame.display.flip()

def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

def selection_sort():
    for i in range(len(random_list)):
        check_events()

        min_index = i
        for j in range(i, len(random_list)):
            if random_list[min_index] > random_list[j]:
                min_index = j
        random_list[i], random_list[min_index] = random_list[min_index], random_list[i]
        redraw_bars()

def keep_running():
    while True:
        check_events()

def main():
    pygame.init()
    draw_bars()
    init_setup()
    selection_sort()
    keep_running()

main()