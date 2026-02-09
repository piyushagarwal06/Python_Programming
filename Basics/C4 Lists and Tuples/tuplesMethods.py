a=(1,45,343,3434,False,45,"Rohan")
print(type(a))
print(a)

n=a.count(45)
print(n) #2
print(a.count(45)) #2

print(a.index(3434))

t = (10, 20, 30)
print(len(t))   # Output: 3
print(max(t))   # 30
print(min(t))   # 10
print(sum(t))   # 60
print("banana" in t)   # false

a, b, c = t
print(a, b, c)   # 10 20 30


z = (1, 2, 3, 4, 5)
x, *middle, y =z
print(x)        # 1
print(middle)   # [2, 3, 4]
print(y)        # 5



t = (3, 1, 4, 2)
sorted_t = sorted(t)
print(sorted_t)   # [1, 2, 3, 4] Returns a list, not a tuple.
print(t)
print(sorted(t))
