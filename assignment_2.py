n=10
sm=(n*(n+1))/2
print("Sum of first 10 natural number: ",sm)

n=int(input("Enter a number "))
fac=1
for i in range(n,0,-1):
    fac*=i
print("Factorial:",fac)

n=int(input("Enter a number "))
a=0
b=1
print(a,end=" ")
print(b,end=" ")
for i in range(n-2):
    sum=a+b
    print(sum,end=" ")
    a=b
    b=sum

x=20
y=43
z=89
if(x>y and x>z):
    print("Max: ",x)
elif(y>x and y>z):
    print("Max: ",y)
else:
    print("Max: ",z)

##### Student Result System
name=input("Enter Name: ")
age=int(input("Enter Age: "))
roll_no=int(input("Enter your roll no:"))
marks=[]
for i in range(1,6,1):
    ele=float(input(f"Enter marks for subject {i} "))
    marks.append(ele)
per =0
for i in marks:
    per +=i
fpercen=per/5
print("----------Student Result -----------------")
print("Name: ",name)
print("Age: ",age)
print("Roll no: ",roll_no)
print("Marks: ",marks)
print("Grade: ",end=" ")
if(fpercen>=90):
    print("A")
elif(fpercen>=75):
    print("B")
elif(fpercen>=50):
    print("C")
else:
    print("D")
