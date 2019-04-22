import time
from time import time as my_time

# montonic -> time cannot go backwards
from time import monotonic as my_mono


# process_time -> time the CPU spends running a current process rather than the elapsed time
from time import process_time as process_timer


# perf_counter is the most accurate timer, can also use monotonic
from time import perf_counter as my_timer

import random

input("Press enter to start: ")
wait_time = random.randint(1, 6)
# .sleep() Delay execution for a given number of seconds.
time.sleep(wait_time)
start_time = my_timer()

input("Press enter to stop: ")
end_Time = my_timer()

# .strftime() - String from time, formats time to a more readable form from the tuple
print("Started at " + time.strftime("%X", time.localtime(start_time)))
print("Ended at " + time.strftime("%X", time.localtime(end_Time)))

print("Your reation time was {}".format((end_Time - start_time)))

# Guide
# Actual Elapsed time -> perf_counter
# CPU time -> process_time
# Real time -> time
