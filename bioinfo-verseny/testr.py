
import pandas as pd

sample = [1, 2, 2, 2, 2.5, 3, 5, 6]
df = pd.DataFrame(data=sample)
print(df.std())

lt = (1, 2, 3)
if type(lt) == tuple:
	print("OKR")