t = "a", "b", "c"
print(t)

print("a", "b", "c")
print(("a", "b", "c"))

welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the Lightning", "Metallica", 1984

print(metallica)
print(metallica[0])
print(metallica[1])
print(metallica[2])

# metallica[0] = "Master of puppets"
imelda = imelda[0], "Imelda May", imelda[2]
print(imelda)

newMetallica = ["Ride the Lightning", "Metallica", 1984]
print(newMetallica)
newMetallica[0] = "Master of Puppets"
print(newMetallica)

# right side is evaluated first
a = b = c = d = 12
print(c)

a, b = 12, 13
print(a, b)

a, b = b, a
print("a is {}".format(a))
print("b is {}".format(b))

title, artist, year = imelda
print(title)
print(artist)
print(year)

newMetallica.append("Rock")
title, artist, year, genre = newMetallica
print(title)
print(artist)
print(year)
print(genre)

imelda = "More Mayhem", "Imelda May", 2011, \
         (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz")

print(imelda)
title, artist, years, track1, track2, track3, track4 = imelda
print(title)
print(artist)
print(years)
print(track1)
print(track2)
print(track3)
print(track4)


