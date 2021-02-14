# Quicksort "in-place"
def quicksort_inplace(L):
    quicksort(L, 0, len(L) - 1)

def quicksort(L, start, end):
    if start >= end:
        return
    j = partition(L, start, end)
    quicksort(L, start, j-1)
    quicksort(L, j+1, end)

def partition(L, start, end):
    from sort_visualizer import check_events, redraw_bars

    check_events()
    pivot = L[start]
    i = start
    j = end + 1
    while (True):
        i += 1
        while (L[i] <= pivot):
            if (i == end):
                break
            i += 1

        j -= 1
        while (L[j] > pivot):
            if (j == start):
                break
            j -= 1

        if (i >= j):
            break

        L[i], L[j] = L[j], L[i]
        redraw_bars()
    
    L[start], L[j] = L[j], L[start]
    redraw_bars()
    return j
