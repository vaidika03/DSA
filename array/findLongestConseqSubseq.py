#7. Find the Longest Consecutive Subsequence
def findLongestConseqSubseq(arr,n):
    s = set()
    ans = 0
    for ele in arr:
        s.add(ele)
    for i in range(n):
        if (arr[i]-1 not in s):
            j = arr[i]
            while(j in s):
                j+=1
            ans = max(ans, j - arr[i])    
    return ans       
if __name__ == "__main__":
    arr = [1, 9, 3, 10, 4, 20, 2]
    n = len(arr)
    print("findLongestConseqSubseq =",findLongestConseqSubseq(arr, n))  
