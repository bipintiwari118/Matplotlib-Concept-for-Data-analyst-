#matplotlib with pandas

import matplotlib.pyplot as plt
import pandas as pd


data={
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Sales': [150, 350, 100, 150, 320, 450]
}

df=pd.DataFrame(data)

print(df)


plt.bar(df['Month'],df['Sales'],color='blue')
plt.title('Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Sales')

plt.savefig('monthly_sales.png')  # Save the plot as an image file
plt.show()