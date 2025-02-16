# 1. Find the Peak Element Which Is Not Smaller Than Its Neighbors
def peakElement(arr,n):
    if n ==1:
        return 0
    if arr[0] > arr[1]:
        return 0
    if arr[n-1] > arr[n-2]:
        return n-1
    lo,hi = 0,n-1
    mid = lo +(hi-lo)//2
    while(lo <= hi):
        mid = lo +(hi-lo)//2
        if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
            return mid
        elif arr[mid] < arr[mid+1]:
            lo = mid+1
        else:
            hi = mid-1

if __name__ == "__main__":
    arr = [1, 2, 4, 5, 7, 8, 3]
    n = len(arr)
    print("peakElement:",peakElement(arr,n))
