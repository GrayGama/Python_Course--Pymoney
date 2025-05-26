def number_outline(L, prefix=()):
    if type(L) in {list, tuple}:
    # keep prefix[-1], extend by new dimension, starting from 1
        i = 0
        for v in L:
            if type(v) not in {list, tuple}:
                i += 1
            number_outline(v, prefix+(i,))
        # don't increment if v is a list/tuple
        # otherwise, indent and join the prefix together by '.'
    else:
        s = ' ' * 4*(len(prefix)-1)
        s += '.'.join(map(str,prefix))
        s += '. ' + L
        print(s)

