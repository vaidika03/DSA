#Sort the Array of 0s, 1s, and 2s.
# TC : O(N) SC: O(N)
def sortColour(arr,n):
    low, mid, high = 0, 0, n - 1 
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:  # nums[mid] == 2
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1    
    return arr
    
if __name__ == "__main__" :
    arr= [1, 0,2,1,0] 
    n = len(arr)
    print(sortColour(arr,n))

