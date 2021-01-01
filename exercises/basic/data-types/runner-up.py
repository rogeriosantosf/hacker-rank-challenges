if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    winner = max(arr)
    runner_up = 0

    for i in reversed(range(len(arr))):
        if arr[i] < winner:
            runner_up = arr[i]
            break

    print(runner_up)
