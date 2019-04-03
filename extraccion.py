import numpy as np 


def em(a=[]):
    for i,elem in enumerate(a):
        a=np.array(a)
        if a[i]<0:
            h=-1
            a=h*a
            break
        if a[i]>0:
            h=1
            a=h*a
            break
        if i==(np.size(a)-1):
            h=1

    return h,a

x,y=em([0,0,-1,0])

print(x,y)