import numpy as np
import pandas as pd
data=[5,8,12,15,18,22,25,28,30]

#mean
mean=np.mean(data)
print(f"Mean={mean}")
#median
median=np.median(data)
print(f"Median={median}")
#mode
mode=pd.Series(data).mode()  #We use pd and convert to series because of the type of data set
print(f"Mode={mode.to_list() if not mode.empty else 'No mode'}")
#range
range=np.max(data)-np.min(data)
print(f"Range={range}")
#variance
variance=np.var(data,ddof=1)
print(f"Variance={variance}")
#standard deviation
sd=np.std(data,ddof=1)
print(f"standard deviation={sd}")
#Interquatile range
q1=np.percentile(data,25)
q3=np.percentile(data,75)
iqr=q3-q1
print(f"Interquatile range={iqr}")