#5. Find Common Elements in Three Sorted Arrays
#for unsorted array
def commonElements(a,b,c):
    intersection1 = []
    for num in a:
        if num in b and num not in intersection1:
            intersection1.append(num)
            
    intersection2 = []        
    for num in intersection1:
        if num in c:
            intersection2.append(num)
        
    return 0 if not intersection2 else intersection2        

"""
#for sorted array
def commonElements(a,b,c):
    i,j,k = 0,0,0
    intersection = []
    while (i<len(a) and j<len(b) and k<len(c)) :
        if a[i] == b[j] and b[j] == c[k]:
            if not intersection or intersection[0] != a[i]:
                intersection.append(a[i])
            i+=1
            j+=1
            k+=1
        elif a[i] < b[j]:
            i+=1
        elif b[j] < c[k]:
            j+= 1
        else :
            k+= 1
    return intersection
"""
if __name__ == "__main__":
    a = [1, 5, 10, 20, 30]
    b = [5, 13, 15, 200]
    c = [10 ,5]
    print("commonElements:",commonElements(a, b , c))
