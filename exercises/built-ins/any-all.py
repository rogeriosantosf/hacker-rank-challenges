# Sample Input
# 5
# 12 9 61 5 14

# Sample Output
# True

# Explanation
# Condition 1: All the integers in the list are positive.
# Condition 2: 5 is a palindromic integer.
# Hence, the output is True.

if __name__ == '__main__':
    count, numbers = input(), input().split()
    print("True" if any(map(lambda value: value == value[::-1], numbers)) and all(
        map(lambda value: int(value) > 0, numbers)) else "False")
