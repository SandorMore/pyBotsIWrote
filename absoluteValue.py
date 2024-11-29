import statistics

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
    n = len(nums)
    if n % 2 == 1:
        print(nums[n // 2])
    else:
        i = n // 2
        print((nums[i - 1] + nums[i]) / 2)

findMedian(1,2,3,4,5,6,7,8,11,22,21,33,12,36,2.3,4.4,3.6,4.2, 11.7,42, 55, 6.5, 22.4, 7.7)
listcheck = [1,2,3,4,5,6,7,8,11,22,21,33,12,36,2.3,4.4,3.6,4.2, 11.7,42, 55, 6.5, 22.4,7.7]
print(statistics.median(listcheck))