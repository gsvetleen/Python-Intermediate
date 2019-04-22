import time

# epoch
print(time.gmtime(0))

# local time
print(time.localtime())

# number of seconds since the start of the epoch
print(time.time())

# Example 1 -> formatting the time tuple
time_here = time.localtime()
print(time_here)
# Parameter 1 & 2 should be the same
print("Year:",time_here[0],time_here.tm_year)
print("Month:",time_here[1],time_here.tm_mon)
print("Day:",time_here[2],time_here.tm_mday)