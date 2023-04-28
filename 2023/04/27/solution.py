# Good morning! Here's your coding interview problem for today.

# This problem was asked by Facebook.

# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

# You can assume that the messages are decodable. For example, '001' is not allowed.

def decode_ways(s):
    # [0, 0, 0, 0]
    dp = [0 for x in range(len(s)+1)]
    # [1, 0, 0, 0]
    dp[0] = 1
    # [1, 1, 0, 0]
    dp[1] = 0 if s[0] == '0' else 1

    
    for i in range(2, len(dp)):
        # s[1] = 2
        # 2 != '0'

        # s[2] = 6
        if s[i-1] != '0':
            # dp[2] = dp[1]
            # [1, 1, 1, 0]

            # dp[3] = dp[2]
            # dp[3] = 2
            # [1, 1, 2, 2]
            dp[i] = dp[i-1]
        
        # int(s[0:2]) = 22
        # int(s[1:3]) = 26
        two_digit = int(s[i-2:i])
        if two_digit >= 10 and two_digit <= 26:
            # dp[2] += dp[0] 
            # dp[2] += 1
            # [1, 1, 2, 0]

            # dp[3] += dp[1]
            # dp[3] += 1
            # [1, 1, 2, 3]
            dp[i] += dp[i-2]
    
    return dp[len(s)]

if __name__ == "__main__":
    s = "12"
    print(decode_ways(s)) 
    s = "226"
    print(decode_ways(s)) 
