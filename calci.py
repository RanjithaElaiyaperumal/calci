a=int(input("Enter your num:"))
b=int(input("Enter your num:"))
print("1,Addition:")
print("2,Subtraction:")
print("3,Multiplication:")
print("4,division:")
choice=int(input())
if(choice==1):
    c=a+b
    print(c)
if(choice==2):
    c=a-b
    print(c)
if(choice==3):
    c=a*b
    print(c)
if(choice==4):
    c=a/b
    print(c)
if(choice==5):
    print("Enter correct value:")