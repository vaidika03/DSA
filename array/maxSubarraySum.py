# # 6. Find the Largest Sum Contiguous Subarray
def maxSubarraySum(arr,n):
    maxSum = arr[0]
    currSum = arr[0]
    for i in range(1,n):
        currSum = max(currSum +arr[i], arr[i])
        if currSum > maxSum:
            maxSum = currSum
    return maxSum    

if __name__ == "__main__":
    arr = [2, 3, -8, 7, -1, 2, 3]
    n = len(arr)
    print("maxSubarraySum =",maxSubarraySum(arr, n))  
