def add(n):
    return (n*(n+1))/2
val=add(10)
print("Sum:",val)

def add(n):
    return (n*(n+1))/2
value=int(input("Enter number: "))
print("Sum of first",value,"numbers: ",add(value))

def rev(num):
    sum=0
    while(num>0):
        m=num%10
        sum+=m
        num//=10
        sum*=10
    return sum/10
print("Reverse: ",rev(239845))

def dig(numb):
    count=0
    while(numb>0):
        k=numb%10
        count+=1
        numb//=10
    return count
print("No.of digits: ",dig(2349758))

def palindrome(n):
    if(str(n)==str(n)[::-1]):
        return True
    return False
print(palindrome(1345))
print(palindrome(11211))

def fib(m):
    a=0
    b=1
    print(a,end=" ")
    print(b,end=" ")
    while(m-2!=0):
            sum=a+b
            print(sum,end=" ")
            a=b
            b=sum
            m-=1
fib(7) 
print()

def calculator(a,b,opern):
    if(opern=="+"):
         return a+b;
    elif(opern=="%"):
         return a%b
    elif(opern=="-"):
         return a-b
    elif(opern=="/"):
         return a/b
    elif(opern=="//"):
         return a//b
    else:
         return a*b
a=int(input("Enter a: "))
opern=input("Enter calculator Operation: ")
b=int(input("Enter b: "))
print(a,opern,b,"=",calculator(a,b,opern))

with open("text.txt","w") as f:
    f.write("Name:Neha\n")
    f.write("Age:20\n")
    f.write("Course:BTech\n")
    f.write("City:Delhi\n")

with open("text.txt","r") as f:
     data=f.read()
print(data)

dividend=int(input("Enter Dividend: "))
divisor=int(input("Enter divisor: "))
try:
     ans=dividend//divisor
     print("Quotient: ",ans)
except ZeroDivisionError:
     print("Enter valid Divisor")
finally:
     print("Program Completed")

class Student:
    name="Priya"
    city="Jaipur"
student1=Student()
print(student1.name)
print(student1.city)