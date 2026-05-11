#piechart

import matplotlib.pyplot as plt

countries=['USA', 'China', 'India', 'Germany', 'UK']
population=[331, 1441, 1380, 830, 684]
colors=['blue', 'red', 'green', 'orange', 'purple']

plt.pie(population, labels=countries, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title("Population Distribution by Country", fontsize=16)
plt.show()