import numpy as np

'''
#geometric sum
#For any natural number n and any number r!=1
#1 + r + r^2 + ... + r^n = Sum_(k=1)^n[r^k]
'''
def geometric_sum(r,n):
    return (1-r**(n+1))/(1-r)

'''
#Difference of Powers
#a^n - b^n == Sum_(k=0)^(k=n-1)[(a^n-1-k)*(b^k)]
'''
def difference_of_powers(a, b, n):
    d_1 = a - b
    d_2 = 0
    for i in range(n):
        print(n - 1 - i)
        d_2 += (a ** (n - 1 - i))*(b ** i)
    return d_1 * d_2


'''
#Binomial Coefficient
#( n ) = ___n!___
#( k ) = k!(n-k)!
'''
def binomial_coefficient(n, k):
    nfactorial = 1
    kfactorial = 1
    nminuskfactorial = 1
    for i in range(1,n+1):
        nfactorial *= i
    for j in range(1, k+1):
        kfactorial *= j
    for l in range(1, n-k+1):
        nminuskfactorial *= l
    return nfactorial/(kfactorial*nminuskfactorial)


'''Binomial Formula
(a+b)^n = Sum_(k=0)^n[(Binomial Coefficient:_k^n) * a^(n-k)*b^k
'''
def binomial_formula(a,b,n):
    summat = 0.0
    for k in range(n+1):
        summat += binomial_coefficient(n, k) * a ** (n - k) * b ** k
    return summat

'''
L_n distance between points A and B:   
'''
def L_p_distance(A, B, p):
    if(p<=0 or type(p)!='int'):
        print("Error: p must be a positive integer")
        return None
    if(len(A) != len(B)):
        print("Error: Dimension Mismatch")
        return None
    else:
        n = len(A)
        d = 0
        for i in range(1, n+1):
            d += (A[i]-B[i])**p
        return d**(1/p)

'''
Sigmoid Function
'''
def sigmoid(x):
    return(1/(1+exp(-x)))