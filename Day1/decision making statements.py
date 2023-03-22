#Decision making statements
#read a number
#multiple 3
#multiple 5
num=int(input("Enter the number:"))
if(num%3==0 and num%5==0):
    print("The number is divisible by 3 and 5")
elif(num%3==0):
    print("The number is divisible by 3")
elif(num%5==0):
    print("The number is divisible by 5")
else:
    print("Invalid input")
