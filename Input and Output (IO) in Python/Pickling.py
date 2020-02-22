import pickle

imelda = ('More Mayhem',
          'Imelda may',
          '2011',
          ((1, 'Pulling the Rug'),
           (2, 'Psycho'),
           (3, 'Mayhem'),
           (4, 'Kentish Town Waltz')))

with open('imelda.pickle', 'wb') as pickleFile:
    pickle.dump(imelda, pickleFile)

with open('imelda.pickle', 'rb') as imeldaPickle:
    imeldaBinary = pickle.load(imeldaPickle)

print(imeldaBinary)

album, artist, year, trackList = imeldaBinary

print(album)
print(artist)
print(year)

for track in trackList:
    trackNumber, trackTitle = track
    print(trackNumber, trackTitle)

imelda = ('More Mayhem',
          'Imelda may',
          '2011',
          ((1, 'Pulling the Rug'),
           (2, 'Psycho'),
           (3, 'Mayhem'),
           (4, 'Kentish Town Waltz')))

even = list(range(0, 10, 2))
odd = list(range(1, 10, 2))

with open('imelda.pickle', 'wb') as pickleFile:
    pickle.dump(imelda, pickleFile, protocol=pickle.HIGHEST_PROTOCOL)
    pickle.dump(even, pickleFile, protocol=0)
    pickle.dump(odd, pickleFile, protocol=pickle.DEFAULT_PROTOCOL)
    pickle.dump(2998302, pickleFile, protocol=pickle.DEFAULT_PROTOCOL)

with open('imelda.pickle', 'rb') as imeldaPickle:
    imeldaBinary = pickle.load(imeldaPickle)
    evenList = pickle.load(imeldaPickle)
    oddList = pickle.load(imeldaPickle)
    x = pickle.load(imeldaPickle)

print(imeldaBinary)

album, artist, year, trackList = imeldaBinary

print(album)
print(artist)
print(year)

for track in trackList:
    trackNumber, trackTitle = track
    print(trackNumber, trackTitle)

print('=' * 40)

for i in evenList:
    print(i)

print('=' * 40)

for i in oddList:
    print(i)

print('=' * 40)

print(x)

print('=' * 40)

# pickle.loads(b"cos\nsystem\n(S'rm imelda.pickle'\ntR.") 