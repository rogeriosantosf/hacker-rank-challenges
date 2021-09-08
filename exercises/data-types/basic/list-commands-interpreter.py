# Sample Input 0

# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print
# Sample Output 0

# [6, 5, 10]
# [1, 5, 9, 10]
# [9, 5, 1]

class Command():
    def __init__(self, command_type, arguments_number):
        self.command_type = command_type
        self.arguments_number = arguments_number


commands_info = {
    "insert": Command("collection", 2),
    "remove": Command("collection", 1),
    "append": Command("collection", 1),
    "sort": Command("collection", 0),
    "pop": Command("collection", 0),
    "reverse": Command("collection", 0),
    "print": Command("runtime", 0)
}


def execute_command(command_text, collection):
    args = command_text.split()
    command_name = args[0]
    args.remove(command_name)
    command = commands_info[command_name]
    if command.command_type == "collection":
        fn = getattr(collection, command_name)
        fn(*map(int, args))
    else:
        print(collection)


if __name__ == '__main__':
    N = int(input())
    collection = []
    for _ in range(N):
        execute_command(input(), collection)
