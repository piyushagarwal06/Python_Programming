a=(1)
b=()
c=(1,)
d=(1,2,3,)
print(type(a))
print(type(b))
print(type(c))
print(type(d))
d[0]=44
print(d) #error-TypeError: 'tuple' object does not support item assignment