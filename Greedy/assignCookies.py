# Assign Cookies
def assignCookies(g,s):
    g.sort()
    s.sort()
    count = 0
    i, j = 0, 0
    while i < len(g) and j < len(s):
        if g[i] <= s[j]:
            count += 1
            i += 1
        j += 1
    return count
    
g = [1,2,3]
s = [1,1]
print("5. assignCookies:",assignCookies(g,s))
