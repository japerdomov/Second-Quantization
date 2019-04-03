import numpy as np  

def suma(l,a=[]):
    suma=0
    for i,elemento in enumerate(a):
        if i==l:
            break
        suma=suma+a[i]
    return suma

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

def destruccion(i,sigma,a=[]):
    if i==1 and sigma==0.5:
        x=0
    if i==1 and sigma==-0.5:
        x=1
    if i==2 and sigma==0.5:
        x=2
    if i==2 and sigma==-0.5:
        x=3

    a=np.array(a)
    h=a[x]
    s=suma(x,a)
    a[x]=a[x]-1
    
    return h*(-1)**(s)*a

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
    
def cd(p2,s2,p1,s1,a=[]):
    #Se destruye electron en p1 con s1 y luego se saca su coeficiente
    x,y=em(destruccion(p1,s1,a))
    #Se crea electron en p2 con s2
    y1=creacion(p2,s2,y)
    #Se saca el coeficiente del vector resultante en el paso anterior
    x2,y2=em(y1)

    return x,x2,y2


print(cd(2,0.5,1,-0.5,[0,0,0,0]))