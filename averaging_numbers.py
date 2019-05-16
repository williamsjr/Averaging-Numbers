#Write a program that will compute the average of a series of numbers entered by the user.
#To make the program more user-friendly, store all of the numbers in a list so that the user's numbers can be displayed again before the average.
#Have your program stop accepting values when the user enters the value -999. Note that this value, -999, should not be averaged in with the other numbers.

user_nums = []
count = 0
sum_num = 0.0
nums = input("Enter a number ('q' will exit) ")

while nums != 'q':
    user_nums.append(nums)
    sum_num += int(nums)
    nums = input("Enter a number ('q' will exit) ")
    
if len(user_nums) != 0:
    average = sum_num / len(user_nums)

    #display the numbers
    print("Using the numbers: ")
    
    for i in range(len(user_nums)):
        print(user_nums[i], end = " ")
    #display the average
    print("\nThe average of those numbers is: ", average)
