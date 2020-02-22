cities = ["Adelaide", "Alice Springs", "Darwin", "Melbourne", "Sidney"]

with open('cities', 'w') as cityFile:
    for city in cities:
        print(city, file=cityFile)

cities = []
with open('cities', 'r') as cityFile:
    for city in cityFile:
        cities.append(city.strip('\n'))

print(cities)
for city in cities:
    print(city)

imelda = "More Mayhem", "Imelda May", "2011", {
    (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz")
}

with open("imelda", 'w') as imeldaFile:
    print(imelda, file=imeldaFile)

with open("imelda", 'r') as imeldaFile:
    contents = imeldaFile.readline()

imelda = eval(contents)
title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)