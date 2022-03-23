#
# This file is test is for set type
#
# coding:utf8
import time
import signal
import requests


# Custom timeout exception
class TimeoutError(Exception): pass

#  Call this function exceeds timeout
def handler(signum, frame):
    raise TimeoutError()

#  Function timeout decorator
def time_out(interval, doc):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                signal.signal(signal.SIGALRM, handler)
                signal.alarm(interval)       #  Interval seconds to send SIGALRM signals to the process
                result = func(*args, **kwargs)
                signal.alarm(0)              #  After the function is executed after the specified time is executed, close the Alarm alarm clock
                return result
            except TimeoutError as e:
                #  Capture the timeout exception, what to do
                print("The function failed to run due to timeout, func:<%s>" % doc)
        return wrapper
    return decorator

@time_out(1, "Demo.py Task1 function")
def task1(req, par):
    #print("task1 start")
    try:
        response = requests.post(req, data = par)
    except:
        response = False
    return response
    # time.sleep(1.2)


string_api_url = "https://string-db.org/api"
output_format = "tsv-no-header"
method = "ppi_enrichment"

my_taxid = 7227
my_genes = ['7227.FBpp0074373', '7227.FBpp0077451', '7227.FBpp0077788',
            '7227.FBpp0078993', '7227.FBpp0079060', '7227.FBpp0079448']

params = {
    "identifiers":      "%0d".join(my_genes),   # your proteins
    "species":          my_taxid,                   # species NCBI identifier
    "caller_identity":  "tester_zdul"           # your app name
}

request_url = "/".join([string_api_url, output_format, method])


if __name__ == "__main__":
    print("start")
    counter = 0
    for i in range(1000):
        counter += 1
        print(task1(request_url, params))
        if (counter % 100) == 0:
            print(counter, " - OK")


