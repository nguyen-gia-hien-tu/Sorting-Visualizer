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
pygame.font.init()

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


# Redraw the bars after every change in the list
def redraw_bars(num_delay):
    pygame.time.delay(num_delay)
    all_sprites_list.empty()
    draw_bars()
    screen.fill(WHITE)
    all_sprites_list.draw(screen)
    pygame.display.flip()


# Instruction Page
def write_text(text, x, y):
    check_events()
    my_font = pygame.font.SysFont('Comic Sans MS', 25)
    text_surface = my_font.render(text, True, BLACK)
    screen.blit(text_surface, (x, y))

def instruction_page():
    check_events()
    screen.fill(WHITE)
    write_text("Choose a sorting algorithm to visualize", 30, 0)
    for i in range(1, 7):
        pygame.draw.rect(screen, BLUE, (156, 70 * i, 200, 50))
    write_text("Bubble Sort", 190, 70 * 1 + 5)
    write_text("Selection Sort", 170, 70 * 2 + 5)
    write_text("Insertion Sort", 170, 70 * 3 + 5)
    write_text("Merge Sort", 190, 70 * 4 + 5)
    write_text("Quick Sort", 190, 70 * 5 + 5)
    write_text("Heap Sort", 200, 70 * 6 + 5)
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
    instruction_page()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if (pos[0] >= 156 and pos[0] <= 356) and (pos[1] >= 70 and pos[1] <= 120):
                        bubble_sort(random_list)
                    elif (pos[0] >= 156 and pos[0] <= 356) and (pos[1] >= 140 and pos[1] <= 190):
                        selection_sort(random_list)
                    elif (pos[0] >= 156 and pos[0] <= 356) and (pos[1] >= 210 and pos[1] <= 260):
                        insertion_sort(random_list)
                    elif (pos[0] >= 156 and pos[0] <= 356) and (pos[1] >= 280 and pos[1] <= 330):
                        merge_sort(random_list)
                    elif (pos[0] >= 156 and pos[0] <= 356) and (pos[1] >= 350 and pos[1] <= 400):
                        quicksort_inplace(random_list)
                    elif (pos[0] >= 156 and pos[0] <= 356) and (pos[1] >= 420 and pos[1] <= 470):
                        heap_sort(random_list)

main()
