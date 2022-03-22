# Sample Input

# 9
# BANANA FRIES 12
# POTATO CHIPS 30
# APPLE JUICE 10
# CANDY 5
# APPLE JUICE 10
# CANDY 5
# CANDY 5
# CANDY 5
# POTATO CHIPS 30
# Sample Output

# BANANA FRIES 12
# POTATO CHIPS 60
# APPLE JUICE 20
# CANDY 20

from collections import OrderedDict

if __name__ == '__main__':
    items_sold = OrderedDict()

    for _ in range(int(input())):
        item_data = input().split()
        item_value = int(item_data.pop())
        item_name = " ".join(item_data)
        value_to_add = 0

        if items_sold.get(item_name) != None:
            value_to_add = items_sold[item_name]

        items_sold.update({item_name: value_to_add + item_value})

    for item in items_sold:
        print(item + " " + str(items_sold[item]))
