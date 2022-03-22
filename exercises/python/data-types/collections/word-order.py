# Given a set of words, prints the number of distinct words and its occurrences

# Sample Input

# 4
# bcdef
# abcdefg
# bcde
# bcdef

# Sample Output

# 3
# 2 1 1

from collections import Counter

if __name__ == '__main__':
    words = []
    counter_values = []

    for i in range(int(input())):
        words.append(input())

    word_counter = Counter(words)

    for word in word_counter:
        counter_values.append(str(word_counter[word]))

    print(len(word_counter))
    print(" ".join(counter_values))
