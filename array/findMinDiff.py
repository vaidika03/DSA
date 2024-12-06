#4. Chocolate Distribution Problem
def findMinDiff(arr, m , n):
    arr.sort()  #1,2,3,4,5,6,7
    start = 0
    end = m-1
    minDiff = float('inf')
    currDiff = 0
    while(end < n):
        currDiff = arr[end] - arr[start]
        minDiff = min(minDiff, currDiff)
        start += 1
        end += 1
    return minDiff    
    
if __name__ == "__main__":
    arr = [7, 3, 2, 4, 9, 12, 56]
    m = 3
    print("findMinDiff: ",findMinDiff(arr, m , len(arr)))
