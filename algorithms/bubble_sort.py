arr = [5, 1, 4, 2, 8]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        j = i
        for j in range(n - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

print(bubble_sort(arr))