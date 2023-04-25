# Good morning! Here's your coding interview problem for today.

# This problem was asked by Stripe.

# Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

# O(n) time | O(1) space
def first_missing_positive(arr):
    i = 0
    while i < len(arr):
        j = arr[i] - 1
        # if the current value is not in it's correct index position
        # swap positions
        if arr[i] > 0 and arr[i] != arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            i += 1
        
    for i in range(len(arr)):
        if arr[i] != i + 1:
            return i + 1
    return -1


if __name__ == "__main__":
    arr = [3, 4, -1, 1]
    result = first_missing_positive(arr)
    print(result)

    arr = [1, 2, 0]
    result = first_missing_positive(arr)
    print(result)

