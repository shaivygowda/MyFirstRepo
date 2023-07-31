l=['ABA','PYT','XYZ','MOM','NAN','HANNAH']
d={}
d1={}
for i in l:
    print(i)
for i in l:
    if i==i[::-1]:
        d[i]='yes'
    else:
        d[i]='no'
for i in l:
    print(i,len(i))
for i in l:
    d1[i]=len(i)
