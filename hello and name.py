# This program says hello and asks for my name.

print("Hello, world")
print()  # creates a space below hello world before asking name
print("What is your name?")  # asks for your name
myName = input()
print("It's good to meet you, " + myName)
print("Thelength of your name is:")
print(len(myName))
print("What is your age?")  # asks your age
myAge = input()
print("You will be " + str(int(myAge) + 1) + " in a year.")

print("I'm " + str(31) + " years old")  # use str to add numbers into the line
