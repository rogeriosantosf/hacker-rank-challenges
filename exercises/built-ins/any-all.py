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
    def is_palindromic(value): return value == value[::-1]
    def is_positive_int(value): return int(value) > 0
    msg = "True" if any(map(is_palindromic, numbers)) and all(
        map(is_positive_int, numbers)) else "False"
    print(msg)
