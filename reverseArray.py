#2Array Reverse using two pointer
# O(n) time with O(1) space complexity.
def reverseArray(arr,n):
    low = 0
    high = n-1
    while (low < high):
        arr[low],arr[high] = arr[high],arr[low]
        low += 1
        high -= 1
    return arr   
    
    
if __name__ == "__main__" :
    arr = [1000, 11, 445, 1, 330, 3000]
    n = len(arr)
    print(reverseArray(arr,n))
    
