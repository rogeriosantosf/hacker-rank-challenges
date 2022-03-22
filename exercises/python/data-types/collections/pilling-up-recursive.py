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


def is_stackable(cubes, stackable=False, cube=None):
    if cube == None:
        cube = grab_a_cube(cubes)

    next_cube = grab_a_cube(cubes)

    while cube == next_cube and len(cubes) > 0:
        stackable = True
        next_cube = grab_a_cube(cubes)

    if cube > next_cube and len(cubes) > 0:
        stackable = True
        return is_stackable(cubes, stackable, next_cube)
    elif cube < next_cube:
        stackable = False

    return stackable


if __name__ == '__main__':
    cases_number = int(input())
    for i in range(cases_number):
        cubes_number = int(input())
        d = deque(map(int, input().split()))
        try:
            print("Yes" if is_stackable(d) or cubes_number == 2 else "No")
        except RuntimeError as e:
            print(e.message)
