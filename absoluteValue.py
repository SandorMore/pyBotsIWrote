userInput = int(input("Write the number you want to have its absolute value: "))

def getAbs():
    global userInput
    if userInput > 0:
        print(userInput)
    else:
        userInput = userInput * -1
        print(userInput)

getAbs()

def findMedian(nums = []):
    nums.sort()
    if nums.lenth % 2 != 0:
        print("A lista páratlan hoszzú!")
    else:
        print("A list a páros hosszú!")