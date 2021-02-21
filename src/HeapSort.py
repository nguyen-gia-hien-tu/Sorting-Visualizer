def build_heap(L):
    for i in range(len(L) // 2 - 1, -1, -1):
        sink(L, len(L), i)

def heap_sort(L):
    build_heap(L)
    length_L = len(L)
    for _ in range(len(L)):
        L[0], L[length_L - 1] = L[length_L - 1], L[0]
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

print(heap_sort([i for i in range(10)]))