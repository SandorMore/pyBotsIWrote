sum = 0
userNumberInput = int(input("Write the number you want to add up every number until."))
for i in range(userNumberInput + 1):

    sum += i

print(sum)