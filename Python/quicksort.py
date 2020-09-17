#quicksort algorithm

def quicksort(A0,A1,p,r):
    if p<r:
        q = partition(A0,A1,p,r)
        quicksort(A0,A1,p,q-1)
        quicksort(A0,A1,q+1,r)
        
def partition(A0,A1,p,r):
    x = A1[r]
    i = p-1
    for j in range(p,r):
        if A1[j]<=x:
            i = i+1
            tempA0 = A0[j]
            A0[j] = A0[i]
            A0[i] = tempA0
            tempA1 = A1[j]
            A1[j] = A1[i]
            A1[i] = tempA1
    temp0 = A0[r]
    A0[r] = A0[i+1]
    A0[i+1]= temp0
    temp1 = A1[r]
    A1[r] = A1[i+1]
    A1[i+1]= temp1
    return i+1