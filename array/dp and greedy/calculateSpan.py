# 3. Stock Span Problem
def calculateSpan(price, n):
    res = [0]*n
    st = []
    st.append(0)
    res[0] = 1
    for i in range(1,n):
        while len(st)>0 and price[st[-1]] <= price[i]:
            st.pop()
        res[i] = i+1 if len(st) == 0 else (i-st[-1])
        st.append(i)
    return res    

if __name__ == "__main__":
    price = [10, 4, 5, 90, 120, 80]
    n = len(price)
    print("calculateSpan",calculateSpan(price, n))
