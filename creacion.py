import numpy as np


def suma(l,a=[]):
    suma=0
    for i,elemento in enumerate(a):
        if i==l:
            break
        suma=suma+a[i]
    return suma



def creacion(i,sigma,a=[]):
    if i==1 and sigma==0.5:
        x=0
    if i==1 and sigma==-0.5:
        x=1
    if i==2 and sigma==0.5:
        x=2
    if i==2 and sigma==-0.5:
        x=3

    a=np.array(a)
    h=(1-a[x])
    s=suma(x,a)
    a[x]=a[x]+1
    return h*(-1)**(s)*a
    

print(creacion(1,-0.5,[1,0,1,0]))


