# MRO - Method Resolution Order
# Reference:
# https://replit.com/@aneagoie/MRO#main.py
# http://www.srikanthtechnologies.com/blog/python/mro.aspx

class A:
    num = 10

class B(A):
    pass

class C(A):
    num = 1

class D(B, C):
    pass

print(D.mro())
D.__str__