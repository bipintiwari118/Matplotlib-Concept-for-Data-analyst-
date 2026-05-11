#subplots
#used to show multiple plots in a single figure


import matplotlib.pyplot as plt

#data 1 for bar chart
countries = ["India", "USA", "China", "Russia", "Japan"]
sales = [1380, 331, 1441, 146, 126]


#data 2 for line chart

years = [2010, 2012, 2014, 2016, 2018]
profits = [100, 150, 200, 250, 300]



#data 3 for scatter plot
s1 = [1, 2, 3, 4, 5]
s2 = [18, 3, 14, 45, 36]

#data 4 for pie chart
labels = ["A", "B", "C", "D"]
sizes = [25, 30, 20, 25]


plt.figure(figsize=(10, 8))

plt.subplot(1,2,1) #1 row, 2 columns, 1st position

plt.bar(countries, sales,color="purple")
plt.title("Bar Chart")
plt.xlabel("Countries")
plt.ylabel("Sales")


plt.subplot(1,2,2) #1 row, 2 columns, 2nd position
plt.plot(years, profits, marker="o", color="green")
plt.title("Line Chart")
plt.xlabel("Years")
plt.ylabel("Profits")


plt.subplot(2,2,3) #2 rows, 2 columns, 3rd position
plt.scatter(s1, s2, color="orange")
plt.title("Scatter Plot")
plt.xlabel("s1")
plt.ylabel("s2")

plt.subplot(2,2,4) #1 row, 4 columns, 4th position
plt.pie(sizes, labels=labels, autopct="%1.1f%%", colors=["red", "blue", "green", "yellow"])
plt.title("Pie Chart")


plt.show()