jabber = open('sample', 'r')

for line in jabber:
    if "jabberwock" in line.lower():
        print(line, end="")

jabber.close()

with open('sample', 'r') as jabber:
    for line in jabber:
        if "JAB" in line.upper():
            print(line, end="")

with open('sample', 'r') as jabber:
    line = jabber.readline()
    while line:
        print(line, end='')
        line = jabber.readline()

with open('sample', 'r') as jabber:
    lines = jabber.readlines()
    print(lines)

for line in lines:
    print(line, end='')

for line in lines[::-1]:
    print(line, end='')

with open('sample', 'r') as jabber:
    lines = jabber.read()

for line in lines:
    print(line, end='')

for line in lines[::-1]:
    print(line, end='')