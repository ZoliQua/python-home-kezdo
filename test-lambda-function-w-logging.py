import logging as lgg

lgg.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', filename='logs/mylog.log', level=lgg.DEBUG)
lgg.debug('This message will be in mylog.log')
lgg.warning('This message will be also in mylog.log')

# HOW to use logging
# URL :: https://docs.python.org/3/howto/logging.html

x = [5, 10, 15]
f = lambda x : [z * 5 for z in x]
print(f(x))

# LAMBDA HOW TO
# URL :: https://medium.com/daily-programming-tips/day12-anonymous-functions-in-python-91b8f6b1a291

lgg.info('Lambda function has been executed.')

import test_import
print("My name: ", __name__)

# norm = lambda x : [i = (i - mean(x)) / std(x) for i in x]
# print(norm(x))
# SOURCE: https://towardsdatascience.com/scientific-python-with-lambda-b207b1ddfcd1