#Find Duplicates in an Array
#TC : O(N) , SC :O(N)
def findDuplicates(arr,n):
    seen = set()
    duplicate = set()
    for num in arr:
        if num in seen:
            duplicate.add(num)
        else: 
            seen.add(num)
    return duplicate
"""
from collections import defaultdict
def findDuplicates(arr,n):
    count = defaultdict(int)
    for num in arr:
        count[num] += 1
    return [num for num,cnt in count.items() if cnt>1]    
"""
if __name__ == "__main__" :
    arr= [1, 2, 2, 5, 5] 
    n = len(arr)
    print(findDuplicates(arr,n))
