print("hello World")

input = int(input("Enter grade score: "))

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


input_Math = int(input("Enter Math grade score: "))
input_Sci = int(input("Enter Science grade score: "))
input_Eng = int(input("Enter English grade score: "))
input_Thai = int(input("Enter Thai grade score: "))
input_Soc = int(input("Enter Social grade score: "))

average = (input_Math + input_Sci + input_Eng + input_Thai + input_Soc) / 5
print("Average grade score:", average)

#it's done bro. it's done.