import pytz
import datetime

# pytz timezone database is maintained by the
# IANA -> internet assigned names authority
# Example of pytz
country = 'Europe/Moscow'

tz_to_display = pytz.timezone(country)
local_time = datetime.datetime.now(tz=tz_to_display)
print("The time in {} is {}".format(country, local_time))
print("UTC is {}".format(datetime.datetime.utcnow()))

# All timezones
# pytz is a library useful for converting UTC to local time
for x in pytz.all_timezones:
    print(x)

# All countries in pytz Acronym -> Full country name
for x in sorted(pytz.country_names):
    print(x + ": " + pytz.country_names[x])

# Note that a country can have several timezones
# Acronym, country name, and dictionary value list
for x in sorted(pytz.country_names):
    print("{}: {}: {}".format(x, pytz.country_names[x], pytz.country_timezones.get(x)))

# Example -> checking if timezone is defined for a country

for x in sorted(pytz.country_names):
    print("{}: {}".format(x, pytz.country_names[x]), end=': ')
    if x in pytz.country_timezones:
        for zone in sorted(pytz.country_timezones[x]):
            tz_to_display = pytz.timezone(zone)
            local_time = datetime.datetime.now(tz=tz_to_display)
            print("\t\t{}: {}".format(zone, local_time))
    else:
        print("No time zone defined")
