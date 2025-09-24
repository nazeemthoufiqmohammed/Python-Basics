#examples
my_tuple = (10,20,30)
print(my_tuple)
print(type(my_tuple))
#creating a tuple
#empty tuple
empt = ()
#with numbers
num = (1,2,3,5,6,7)
#with strings 
s = ("A","B","C","D")
#with mixed datatypes
x = (1,2,3,"a","B",True,"False")
#with single element
one = (151,)
print(type(one))
#accessing elements in tuple
xy = ["a","b","c","d","e"]
print(xy[0])
print(xy[-1])
#changing the values
xy[2] = "v"
print(xy)
#ERROR
xy.append("v")
print(xy)
#length
l = len(xy)
print(l)
z = (1,2,3,4,99)
#max
print(max(z))
#min
print(min(z))
#sum
print(sum(z))
#concatenation
y = (5,6,8)
k = z+y
print(k)
#repitition
n = int(input("enter a num:"))
krep = y*n
print(krep)
#searching and checking
o = int(input("enter a number to search:"))
if o in y:
    print("yes")
if o not in y:
    print("no")
#index()
print(y.index(5))
#count()
y_cnt = 0
for i in y:
    y_cnt += 1
print(y_cnt)
#sorting and reversing are not applicable in tuples cause elements are not mutable.
#copying tuples
q = ()
copy_y = q + y
print(copy_y)
#iterations in tuples using for loops
ax = (20,30,10,50,60)
for i in ax:
    print(i)
    
