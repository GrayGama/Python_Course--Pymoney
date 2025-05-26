name = input()
shlist = input()
shlist = shlist.split(', ')
mdlist = []
for word in shlist: 
    mdlist += word.split('*')

indx = 0
for elem in mdlist: 
    if(mdlist[indx].isdigit()):
        indx += 1
        pass
    else:
        print('%s*%s' %(mdlist[indx], mdlist[indx-1]))
        indx += 1