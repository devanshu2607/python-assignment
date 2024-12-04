##59.	Develop a divide-and-conquer algorithm to sort an array.

def merge_sort(arr):
    if len(arr) <= 1:return arr
    mid = len(arr)//2
    left,right = merge_sort(arr[:mid]),merge_sort(arr[mid:])
    return merge(left,right)

def merge(left, right):
    result, i, j=[],0,0
    while i< len(left) and j< len(right):
        if left[i]<right[j]: result.append(left[i]); i +=1
        else : result.append(right[j]); j+=1
    return result + left[i:]+right[j:]

print(merge_sort([36,55,46,82,92,12]))