#line chart

import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[10,20,15,25,30]
y1=[5,15,10,20,25]



plt.plot(x,y,color='red',label="2025 Sales")
plt.plot(x,y1,color='blue',label="2024 Sales")
plt.title("Yearly Sales Comparison",fontsize=16)
plt.xlabel("month",fontsize=14)
plt.ylabel("sales",fontsize=14)

plt.legend()
plt.show()