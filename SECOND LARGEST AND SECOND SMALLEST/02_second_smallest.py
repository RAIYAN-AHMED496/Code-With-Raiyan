# FOR A LIST FIND THE SECOND SMALLEST ELEMENT
# AT FIRST LET'S SEE THE CLEVER SOLUTION . THIS SOLUTION MAKES YOU SMARTER AND HAPPIER
l = [44, 11, 83, 29, 25, 76, 88]
nums = sorted(l)
print("Second smallest number is: ", nums[1])

# LET'S SEE A HARDER CODE
def get_second_smallest(nums):
    smallest = float('inf')
    second_smallest = float('inf')
    for i in range(0, len(nums)):
        if nums[i] <= smallest:
            second_smallest = smallest
            smallest = nums[i]
        elif nums[i] < second_smallest:
            second_smallest = nums[i]
    return second_smallest
my_nums = [44, 11, 83, 29, 25, 76, 88]
second_smallest = get_second_smallest(my_nums)
print("Second smallest number is: ", second_smallest)

# LET'S SEE ANOTHER CLEVET SOLUTION
nums = [2, 15, 14, 71, 52, 209, 551]
nums.remove(min(nums))

second_smallest = min(nums)
print("Second smallest number is: ", second_smallest)