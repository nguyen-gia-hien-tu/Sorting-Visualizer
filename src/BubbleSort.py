# Bubble Sort
def bubble_sort(L):
    from sort_visualizer import check_events, redraw_bars
    
    for i in range(len(L) - 1):
        for j in range(len(L) - 1 - i):
            check_events()
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]
            redraw_bars(20)