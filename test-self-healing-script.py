import time
import traceback

def task(start_index):
    for i in range(start_index, 100):
        print(f"Processing {i}")
        if i == 42:
            raise Exception("Boom!")  # Simulate a failure
        time.sleep(0.5)

def run_resilient_task():
    last_index = 0
    while last_index < 100:
        try:
            task(last_index)
            break
        except Exception as e:
            print("Error occurred:", e)
            print(traceback.format_exc())
            last_index += 1
            time.sleep(1)  # cool down and retry

run_resilient_task()