#error handling
#types of errors:
#1.zerodivisionerror
try:
    a = int(input("enter a numerator:"))
    b = int(input("enter a denominator:"))
    c = a//b
    print(c)
except ZeroDivisionError:
    print("the value is infinity, and the denominator should not be zero.")
#2.value error
try:
    rollno = int(input("enter your rollno:"))
except ValueError:
    print("the given is not an integer datatype.")
#3.index error
try:
    a =[1,2,3,4,5]
    print(a[10])
except IndexError:
    print("the index is not in the given list.")
#4.key error
try:
    z = {"a":"1","b":"2"}
    print(z['c'])
except KeyError:
    print("the provided key is not in the dictionary.")
#5.type error
try:
    a = "jhjkd"
    b = 254
    c = bool(a+b)
    print(c)
except TypeError:
    print("the output is in two different datatypes")
#6.filenotfounderror
try:
    file = open("nothingfile.txt","r")
    cont = file.read()
    print(cont)
except FileNotFoundError:
    print("the file you seeking is not found in the system.")
finally:
    print("program is executed")
#7.nameerror
#try:
#    print(nazeem)
#except NameError:
#    print("variable not declared")

    
