import random

class SelectionSort:
    def __init__(self, L):
        self.L = L

    def get_list(self):
        return self.L

    def selection_sort(self):
        import sort_visualizer
        for i in range(len(self.L) - 1):
            min_index = self.__find_min_index(i)
            self.L[i], self.L[min_index] = self.L[min_index], self.L[i]
            sort_visualizer.update(self)

    def __find_min_index(self, start):
        min_idx = start
        for i in range(start + 1, len(self.L)):
            if self.L[i] < self.L[min_idx]:
                min_idx = i
        return min_idx
