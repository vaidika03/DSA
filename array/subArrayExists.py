# 5. Find if There is Any Subarray with a Sum Equal to Zero
def subArrayExists(arr,n):
    nset = set()
    currSum = 0
    for i in range(n):
        currSum += arr[i]
        if currSum == 0 or currSum in nset:
            return True
        nset.add(currSum)
    return False    

if __name__ == "__main__":
    arr = [4, -2, 2, 1, 6]
    n = len(arr)
    print("subArrayExists =",subArrayExists(arr, n))
