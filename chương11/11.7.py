L=[1,2,3,4]
thresh=2
def emlementwise_greater_than(L,thresh):
    a=[False]*len(L)
    for i in range(len(L)):
        if L[i]>thresh:
            a[i]=True
    return a
print(emlementwise_greater_than(L,thresh))