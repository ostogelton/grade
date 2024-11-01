name = input("Name: ")
math = float(input("Math: "))
english = float(input("English: "))
science = float(input("Science: "))
filipino = float(input("Filipino: "))


result = (math + english + science + filipino)/4

if result > 100 or result <= 50:
    print("Invalid grade" + str(result))
    exit()
    print("hello")
elif result >= 98:
    print("With Highest Honor" + str(result))
elif result >= 95:
    print("With Higher Honor" + str(result))
elif result >= 90:
    print("With High Honor" + str(result))
elif result >= 75:
    print("Passed" + str(result))
else:
    print("Failed" + str(result))