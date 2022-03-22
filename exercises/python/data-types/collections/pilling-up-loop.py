# Given a number of linear cubes with it's size lengths, 
# print if you can stack the cubes by grabing the rightmost or leftmost each time
# print 'Yes' if you can pile the cubes or 'No' otherwise

# Sample Input

# 2
# 4
# 4 3 2 4
# 3
# 3 2 1

# Sample Output

# Yes
# No

from collections import deque

def grab_a_cube(cubes):
    if len(cubes) == 1:
        return cubes.pop()
    else:
        leftmost = cubes.popleft()
        rightmost = cubes.pop()
        if leftmost > rightmost:
            cubes.append(rightmost)
            return leftmost
        else:
            cubes.appendleft(leftmost)
            return rightmost


def is_stackable(cubes):
    stackable = False
    cube = grab_a_cube(cubes)

    for i in range(len(cubes)):
        next_cube = grab_a_cube(cubes)
        if cube >= next_cube:
            stackable = True
            cube = next_cube
        else:
            stackable = False
            break

    return stackable


if __name__ == '__main__':
    cases_number = int(input())
    for i in range(cases_number):
        cubes_number = int(input())
        d = deque(map(int, input().split()))
        try:
            print("Yes" if is_stackable(d) else "No")
        except RuntimeError as e:
            print(e.message)
