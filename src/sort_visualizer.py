import sys
import random

import pygame

from BubbleSort import bubble_sort
from SelectionSort import selection_sort
from InsertionSort import insertion_sort
from QuickSort import quicksort_inplace
from MergeSort import merge_sort
from HeapSort import heap_sort
from Bar import Bar


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)


pygame.init()

size = (512, 512)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Sorting")

random_list = [i for i in range(256)]
random.shuffle(random_list)
all_sprites_list = pygame.sprite.Group()


# Draw the bars
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

# Initial setup
def init_setup():
    draw_bars()
    screen.fill(WHITE)
    all_sprites_list.draw(screen)
    pygame.display.flip()

# Redraw the bars after every change in the list
def redraw_bars(num_delay):
    pygame.time.delay(num_delay)
    all_sprites_list.empty()
    draw_bars()
    screen.fill(WHITE)
    all_sprites_list.draw(screen)
    pygame.display.flip()

# Check if the <close> button is pressed to end the window
def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

# Keep running the window
def keep_running():
    while True:
        check_events()

# Main method
def main():
    init_setup()
    check_events()
    # Take the user command line input
    if sys.argv[1] == "BubbleSort":
        bubble_sort(random_list)
    elif sys.argv[1] == "SelectionSort":
        selection_sort(random_list)
    elif sys.argv[1] == "InsertionSort":
        insertion_sort(random_list)
    elif sys.argv[1] == "MergeSort":
        merge_sort(random_list)
    elif sys.argv[1] == "QuickSort":
        quicksort_inplace(random_list)
    elif sys.argv[1] == "HeapSort":
        heap_sort(random_list)
    else:
        print("Wrong input argument")
    keep_running()

main()
