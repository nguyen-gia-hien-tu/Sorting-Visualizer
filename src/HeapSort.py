# Heap Sort

NUM_DELAY = 100

def build_heap(L):
    from sort_visualizer import check_events, redraw_bars

    check_events()
    for i in range(len(L) // 2 - 1, -1, -1):
        check_events()
        sink(L, len(L), i)
        redraw_bars(NUM_DELAY)

def heap_sort(L):
    from sort_visualizer import check_events, redraw_bars

    check_events()
    build_heap(L)

    check_events()
    length_L = len(L)
    for _ in range(len(L)):
        check_events()
        L[0], L[length_L - 1] = L[length_L - 1], L[0]
        redraw_bars(NUM_DELAY)
        length_L -= 1
        sink(L, length_L, 0)
    return L

def sink(L, length_L, i):
    largest = i
    if (left(i) < length_L) and (L[left(i)] > L[largest]):
        largest = left(i)
    if (right(i) < length_L) and (L[right(i)] > L[largest]):
        largest = right(i)
    if largest != i:
        L[i], L[largest] = L[largest], L[i]
        sink(L, length_L, largest)

def left(i):
    return 2 * i + 1

def right(i):
    return 2 * i + 2
