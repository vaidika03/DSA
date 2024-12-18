# #### **Dynamic Programming & Greedy Algorithms**
#----------------------------------------------------------
# 1. Trapping Rainwater
"""
def trappingWater(arr,n):
    left = [0]*n
    left[0] = arr[0]
    res = 0
    for i in range(1,n):
        left[i] = max(left[i - 1], arr[i])

    right = [0]*n
    right[n-1] = arr[n-1]
    for i in range(n-2,-1,-1):
        right[i] = max(right[i+1], arr[i])
    print("right",right)
    print("left",left)
    for i in range(n):
        res += min(right[i],left[i]) - arr[i]
    return res
"""
def trappingWater(arr, n):
    n = len(arr)
    left_max = 0
    right_max = 0
    left, right = 0, n - 1
    res = 0
    while left <= right:
        if arr[left] <= arr[right]:
            if arr[left] >= left_max:
                left_max = arr[left]
            else:
                res += left_max - arr[left]
            left += 1
        else:
            if arr[right] >= right_max:
                right_max = arr[right]
            else:
                res += right_max - arr[right]
            right -= 1     
    return res

if __name__ =="__main__":
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    n=len(height)
    print("trappingWater:",trappingWater(height,n))
#--------------------------------------------------------------------    
# 2. Coin Change Problem
"""
def count(coins, sum):
    n = len(coins)
    if sum == 0:
        return 1
    if sum < 0 or n == 0:
        return 0
    dp = [[0]*(sum+1) for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 1

    for i in range(1,n+1):
        for j in range(1,sum+1):
            if coins[i-1] <= j:
                dp[i][j]= dp[i-1][j]+dp[i][j-coins[i-1]]
            else: 
                dp[i][j]= dp[i-1][j]
    return dp[n][sum]
"""
def count(coins, target):
    n = len(coins)
    dp = [0]*(target+1) 
    dp[0] = 1
    for coin in coins:
        for i in range(coin,target+1):
            dp[i] += dp[i-coin] 
    return dp[target]

if __name__ == "__main__":
    coins = [1, 2, 3]
    target = 5
    print("count:",count(coins, target))
#---------------------------------------------------------------------
# 3. Partition Equal Subset Sum
"""
def canPartition(arr,n):
    n = len(arr)
    arrSum = sum(arr) 
    if arrSum%2 != 0:
        print("False")
    arrSum = arrSum // 2
    dp = [[False] * (arrSum + 1) for _ in range(n + 1)]
    for i in range(n+1):
        dp[i][0] = True

    for i in range(1,n+1):
        for j in range(1,arrSum+1):
            if j >= arr[i-1]:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i-1]]
            else:
                dp[i][j] = dp[i-1][j] #exclude
    return dp[n][arrSum] 

def canPartition(arr,n):
    n = len(arr)
    arrSum = sum(arr)
    print(arrSum)
    if arrSum%2 != 0:
        return(False)
    arrSum = arrSum // 2
    dp = [False] * (arrSum + 1)
    dp[0] = True
    for num in arr:
        for j in range(arrSum, num - 1, -1):
            dp[j] = dp[j] or dp[j-num]
    return dp[arrSum]    
"""

def canPartition(arr,n):
    n = len(arr)
    arrSum = sum(arr)
    if arrSum%2 != 0:
        return(False)
    arrSum = arrSum // 2
    dp = {0}
    for num in arr:
        new_dp = set(dp)
        for i in dp:
            if i+num == arrSum:
                return True
            else:
                new_dp.add(i+num)
        dp = new_dp
    return False      
if __name__ == "__main__":
    arr = [2,2, 4,4, 8,8,9,11]
    #arr = [4,4,4,4,4,4,4,4,8,8,8,8,8,8,8,8,12,12,12,12,12,12,12,12,16,16,16,16,16,16,16,16,20,20,20,20,20,20,20,20,24,24,24,24,24,24,24,24,28,28,28,28,28,28,28,28,32,32,32,32,32,32,32,32,36,36,36,36,36,36,36,36,40,40,40,40,40,40,40,40,44,44,44,44,44,44,44,44,48,48,48,48,48,48,48,48,52,52,52,52,52,52,52,52,56,56,56,56,56,56,56,56,60,60,60,60,60,60,60,60,64,64,64,64,64,64,64,64,68,68,68,68,68,68,68,68,72,72,72,72,72,72,72,72,76,76,76,76,76,76,76,76,80,80,80,80,80,80,80,80,84,84,84,84,84,84,84,84,88,88,88,88,88,88,88,88,92,92,92,92,92,92,92,92,96,96,96,96,96,96,96,96,97,99]
    print("canPartition:",canPartition(arr,len(arr)))
#----------------------------------------------------------------------
# 4. Smallest Positive Integer That Can’t Be Represented as a Sum
def findSmallest(arr, n):
    res = 1 
    for i in range(n):
        if arr[i] <= res:
            res = res + arr[i]
        else:
            break
    return res
if __name__ == "__main__":
    arr1 = [1, 3, 4, 5]
    n1 = len(arr1)
    print("findSmallest:",findSmallest(arr1, n1))
#--------------------------------------------------------------------    
# 5. Maximum Sum in the Configuration
def maxSum(arr):
    n = len(arr)
    current_sum = sum(i * arr[i] for i in range(n))
    total_sum = sum(arr)
    max_sum = current_sum
    for i in range(1, n):
        current_sum = current_sum + total_sum - n * arr[n - i]
        max_sum = max(max_sum, current_sum)
    
    return max_sum
if __name__ == "__main__":
    arr = [8, 3, 1, 2]
    n = len(arr)
    print("maxSum:",maxSum(arr))
    
#--------------------------------------------------------------------------------
# 6. Minimum Number of Jumps to Reach the End
def MinJump(arr):
    n = len(arr)
    jump = 0
    step = arr[0]
    maxReach = arr[0]
    for i in range(0,n):
        if i == n-1:
            return jump
        if arr[i]>(n-1-i):
            return jump+1
        maxReach = max(maxReach,arr[i]+i) 
        step -= 1
        if step ==0:
            jump+=1
        if i >= maxReach:
            return -1
        step =  maxReach - i 
    return -1
if __name__ == "__main__":
    arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
    print("MinJump:", MinJump(arr))
    
#smallest positive missing elements
"""
def FindMissing(arr):
    arr.sort()
    res = 1
    for num in arr:
        if res == num:
            res+=1
        elif res < num:
            break
    return res 
"""
def FindMissing(nums):
    n = len(nums)
    visited = [False]*n      
    for i in range(n):
        if 0 < nums[i] <= n:
            visited[nums[i]-1] = True
    for i in range(1,n+1):
        if visited[i-1]==False:
            return i
    return n+1   
if __name__ == "__main__":
    num = [3,4,-1,1]
    print("FindMissing:", FindMissing(num))
