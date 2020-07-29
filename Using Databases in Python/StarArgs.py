def average(*args):
    print(type(args))
    print("args is {}:".format(args))
    print("*args is:", *args)
    mean = 0
    for arg in args:
        mean += arg
    return mean / len(args)


print(average(1, 2, 3, 4))


def build_tuple(*args):
    return args


print(build_tuple("hello", "planet", "earth", "take", "me", "to", "your", "leader"))
print(build_tuple(1, 2, 4, 5))


def print_backwards(*args, **kwargs):
    end_character = kwargs.pop('end', '\n')
    sep_character = kwargs.pop('sep', ' ')
    for word in args[:0:-1]:  # change the range
        print(word[::-1], end=sep_character,  **kwargs)
    print(args[0][::-1], end=end_character, **kwargs)  # and print the first word separately


def backwards_print(*args, **kwargs):
    set_character = kwargs.pop('sep', ' ')
    print(set_character.join(word[::-1] for word in args[::-1]), **kwargs)


with open("backwards.txt", 'w') as backwards:
    print_backwards("hello", "planet", "earth", "take", "me", "to", "your", "leader", file=backwards, end='\n')

print_backwards("hello", "planet", "earth", "take", "me", "to", "your", "leader", end='', sep='\n**\n')

