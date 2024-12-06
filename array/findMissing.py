#2. Find the Missing Integer
def findMissing(arr,n):
    arrSum = sum(arr)
    expectedSum = n*(n+1)/2
    return expectedSum - arrSum
if __name__ == "__main__":
    arr = [1, 2, 3,5, 6]
    n = len(arr)
    print("findMissing:",findMissing(arr,n+1))
