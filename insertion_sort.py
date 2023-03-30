import random
import time


def insertion_sort(unsorted_list):
    sorted_list = []
    while(len(unsorted_list) > 0):
        smallest = unsorted_list[0]
        smallest_index = 0
        for index, elem in enumerate(unsorted_list):
            if elem < smallest:
                smallest = elem
                smallest_index = index
        unsorted_list.pop(smallest_index)
        sorted_list.append(smallest)
    return sorted_list


if __name__ == "__main__":
    list = []
    for i in range(9999):
        list.append(random.randint(0, 999))
    start = time.time()
    print(insertion_sort(list))
    end = time.time()
    print(end - start)