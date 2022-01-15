def swap_case(s):
    swapped_s = ''

    for letter in s:
        swapped_s += letter.lower() if letter.isupper() else letter.upper()

    return swapped_s


if __name__ == '__main__':
    s = raw_input()
    result = swap_case(s)
    print(result)
