name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")
maths = float(input("Enter Maths Marks: "))
science = float(input("Enter Science Marks: "))
english = float(input("Enter English Marks: "))
total = maths + science + english
percentage = total / 3
print()
print("----- Student Report -----")
print("Name of the Student:", name)
print("Roll Number of the Student:", roll_no)
print("Total Marks :", total)
print("Percentage :", percentage, "%")