# Good morning! Here's your coding interview problem for today.

# This problem was recently asked by Google.

# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

# Bonus: Can you do this in one pass?

# O(N) time | O(1) space
def add_up_to_k(arr, k):
    start, end = 0, len(arr) - 1
    while start <= end:
        target = arr[start] + arr[end]
        if target == k:
            return True, [arr[start], arr[end]]
        else:
            return False, [-1, -1]

if __name__ == "__main__":
    arr = [10, 15, 3, 7]
    k = 17
    print(str(add_up_to_k(arr, k)))

