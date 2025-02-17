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
