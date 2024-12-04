##46.	Implement a binary search algorithm on a sorted list of numbers.

def binary_search(arr,target):
    left, right =0,len(arr)-1

    while left<=right:
        mid=left+(right-left)//2

        if arr[mid]==target:
            return mid
        elif arr[mid] <target:
            left=mid+1
        else:
            right=mid-1
        return -1


arr=[2,6,8,4,3,70,50]
target=6

result =binary_search(arr,target)
if result !=-1:
    print(f"elemnt is present at index {result}")
else:
    print("element is not present in array ")