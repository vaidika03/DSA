# 2. Find the Maximum Product Subarray
def maxProduct(arr,n):
    resMax = float('-inf')
    ltor,rtol = 1,1
    for i in range(n):
        if ltor == 0:
            ltor =1
        if rtol == 0:
            rtol = 1
        ltor *= arr[i]
        j = n-i-1
        rtol *= arr[j]
        resMax = max(ltor,rtol,resMax)
    return resMax
"""
def maxProduct(arr,n):
    currMax = arr[0]
    currMin = arr[0]
    resMax = arr[0]
    for i in range(1,n):
        if arr[i]<0:
            currMax,currMin = currMin,currMax
        currMax = max(arr[i],currMax*arr[i])
        currMin = min(arr[i],currMin*arr[i])
        
        resMax = max(currMax,resMax)
    return resMax
"""

if __name__ == "__main__":
    arr = [-2, 6, -3, -10, 0, 2]
    n = len(arr)
    print("maxProduct:",maxProduct(arr,n))
