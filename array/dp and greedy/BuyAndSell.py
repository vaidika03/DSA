# 6. Stock Buy and Sell Problem
# prices = [7,1,5,3,6,4]
# Output: 5
def BuyAndSell1(arr,n):
    n = len(arr)
    if n <= 1:
        return 0
    buy = 10000
    maxVal = 0
    for num in arr: 
        if num-buy>maxVal:
            maxVal = num-buy
        else:
            buy = num
    return maxVal    

"""
def BuyAndSell2(arr,n):
    n = len(arr)
    maxProfit = 0
    for i in range(1,n):
        if arr[i]>arr[i-1]:
            maxProfit += arr[i]-arr[i-1]
    return maxProfit
"""           
if __name__ == "__main__":
    k = 3
    prices = [1,2,5,14,5]
    n = len(prices)
    print("BuyAndSell1:",BuyAndSell1(prices, n))
