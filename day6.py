# Scatter Plot 
# used to find relationship between  variables


import matplotlib.pyplot as plt

s1 = [1, 2, 3, 4, 5]
s2 = [18, 3, 14, 45, 36]

plt.scatter(s1, s2)
plt.title("Scatter Plot")
plt.xlabel("s1")
plt.ylabel("s2")
plt.show()
