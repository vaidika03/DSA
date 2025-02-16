# 7. Find the Largest Sum Contiguous Subarray
def maxSum(arr, n):
    currSum = arr[0]
    maxSum = arr[0]
    for i in range(1,n):
        currSum = max(arr[i],currSum+arr[i])
        maxSum = max(maxSum,currSum)
    return maxSum
if __name__ == "__main__":
    arr = [-2, -3, 4, -1, -2, 1, 5, -3]
    n = len(arr)
    print("maxSum:",maxSum(arr, n))
