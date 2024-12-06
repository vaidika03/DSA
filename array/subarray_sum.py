#1. Subarray with Given Sum
#TC: o(N) , SC:O(1)
def subarray_sum(arr, n, target_sum):
    low = 0
    currSum = 0
    for high in range(n):
        currSum += arr[high]
        while currSum > target_sum and low <= high:
            currSum -= arr[low]
            low += 1
        if currSum == target_sum:
            return arr[low:high+1]    
    return 0      
            
if __name__ == "__main__":
    arr = [15, 2, 4, 8, 9, 5, 10, 23]
    n = len(arr)
    target_sum = 26
    print(subarray_sum(arr, n, target_sum))
