# Good morning! Here's your coding interview problem for today.

# This problem was asked by Uber.

# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

# Follow-up: what if you can't use division?

# O(N) time | O(N) space

def product_array(arr):
    # [0, 0, 0]
    left_arr = [0 for x in arr]
    # [0, 0, 0]
    right_arr = [0 for x in arr]

    left_product = 1

    # [3, 2, 1]
    for i in range(len(arr)):
        # left_arr[0] = 1
        # left_arr[1] = 3
        # left_arr[2] = 6
        left_arr[i] = left_product
        # left_product = 1 * 3
        # left_product = 3 * 2 
        # left_product = 6 * 1
        left_product *= arr[i]

    print('Left array: ', left_arr)
    
    right_product = 1

    # [3, 2, 1]
    # starting from len(arr) - 1 
    # len(arr) = 3
    # len(arr) - 1  = 2
    for i in range(len(arr)-1, -1, -1):
        # right_arr[2] = 1; [0, 0, 1]
        # right_arr[1] = 1; [0, 1, 1]
        # right_arr[0] = 2; [2, 1, 1]
        right_arr[i] = right_product
        # right_product = 1 * 1
        # right_product = arr[1] * 1 = 2 * 1 = 2
        # right_product = arr[0] * 2 = 3 * 2 = 6
        right_product *= arr[i]
    
    print('Right array: ', right_arr)
    
    result = [0 for x in arr]

    # left_arr = [1, 3, 6]
    # right_arr = [2, 1, 1]
    for i in range(len(arr)):
        arr[i] = left_arr[i] * right_arr[i]

    return arr

if __name__ == "__main__":
    arr = [3,2,1]
    result = product_array(arr)
    print(result)
    arr = [1, 2, 3, 4, 5]
    result = product_array(arr)
    print(result)