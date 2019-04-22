import timeExample

# %c -> locale's appropriate date and time representation
print("The epoch on this system starts at " + timeExample.
      strftime('%c', timeExample.gmtime(0)))

print("The current timezone is {0} with an offset of {1}".format(
    timeExample.tzname[0], timeExample.timezone))

if timeExample.daylight != 0:
    print("\t Daylight Saving Time is in effect for this location")
    print("\t The DST timezone is " + timeExample.tzname[1])

print("Local time is " + timeExample.strftime('%Y-%m-%d %H:%M:%S', timeExample.localtime()))
print("UTC time is " + timeExample.strftime('%Y-%m-%d %H:%M:%S', timeExample.gmtime()))
