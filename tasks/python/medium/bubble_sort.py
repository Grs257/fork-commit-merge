# Python - Medium

def bubble_sort(arr):
    # TODO: Implement the bubble sort algorithm
    n = len(arr)

    swapped = False
    # Traverse through all array elements
    for i in range(n-1):
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                swapped = True
                arr[j], arr[j+1] = arr[j+1], arr[j]

            # If there is no need for swapping any element; all elements are sorted.
            # We can just exit the main loop.
            if not swapped:
                return


#! Test cases (Don't edit):
arr = [64, 25, 12, 22, 11]
print("Original array:", arr)

bubble_sort(arr)
print("Sorted array:", arr)
