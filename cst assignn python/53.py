##53.	Implement a bar chart visualizing sales data over a month.

import matplotlib.pyplot as plt 

days =range(1,31)
sales=[abs(day*2+5-(day%7)*3) for day in days]

plt.bar(days,sales)
plt.show()