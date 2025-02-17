#6. Palindrome partitioning of string.
def isPalindrome(s):
    return s == s[::-1]
def findSet(s,ans,currSet,idx):
    if idx >= len(s):
        ans.append(list(currSet))
        return
    
    for i in range(idx+1,len(s)+1):
        substr = s[idx:i]
        if isPalidrome(substr):
            currSet.append(substr)
            findSet(s,ans,currSet,i) 
            currSet.pop()
                
def palPartitionRec(s):
    ans = []
    currSet = []
    res = ""
    findSet(s,ans,currSet,0)
    return ans

s = "aab"
print("6. palPartitionRec:",palPartitionRec(s))
