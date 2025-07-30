# This is grading program

input = int(input("Enter you grade: "))

if input >= 80:
    print(f"Your grade is A and your score is {input}")
elif input >= 75:
    print(f"Your grade is B+ and your score is {input}")
elif input >= 70:
    print(f"Your grade is B and your score is {input}")
elif input >= 65:
    print(f"Your grade is C+ and your score is {input}")
elif input >= 60:
    print(f"Your grade is C and your score is {input}")
elif input >= 55:
    print(f"Your grade is D+ and your score is {input}")
elif input >= 50:
    print(f"Your grade is D and your score is {input}")
else:
    print(f"Your grade is F and your score is {input}")

print("Thank you for using the grading program!")
