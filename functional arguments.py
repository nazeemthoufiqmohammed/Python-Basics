#functional arguments
#1. positional arguments
def func(name,batchno):
    print("he is",name,"from the batch:",batchno)
func("nazeem","k007")
#2. keyword arguments
def func1(idno,name):
    print("he is",name,"id:",idno)
func1(idno="k007",name="nazeem")
#3.default argument
def func2(name="vito corleone"):
    print("he is",name)
func2()    
func2(name="godfather")
#4.variable length arguments
def sum1(*lst):
    sum2 = 0
    for i in range(len(lst)):
        sum2 = sum2 + lst[i]
    print(sum2)
sum1(1,2,3,4,5)
#2.** keyword vriable length arguments
#collects multiple key value pair into a dictionary
def details(**info):
  for i,j in info.items():
      print(i,":",j)
details(name="nazeem",batchno="z007",bgroup="o+ve")
#scope of the variable
x = 30 #global variable
def func11():
    y = 60 #local variable
    print("inside function func11",x,y)
func11()
def func12():
    print("inside function func12",x)
func12()
print("outside function:",x)
#lambda function
sqr1 = lambda c:c*c
print(sqr1(55))
#OR normal function
def sqr(zx):
    print(zx*zx)
sqr(55)
