#8. count Pairs with the Given Sum in a Sorted Array
def countPairs(arr,k):
    setArray = set()
    result = []
    count = 0
    for num in arr:
        rem = k-num
        if rem in setArray:
            result.append((num,rem))
            count+=1
        else:
            setArray.add(num)
    return count       
    
if __name__ == "__main__":
    k = 7
    arr = [1, 2, 3, 4, 5, 6, 7]
    print("countPairs:",countPairs(arr,k)) 
