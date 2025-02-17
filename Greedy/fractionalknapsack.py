#3. Fractional Knapsack Problem
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
