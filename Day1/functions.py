#functions
'''
def function1():
    print("Its a function")
function1()
def function2(n1,n2):
    print("n1=",n1,"n2=",n2)
function2(10,20)
def function3(n1,n2):
    n3=n1+n2
    return n3
'''
#Categories of function
#Based on arguments
#1: Positional arguments
'''def function1(n1,n2,n3,n4):
    print("n1=",n1,"n2=",n2,"n3=",n3,"n4=",n4)
function1(1,2,3,4)
'''
#2: Keyword arguments
'''
def function1(n1,n2,n3,n4):
    print("n1=",n1,"n2=",n2,"n3=",n3,"n4=",n4)
function1(n1=10,n2=20,n3=30,n4=40)
'''
#default arguments
'''
def function2(name,rollno,branch,collegename="GIET"):
    print(name,rollno,branch,collegename)
function2("Ashish","01","CSE")
function2("Ayush","02","mech")
function2("Arya","03","CSE")
function2("Aman","04","ECE")
'''
#function overloading
def add(*var):
    sum1=0
    for i in var:
        sum1=sum1+i
    return(sum1)
print(add(10,20))
print(add(10,20,30))
print(add(10,20,30,40,50))














