import random
import timeit


def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i] # the current element equal to lst[i]
        j = i-1 # index of the previous element
        while j >=0 and key < lst[j] : # compare key with each element on the left of it until an element smaller than it is found
                lst[j + 1] = lst[j]
                j -= 1
        lst[j + 1] = key
    return lst


def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left_half = lst[:mid]
    right_half = lst[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # First, merge the smaller elements
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # If there are remaining elements in the left or right half, 
        # add them to the result
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

def timsort(lst):
    return sorted(lst)
     

     
# main block to test the function
if __name__ == "__main__":
    for n in [100, 1000, 5000]:
        lst = random.sample(range(1, n+1), n)  # list of n random integers between 1 and n

        print(f"n = {n}")
        print(" insertion_sort time:", round(timeit.timeit(lambda: insertion_sort(lst.copy()), number=10), 5))
        print(" merge_sort     time:", round(timeit.timeit(lambda: merge_sort(lst.copy()), number=10), 5))
        print(" timsort        time:", round(timeit.timeit(lambda: timsort(lst.copy()), number=10), 5))
        print()  