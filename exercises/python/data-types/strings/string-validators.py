# Input Format

# A single line containing a string .

# Constraints


# Output Format

# In the first line, print True if has any alphanumeric characters. Otherwise, print False.
# In the second line, print True if has any alphabetical characters. Otherwise, print False.
# In the third line, print True if has any digits. Otherwise, print False.
# In the fourth line, print True if has any lowercase characters. Otherwise, print False.
# In the fifth line, print True if has any uppercase characters. Otherwise, print False.

# Sample Input

# qA2
# Sample Output

# True
# True
# True
# True
# True

if __name__ == '__main__':
    s = input()
    print(True if any([l for l in s if l.isalnum()]) else False)
    print(True if any([l for l in s if l.isalpha()]) else False)
    print(True if any([l for l in s if l.isdigit()]) else False)
    print(True if any([l for l in s if l.islower()]) else False)
    print(True if any([l for l in s if l.isupper()]) else False)
