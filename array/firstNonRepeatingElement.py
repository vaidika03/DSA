# 4. Find the First Non-Repeating Element in a Given Array of Integers
from collections import defaultdict
def firstNonRepeatingElement(arr,n):
    mp = defaultdict(lambda: 0)
    for i in range(n):
        mp[arr[i]] += 1
    for i in range(n):
        if mp[arr[i]] == 1:
            return arr[i]
    return -1    
        
if __name__ == "__main__":
    arr = [1, 2, 3, 1, 3, 5]
    n = len(arr)
    print("firstNonRepeatingElement =",firstNonRepeatingElement(arr, n))
