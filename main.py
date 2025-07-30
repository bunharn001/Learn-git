# This is grading program

input = int(input("Enter you grade: "))

if input >= 80:
    print("A")
elif input >= 75:
    print("B+")
elif input >= 70:
    print("B")
elif input >= 65:
    print("C+")
elif input >= 60:
    print("C")
elif input >= 55:
    print("D+")
elif input >= 50:
    print("D")
else:
    print("F")

print("Thank you for using the grading program!")