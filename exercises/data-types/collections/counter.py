# How much did Raghu earned form his shoes? 

# Sample Input

# 10
# 2 3 4 5 6 8 7 6 5 18
# 6
# 6 55
# 6 45
# 6 55
# 4 40
# 18 60
# 10 50

# Sample Output

# 200

from collections import Counter

if __name__ == '__main__':
    shoes_number = int(input())
    shoes_sizes = list(map(int, input().split()))
    customers_number = int(input())
    shoes_available = Counter(shoes_sizes)
    money_earned = 0

    for i in range(customers_number):
        customer = list(map(int, input().split()))
        if shoes_available[customer[0]] > 0:
            money_earned += customer[1]
            shoes_available[customer[0]] -= 1

    print(money_earned)
