import numpy as np
import matplotlib.pyplot as plt

t_periods = ["T1","T2","T3","T4"]
cat_A=[1,2,3,4]
cat_B=[3,4,5,6]
cat_C=[4,6,3,4]

plt.bar(t_periods,cat_A,label="Category A", color="red")
plt.bar(t_periods,cat_B,label="Category B", bottom=cat_A, color="blue")
plt.bar(t_periods,cat_C,label="Category C", bottom=np.array(cat_A)+np.array(cat_B), color="green")

plt.xlabel("Time Periods")
plt.ylabel("Values")
plt.title("Stacked Bar Graph")
plt.legend()
plt.show()
