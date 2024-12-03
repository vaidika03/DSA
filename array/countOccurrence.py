#5. Find the Occurrence of an Integer in the Array
#use predefined Counter(arr) function
# TC : O(N) , SC : O(1)
def countOccurence(arr,n,element):
    count = 0
    for i in range(n):
        if element == arr[i]:
            count += 1
    return count
"""
def binarySearch(arr, low, high, element, find_first):
    result = -1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == element:
            result = mid
            # If we want to find the first occurrence, move left
            if find_first:
                high = mid - 1
            # If we want to find the last occurrence, move right
            else:
                low = mid + 1
        elif arr[mid] < element:
            low = mid + 1
        else:
            high = mid - 1
    return result

def countOccurrence(arr, element,n):
    arr.sort()
    first = binarySearch(arr, 0, n - 1, element, True)
    if first == -1:
        return 0
    last = binarySearch(arr, 0, n - 1, element, False)
    return last - first + 1

#not optimized but can be used if array is already sorted
import bisect
def countOccurrence(arr, element):
    arr.sort()
    first = bisect.bisect_left(arr, element)
    last = bisect.bisect_right(arr, element)
    return last - first
"""
if __name__ == "__main__" :
    arr= [1, 2, 2, 2, 5] 
    n = len(arr)
    element = 2 
    print(countOccurence(arr,n,element))
