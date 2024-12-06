#3. Subarrays with Equal 1s and 0s
def countSubarrWithEqualZeroAndOne(arr,n):
    um = {}
    currSum = 0
    for i in range(0,n):
        currSum +=(-1 if (arr[i]==0) else 1)
        um[currSum] = um.get(currSum,0)+1
    count = 0
    for itr in um:
        if um[itr] > 1:
            count += ((um[itr] * int(um[itr] - 1)) / 2)        
    if um.get(0):
        count += um[0]  
    return count        
            
if __name__ == "__main__":
    arr = [1, 0, 0, 1, 0, 1, 1]
    n = len(arr)
    print("Count =",countSubarrWithEqualZeroAndOne(arr, n))
