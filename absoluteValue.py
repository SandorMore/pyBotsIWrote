userInput = int(input("Write the number you want to have its absolute value: "))

def getAbs():
    global userInput
    if userInput > 0:
        return userInput
    else:
        return userInput * -1

getAbs()