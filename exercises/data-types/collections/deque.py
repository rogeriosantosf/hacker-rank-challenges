# Given an set of operations and values, execute the operations with the 
# values and print the resultant deque
# 
# Sample Input

# 6
# append 1
# append 2
# append 3
# appendleft 4
# pop
# popleft
# Sample Output

# 1 2

from collections import deque

if __name__ == '__main__':
    d = deque()
    for _ in range(int(input())):
        operation = input()

        if " " in operation:
            operation, value = operation.split()
            getattr(d, operation)(value)
        else:
            getattr(d, operation)()

    print(" ".join(d))
