#1. Rearrange the Array in Alternating Positive and Negative Items
"""
def rearrange(arr):
    pos = []
    neg = []
    for num in arr:
        if num >= 0:
            pos.append(num)
        else:
            neg.append(num)

    posIdx = 0
    negIdx = 0
    i = 0

    while posIdx < len(pos) and negIdx < len(neg):
        if i % 2 == 0:
            arr[i] = pos[posIdx]
            posIdx += 1
        else:
            arr[i] = neg[negIdx]
            negIdx += 1
        i += 1

    while posIdx < len(pos):
        arr[i] = pos[posIdx]
        posIdx += 1
        i += 1

    while negIdx < len(neg):
        arr[i] = neg[negIdx]
        negIdx += 1
        i += 1
"""
def rearrange(arr,n):
    pos = 0 
    neg = 1 
    while pos < n and neg < n:
        if arr[pos] >= 0:
            pos += 2
        elif arr[neg] < 0:
            neg += 2
        else:
            arr[pos], arr[neg] = arr[neg], arr[pos]
            pos += 2
            neg += 2
    return arr

if __name__ == "__main__":
    arr = [1, 2, 3, -4, -1, 4]
    n = len(arr)
    print("rearrange:",rearrange(arr,n))
