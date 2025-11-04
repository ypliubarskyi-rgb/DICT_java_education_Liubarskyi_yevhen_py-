nameBot = "Zhora"
birth_year = "2025"
print(f"Hello my name is {nameBot}")
print(f"I was created in {birth_year}.")

NameUser = input("Please, remind me your name \n")
print(f"What a great name you have,{NameUser}!")

print("Let me guess your age.")
print("Enter remainders of dividing your age by 3, 5 and 7..")

remainder3 = int(input("Enter remainder of dividing your age by 3: "))
remainder5 = int(input("Enter remainder of dividing your age by 5: "))
remainder7 = int(input("Enter remainder of dividing your age by 7: "))

age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105

print(f"Your age is {age}.\n "  f"that's a good time to start programming!")

print("Now I will prove to you that I can count to any number you want.")
n = int(input("Enter :"))
i=0
while i<n:
    i+=1
print(f"{i}!")
print("Completed, have a nice day!")

print("Let's test your programming knowledge.")
print("Why do we use methods?")
print("1. To repeat a statement multiple times.")
print("2. To decompose a program into several small subroutines.")
print("3. To determine the execution time of a program.")
print("4. To interrupt the execution of a program.")

while(True):
    print("Answer")
    Answer = input("Enter your answer: ").strip()
    if Answer == "":
        print("You must enter something!")
    elif Answer == "2":
        print("Nice one!")
        break
    else:
        print("Try again!.")
print("Congratulations, have a nice day!")