# Good morning! Here's your coding interview problem for today.

# This problem was asked by Airbnb.

# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

# Follow-up: Can you do this in O(N) time and constant space?


# O(n) time | O(n) space
def max_sum_non_adjacent(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    maxSum = nums[:]
    maxSum[1] = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        maxSum[i] = max(maxSum[i - 1], maxSum[i - 2] + nums[i])
    return maxSum[-1]


# O(n) time | O(1) space
def max_sum_non_adjacent_opt(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    first = nums[0]
    second = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        curr = max(second, first + nums[i])
        first = second
        second = curr
    return second


if __name__ == "__main__":
    nums = [2, 4, 6, 2, 5]
    print(max_sum_non_adjacent(nums))
    nums = [5, 1, 1, 5]
    print(max_sum_non_adjacent(nums))
    nums = [2, 4, 6, 2, 5]
    print(max_sum_non_adjacent_opt(nums))
    nums = [5, 1, 1, 5]
    print(max_sum_non_adjacent_opt(nums))
