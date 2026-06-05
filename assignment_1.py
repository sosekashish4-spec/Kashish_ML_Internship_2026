len=float(input("Enter length: "))
bre=float(input("Enter breadth: "))
area=len*bre
print("Area of Rectangle : ",area)

amt=float(input("Enter Principle amount: "))
rate=float(input("Enter Rate: "))
time=float(input("Enter No. of years: "))
si=amt*rate*time
print("Simple Interest : ",si)

temp=float(input("Enter temperature(degree C )"))
f_temp=(temp*1.8)+32
print("Temperature(degree F ): ",f_temp)

a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
c=int(input("Enter 3rd number: "))
avr=(a+b+c)/3
print("Average: ",avr)

num=int(input("Enter a number: "))
pow=1
for i in range(1,2,1):
    pow*=num
print("Square:",pow)
print("Cube: ",pow*num)

a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
print("a: ",a," b: ",b)
a=a+b
b=a-b
a=a-b
print("a: ",a," b: ",b)

 
print("-------------Student Report Portal----------------")
name=input("Name: ")
age=int(input("Age: "))
roll_no=int(input("Roll no: "))
course=input("Course: ")
sub1=int(input("English Marks: "))
sub2=int(input("Hindi Marks: "))
sub3=int(input("Mathmatics Marks: "))
sub4=int(input("Science Marks: "))
sub5=int(input("Arts Marks: "))
total=(sub1+sub2+sub3+sub4+sub5)
percen=total/5
print("Percentage: ",percen,"%")