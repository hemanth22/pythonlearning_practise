# MRO - Method Resolution Order
# Reference:
# https://replit.com/@aneagoie/MRO#main.py
# http://www.srikanthtechnologies.com/blog/python/mro.aspx
# https://data-flair.training/blogs/python-multiple-inheritance/

class X:pass
class Y: pass
class Z:pass
class A(X,Y):pass
class B(Y,Z):pass
class M(B,A,Z):pass

print(M.__mro__)