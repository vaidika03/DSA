#1. Find the Minimum and Maximum Element in an Array
#Time Complexity: O(n) , Space Complexity: O(1)
class Pair:
    def __init__(self):
        self.mn = 0  
        self.mx = 0  
      
    # Optimized because it minimizes the number of comparisons
    @staticmethod    
    def getMinMax(arr: list, n: int):
        if n == 0:
            return None
       
        minMax = Pair()
        if n == 1:
            minMax.mn = arr[0]  
            minMax.mx = arr[0]  
            return minMax
        
        if arr[0] > arr[1]:
            minMax.mx = arr[0]  
            minMax.mn = arr[1]  
        else:
            minMax.mx = arr[1]  
            minMax.mn = arr[0]  
        
        for i in range(2, n, 2):
            if i + 1 < n: 
                pair_mn = min(arr[i], arr[i+1])
                pair_mx = max(arr[i], arr[i+1]) 
            else:  
                pair_mn = arr[i]
                pair_mx = arr[i]

            minMax.mn = min(minMax.mn, pair_mn) 
            minMax.mx = max(minMax.mx, pair_mx) 

        return minMax
    
    """
    @staticmethod    
    def getMinMax(arr:list, n :int) :
        minMax = Pair()
        if n ==1 : 
            minMax.mn = arr[0]
            minMax.mx = arr[0]
            return minMax
        
        if arr[0] > arr[1]:
            minMax.mx = arr[0]
            minMax.mn = arr[1]
        else:
            minMax.mx = arr[1]
            minMax.mn = arr[0]

        for i in range(2, n):
            if arr[i] > minMax.mx:
                minMax.mx = arr[i]
            elif arr[i] < minMax.mn:
                minMax.mn = arr[i]

        return minMax
    """
# Driver Code
if __name__ == "__main__":
    arr = [1000, 11, 445, 1, 330, 3000]
    arr_size = len(arr)
    minmax = Pair.getMinMax(arr, arr_size)
    print("Minimum element is", minmax.mn) 
    print("Maximum element is", minmax.mx) 

