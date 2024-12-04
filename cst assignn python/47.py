##47.	Write a sorting algorithm (e.g., bubble sort) and test its functionality.
def bubble_sort(arr):
    n =len(arr)

    for i in range(n):
        for j in range (0,n-i-1):

            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [64,86,52,4,69,53,78]
print("unsorted array:",arr)

bubble_sort(arr)

print("'sorted array:",arr)