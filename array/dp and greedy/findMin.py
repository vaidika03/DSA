# 8. Find the Minimum Element in a Rotated and Sorted Array
def findMin(arr, n):
    minVal = 5000
    lo,hi = 0,n-1
    while(lo<hi):
        mid = lo+(hi-lo)//2
        if arr[mid]>arr[hi]:
            lo = mid+1
        else:
            hi=mid 
    return arr[lo]       

if __name__ == "__main__":
    arr = [3,4,5,1,2]
    n = len(arr)
    print("findMin",findMin(arr, n))
