# Sample Input:

# 4
# lara@hackerrank.com
# brian-23@hackerrank.com
# britts_54@hackerrank.com
# abc@abc

# Sample output:

# ['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']
import re

def fun(s):
    pattern = r"[A-Za-z0-9\-\_]{1,}[\@][A-Za-z0-9]*\.[A-Za-z0-9]{0,3}"
    return bool(re.fullmatch(pattern, s))


def filter_mail(emails):
    return list(filter(fun, emails))


if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
