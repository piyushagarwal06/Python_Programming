# l=[]
# n=int(input("Enter how many numbers"))
# for i in range(n):
#     x = int(input("Enter number: "))
#     l.append(x)
# print(l)



# l = []
# while True:
#     x = input("Enter number (or 'q' to quit): ")
#     if x == 'q':
#         break
#     l.append(int(x))
#t1 = tuple(l)
# print(t1)



t=list(map(int,input("Enter numbers:").split()))
print(t)

t=set(map(int,input("Enter numbers:").split()))
print(t)

t=tuple(map(int,input("Enter numbers:").split()))
print(t)



d = {}
n = int(input("Enter number of items: "))

for i in range(n):
    key, value = input("Enter key and value: ").split()
    d[key] = value

print(d)