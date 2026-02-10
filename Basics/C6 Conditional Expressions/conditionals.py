age = int(input("Enter age: "))
marks = int(input("Enter marks: "))

if age >= 18 and marks >= 40:
    print("Eligible")
elif age < 18 or marks < 40:
    print("Not eligible")