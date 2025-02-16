# 5. Minimize the Maximum Difference Between the Heights
def getMinDiff(arr, k, n):
    arr.sort()
    smallest =  arr[0]+k
    largest = arr[n-1]-k
    ans = largest-smallest
    for i in range(0,n-1):
        mi = min(smallest,arr[i+1]-k)
        ma = max(largest,arr[i]+k)
        #print(ma-mi)
        if mi < 0:
            continue
        ans = min(ans,ma-mi)
    return ans    
if __name__ == "__main__":
    k = 3
    arr = [1, 5, 10, 15]
    n = len(arr)
    print("getMinDiff:",getMinDiff(arr, k, n))
