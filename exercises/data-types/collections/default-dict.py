# In this challenge, you will be given 2 integers, m and n. 
# There are n words, which might repeat, in word group A. 
# There are m words belonging to word group B. 
# For each m words, check whether the word has appeared in group A or not. 
# Print the indices of each occurrence of m in group A. 
# If it does not appear, print -1.

from collections import defaultdict

if __name__ == '__main__':
    n, m = map(int, input().split())
    groups = defaultdict(list)

    for _ in range(n):
        groups['A'].append(input())

    for _ in range(m):
        groups['B'].append(input())

    for letter in groups['B']:
        if letter in groups['A']:
            occur = []
            for i in range(len(groups['A'])):
                if groups['A'][i] == letter:
                    occur.append(i + 1)
            print(" ".join(map(str, occur)))
        else:
            print("-1")
