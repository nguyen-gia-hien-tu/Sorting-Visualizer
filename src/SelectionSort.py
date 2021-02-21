# Selection Sort

def selection_sort(L):
    from sort_visualizer import check_events, redraw_bars

    for i in range(len(L)):
        check_events()

        min_index = i
        for j in range(i, len(L)):
            check_events()

            if L[min_index] > L[j]:
                min_index = j
        L[i], L[min_index] = L[min_index], L[i]
        redraw_bars(50)
