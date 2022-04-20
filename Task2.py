#Task 2

#Numbers = [5, 2, 7, 10, 1]


Numbers = []

UserInput = input(" Enter a random list of numbers with a space between them ")
print("\n")

UserNumbers = UserInput.split()

print("Numbers: ", UserNumbers)

for i in range(len(UserNumbers)):
    UserNumbers[i] = int(UserNumbers[i])


UserNumbers.sort()

print("Sorted numbers: ", UserNumbers)





#using append method?






