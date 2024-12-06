#4. Pair with the Given Sum in a Sorted Array
def pair_with_given_sum(arr,k):
    setArray = set()
    result = []
    for num in arr:
        rem = k-num
        if rem in setArray:
            result.append((num,rem))
        else:
            setArray.add(num)
    return result       
    
if __name__ == "__main__":
    k = 7
    arr = [1, 2, 3, 4, 5, 6, 7]
    print("pair_with_given_sum:",pair_with_given_sum(arr,k)) 
