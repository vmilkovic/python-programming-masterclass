import time

print(time.gmtime(0))
print(time.localtime(time.time()))
print(time.time())

timeHere = time.localtime()
print(timeHere)
print("Year: ", timeHere[0], timeHere.tm_year)
print("Month: ", timeHere[1], timeHere.tm_mon)
print("Day: ", timeHere[2], timeHere.tm_mday)

from time import perf_counter as my_timer
import random

input("Press enter to start")

waitTime = random.randint(1, 6)
time.sleep(waitTime)
startTime = my_timer()

input("Press enter to stop")

print("=" * 30)

endTime = my_timer()

print("Started at " + time.strftime("%X", time.localtime(startTime)))
print("Ended at " + time.strftime("%X", time.localtime(endTime)))

print("Your reaction time was {} seconds".format(endTime - startTime))


print("The epoch on this system starts at " + time.strftime('%c', time.gmtime(0)))

print("The current timezone is {0} with an offset of {1}".format(time.tzname[0], time.timezone))

if time.daylight != 0:
    print("\tDaylight Saving Time is in effect for this location")
    print("\tThe DST timezone is " + time.tzname[1])

print("Local time is " + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
print("UTC time is " + time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()))
