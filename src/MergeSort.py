# Merge Sort
def merge_sort(L):
    aux = []
    for num in L:
        aux.append(num)

    m_sort(L, aux, 0, len(L) - 1)

def m_sort(L, aux, start, end):
    if end <= start:
        return
    mid = (start + end) // 2
    m_sort(L, aux, start, mid)
    m_sort(L, aux, mid+1, end)
    merge(L, aux, start, mid, end)

def merge(L, aux, start, mid, end):
    from sort_visualizer import check_events, redraw_bars

    i = start
    j = mid + 1
    for index in range(start, end + 1):
        aux[index] = L[index]
    
    for k in range(start, end+1):
        if i > mid:
            L[k] = aux[j]
            j += 1
        elif j > end:
            L[k] = aux[i]
            i += 1
        elif aux[i] <= aux[j]:
            L[k] = aux[i]
            i += 1
        else:
            L[k] = aux[j]
            j += 1
        redraw_bars(30)
        check_events()

