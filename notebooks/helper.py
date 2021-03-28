# in helper.py
import numpy as np


def forecasting(x):
	# just some math stuff here
	yhat = np.sum([np.exp(i) for i in x])

	# return a single scalar (number)
	return yhat