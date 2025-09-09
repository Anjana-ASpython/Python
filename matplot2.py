import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

categories=["A","B","C"]
values=[2,4,6]
plt.bar(categories,values,color=["blue","green","yellow"])
plt.title("Bar Plot")
plt.show()