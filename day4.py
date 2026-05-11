#histogram
# use for distribution of data

import matplotlib.pyplot as plt
import random


data=[random.randint(1,100) for i in range(1000)]

plt.hist(data,bins=20,color='yellow')
plt.xlabel("Values",fontsize=14)
plt.ylabel("Frequency",fontsize=14)
plt.title("Histogram of Random Data",fontsize=16)
plt.show()