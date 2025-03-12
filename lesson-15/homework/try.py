import numpy as np
import matplotlib.pyplot as plt

t_periods = ["T1","T2","T3","T4"]
cat_A=[1,2,3,4]
cat_B=[3,4,5,6]
cat_C=[4,6,3,4]

x=np.arange(len(t_periods))
w=0.2
plt.bar(x-w,cat_A,label="Category A", color="red", width=w)
plt.bar(x,cat_B,label="Category B", color="blue", width=w)
plt.bar(x+w,cat_C,label="Category C", color="green", width=w)

plt.xlabel("Time Periods")
plt.ylabel("Values")
plt.xticks(x, t_periods)
plt.title("Grouped Bar Graph")
plt.legend()
plt.show()