# N meetings in one room
def maxMeetings(start, end, n):
    meetings = list(zip(start, end))
    meetings.sort(key=lambda x: x[1])
    last_end_time = -1
    count = 0    
    for meeting in meetings:
        if meeting[0] > last_end_time:
            count += 1
            last_end_time = meeting[1]    
    return count

start = [1, 3, 0, 5, 8, 5]
end =  [2, 4, 6, 7, 9, 9]
print("1. n meetings in one room:",maxMeetings(start, end, len(start)))
#------------------------------------------------------------------------------
#2. Program to find minimum number of platforms required on a railway station
def findPlatform(arr, dep, n):
    arr.sort()
    dep.sort()
    plat_needed = 1
    result = 1
    i = 1
    j = 0
    while (i < n and j < n):
        if (arr[i] <= dep[j]):
            plat_needed += 1
            i += 1
        elif (arr[i] > dep[j]):
            plat_needed -= 1
            j += 1
        if (plat_needed > result):
            result = plat_needed
    return result
arr = [100, 300, 500]
dep = [900, 400, 600]
n = len(arr)
print("2. platform needed:",findPlatform(arr, dep, n))
#-----------------------------------------------------------------------------------------
# Fractional Knapsack Problem
def fractionalknapsack(val, wt, capacity):
    arr = zip(val,wt)
    arr = sorted(arr,key = lambda x: x[0] / x[1], reverse=True)
    currCap = 0
    remWeight = capacity
    for v,w in arr:
        if remWeight > 0:
            if remWeight >= w:
                currCap += v
                remWeight -= w
            else:
                ratio = remWeight/w
                currCap += (v*ratio)
                break
    return currCap
                   
val = [60, 120, 100]
wt = [10, 30, 20]
capacity = 50
print("3. fractionalknapsack:",fractionalknapsack(val, wt, capacity) )   
#-------------------------------------------------------------------------------------
# Greedy algorithm to find minimum number of coins
"""
def minCoins(coins,amount):
    n = len(coins)
    memo = [[float('inf')] * (amount + 1) for _ in range(n + 1)]
    memo[0][0] = 0 

    for i in range(1, n + 1):
        coin = coins[i - 1]  
        for j in range(amount + 1):
            #coin excluded
            memo[i][j] = memo[i - 1][j]
            if j >= coin:
                #coin included
                memo[i][j] = min(memo[i][j], 1 + memo[i][j - coin])

    if result != float('inf'):
        return memo[n][amount]
    return -1
"""   
def minCoins(coins,amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    # Process each coin
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1
    
coins = [25,10,5]
exp = 65
print("4. minCoins:",minCoins(coins,exp))    
#--------------------------------------------------------------------------------------
# Assign Cookies
def assignCookies(g,s):
    g.sort()
    s.sort()
    count = 0
    i, j = 0, 0
    while i < len(g) and j < len(s):
        if g[i] <= s[j]:
            count += 1
            i += 1
        j += 1
    return count
    
g = [1,2,3]
s = [1,1]
print("5. assignCookies:",assignCookies(g,s))

#----------------------OUTPUT-----------------------------------------------------------------------
# 1. n meetings in one room: 4
# 2. platform needed: 2
# 3. fractionalknapsack: 240.0
# 4. minCoins: 4
# 5. assignCookies: 1
