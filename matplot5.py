import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

sizes=[40,40,50,40]
labels=['A','B','C','D']
plt.pie(sizes,labels=labels,autopct='%1.1f%%',startangle=90)
plt.title("Pie Chart")
plt.show()