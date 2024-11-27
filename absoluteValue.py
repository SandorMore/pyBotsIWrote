userInput = int(input("Write the number you want to have its absolute value: "))

def getAbs():
    global userInput
    if userInput > 0:
        print(userInput)
    else:
        userInput = userInput * -1
        print(userInput)

getAbs()

def findMedian(*nums):
    nums = list(nums)
    nums.sort()
    if len(nums) % 2 != 0:
        print("A lista páratlan hoszzú!")
    else:
        print("A list páros hosszú!")

    if len(nums) % 2 != 0:
        medianIfOdd = nums[int(len(nums) / 2)]
        print(medianIfOdd)
    elif len(nums) % 2 == 0:
        medianIfEven = (nums[int(len(nums) / 2)] + nums[(int(len(nums) / 2)) + 1]) / 2
        print(medianIfEven)


findMedian(1,2,3,4,5,6,7,8,11,22)