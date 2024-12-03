# 3. Write a Program to Cyclically Rotate an Array by One
#TC : O(N) , SC : O(1)

#optimixed approach for SC = O(1)
def rotateArray(arr:list,n : int, k : int):
    k = k % n
    arr.reverse()
    arr[:k] = reversed(arr[:k])
    arr[k:] = reversed(arr[k:])
    return arr

"""
#SC = O(n)
def rotateArray(arr:list,n : int, k : int):
    output = [0]*n
    idx = 0
    
    for i in range(n-k,n):
        output[idx] = arr[i]
        idx +=1
        
    for i in range(n-k):
        output[idx] = arr[i]
        idx +=1
        
    return output    
"""        
if __name__ == "__main__" :
    arr= [1, 2, 3, 4, 5] 
    n = len(arr)
    k = 2 #rotation degree
    print(rotateArray(arr,n,k))
