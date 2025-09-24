#sets
#unique values only
my_set = {1,2,3,3,2,1,2,3}
print(my_set)
#creating a set
a1 = {1,2,3}
a2 = {10,1,2,"hello",True}
#empty set
a3 = set()
print(type(a3))
#accessing a set
a4  = {"Rajinikanth","Nagarjuna","Shoubin Sahir"}
for role in a4:
    print(role)
#adding elements in a set
S = {10,20,30}
S.add(99)
S.update([26,5,44,88,99,55,99])
print(S)
# deleting elements in a set
S.remove(99)
print(S)
S.clear()
print(S)
#discard():
s1 = {1,20,3,254,65,41}
s1.discard(205)
print(s1)
#pop(): removes the random element from the set
s1.pop()
print(s1)
#Mathematical operation in sets
#union "|"
A = {1,2,3,4}
B = {4,5,6}
print(A|B)
#intersection
print(A&B)
#difference
print(A - B)
#sort
A.sort()
print(A)