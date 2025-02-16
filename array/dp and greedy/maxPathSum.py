# # 4. Max Sum Path in Two Arrays
"""
def intersection_array(a,b):
    a,b = set(a),set(b)
    return list(a & b)
def maxPathSum(arr1,arr2):
    intersection = intersection_array(arr1,arr2)
    idx = 0
    i,j =0,0
    maxSum = 0
    while (idx < len(intersection)):
        sum1,sum2=0,0
        while(i<len(arr1) and arr1[i] <= intersection[idx]):
            sum1+=arr1[i]
            i+=1
        while(j<len(arr2) and arr2[j] <= intersection[idx]):
            sum2+=arr2[j]
            j+=1  
        maxSum += max(sum1,sum2)    
        idx +=1
        
    sum1,sum2=0,0   
    while(i<len(arr1)):
        sum1+=arr1[i]
        i+=1
    while(j<len(arr2)):
        sum2 += arr2[j]
        j+=1
    maxSum += max(sum1,sum2)        
    return maxSum   
"""
def maxPathSum(arr1,arr2):
    idx = 0
    i,j =0,0
    maxSum = 0
    sum1,sum2 = 0,0
    while(i< len(arr1) and j<len(arr2)):
        if arr1[i]<arr2[j]:
            sum1+=arr1[i]
            i+=1
        elif arr2[j]<arr1[i]:
            sum2+=arr2[j]
            j+=1
        else:
            maxSum += max(sum1,sum2) + arr1[i]
            i+=1
            j+=1
            sum1=0
            sum2=0  

    while(i<len(arr1)):
        sum1+=arr1[i]
        i+=1
    while(j<len(arr2)):
        sum2 += arr2[j]
        j+=1

    maxSum += max(sum1,sum2)
    return maxSum

if __name__ == "__main__":
    # arr1 = [2, 3, 7, 10, 12]
    # arr2 = [1, 5, 7, 8]
    arr1 = [2, 3, 7, 10, 12, 15, 30, 34]
    arr2 = [1, 5, 7, 8, 10, 15, 16, 19]
    print("maxPathSum:",maxPathSum(arr1, arr2))
#
