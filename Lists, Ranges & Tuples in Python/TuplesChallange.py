# Given the tuple below that represents the Imelda May track "More Mayhem", write
# code to print the album details, follow by a list of all the tracks in the album.
#
# Indent the tracks by a single tab stop when printing them (remember that you can pass
# more than one item to the print function, spreading them with a come).

imelda = "More Mayhem", "Imelda May", 2011, \
         ((1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))

title, artist, year, tracks = imelda

print(title)
print(artist)
print(year)

for song in tracks:
    track, title = song
    print("\tTrack number {}, Title: {}".format(track, title))
