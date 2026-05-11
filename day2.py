# Matplotlib Bar Plot 
import matplotlib.pyplot as plt


x=['A', 'B', 'C', 'D', 'E']
y=[10, 20, 15, 25, 30]

c=['red', 'blue', 'green', 'orange', 'purple']

plt.bar(x,y,color=c,width=0.5,edgecolor='purple' ,linewidth=5,alpha=0.7,label=x)
plt.legend()
plt.title('Bar Plot Example')
plt.xlabel("Categories",fontsize=14)
plt.ylabel('Values',fontsize=14)

plt.show()