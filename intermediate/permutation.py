def toString(str_list):
    return "".join(str_list)

def permutate(st , s, e):
    if s==e:
        print(toString(st))
    else:
        for i in range(s , e):
            st[s] , st[i] = st[i] , st[s]
            permutate(st , s+1 , e)
            st[s] , st[i] = st[i] , st[s]
st = "ABC"
permutate(list(st) , 0 , len(st))
