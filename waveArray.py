#11Wave array 

"""
def waveArray(arr,n):
    arr.sort()
    for i in range(0,n-1,2):
        arr[i],arr[i+1] = arr[i+1],arr[i]
    return arr    
"""
def waveArray(arr,n):
    for i in range(0,n-1,2):
        if (i >0 and arr[i] > arr[i-1]):
            arr[i],arr[i-1] = arr[i-1],arr[i]
        
        if (i < n-1 and arr[i] < arr[i+1]):
            arr[i],arr[i+1] = arr[i+1],arr[i]
                        
        
    return arr
if __name__ == "__main__" :
    arr = [1, 10, 12, 6, 3, 2, 20, 100, 80]
    n = len(arr)
    print(waveArray(arr,n))
