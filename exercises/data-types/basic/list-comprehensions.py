[print([i, j, k]) for i in [0, 1] for j in [0, 1] for k in [0, 1]]


def print__cuboid__without__sum(x, y, z, n):
    results = []

    for i in range(x + 1):
        for j in range(y + 1):
            for k in range(z + 1):
                if i + j + k != n:
                    results.append([i, j, k])

    print(results)
