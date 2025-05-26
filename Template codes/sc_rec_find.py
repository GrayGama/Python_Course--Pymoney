def rec_find(L, val):
    if type(L) in {list, tuple}: # if look inside members of L
        for i, v in enumerate(L):
            p = rec_find(v, val) # recursively find each member
            if p == True: # L[i] == val, so we return (i,)
                return (i,)
            if p != False: # L[i] recursively found val,
                return (i,)+p # so we prepend i to its path p
    return L == val # either L is not seq or for-loop didn't find