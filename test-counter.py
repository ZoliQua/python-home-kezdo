import time
from datetime import datetime


def TimeNow(str_now, name_of_script, start_time=False):
	now = datetime.now()
	time_abb = now.strftime("%Y-%m-%d - %H:%M:%S (%f)")
	print(f"Runtime of '{name_of_script}' is at {str_now} phase at {time_abb}")

	if str_now == "end":
		runtime = time.time() - start_time
		hours = runtime // 3600
		temp = runtime - 3600 * hours
		minutes = temp // 60
		seconds = temp - 60 * minutes

		print(f"Runtime of '{name_of_script}' was", '%d hours %d minutes %d seconds' % (hours, minutes, seconds),
			"(" + str(float("{:.5f}".format(runtime))) + ")")

	return True


# Print start time to the console
start_time = time.time()
TimeNow("start", "test-counter.py")

x = 0
while x < 1000000000:
	x += 1
print('Done')

# Print end time to the console
TimeNow("end", "test-counter.py", start_time)
