# FOR A LIST FIND THE SECOND LARGEST NUMBER IN THE LIST
def get_second_largest(nums):
    largest = nums[0]
    second_largest = nums[0]
    for i in range(1, len(nums)):
        if nums[i] > largest:
            second_largest = largest
            largest = nums[i]
        elif nums[i] > second_largest:
            second_largest = nums[i]
    return second_largest
my_nums = [44, 11, 83, 29, 25, 76, 88]
second_largest = get_second_largest(my_nums)
print("Second largest number of this list is: ", second_largest)
# THIS CODE IS MUCH HARDER TO UNDERSTAND


## BUT LET'S SEE A CLEVER SOLUTION

nums = [44, 11, 83, 29, 25, 76, 88]
nums.remove(max(nums))
second_largest = max(nums)
print("Second largest number of this list is: ", second_largest)
# It is a clever solution right!

# LET'S SEE ANOTHER SOLUTION
nums = [44, 11, 83, 29, 25, 76, 88]
sorted_nums = sorted(nums)
print(sorted_nums)
print(sorted_nums[-2])
# This is also a cool solution

# LET'S SEE A ADVANCE SOULTION
nums = [44, 11, 83, 29, 25, 76, 88]
nums.sort(reverse=True)
print(nums[1])
## hlw how are you 


