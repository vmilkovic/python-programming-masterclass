# Create a list of items (you may use either strings or numbers in the list),
# then create an iterator using the iter() function
#
# Use a loop to loop "n" times, where n is the number of items in your list,
# Each time round the loop, use next() on your list to print the next item.
#
# hint: use the len() function rather then counting the number of items in the list.

days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

myIterator = iter(days)

for n in range(0, len(days)):
    nextItem = next(myIterator)
    print(nextItem)
