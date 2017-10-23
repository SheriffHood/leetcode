#!/usr/bin/env python3
#-*- coding:utf-8 -*-
 
def myPow(x, n):
    if n == 0:
        return 1
    if n < 0:
        return 1 / myPow(x, -1*n)
    tmp =  myPow(x, n//2)
    if n % 2 == 1:
        return tmp * tmp * x
    else:
        return tmp * tmp

print( myPow(9, 2) )
print( myPow(2, 0) )
print( myPow(-2, 2) )
print( myPow(8, -3) )
