# Insertion Sort

def insertion_sort(L):
    from sort_visualizer import check_events, redraw_bars
 
    for i in range(1, len(L)):
        j = i - 1
        key = L[i]
        while (j >= 0 and L[j] > key):
            L[j + 1] = L[j]
            j -= 1
            redraw_bars(20)
            check_events()
        L[j + 1] = key
