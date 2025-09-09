import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

categories=["A","B","C"]
values=[2,4,6]
plt.barh(categories,values,color="olive")
plt.title("Horizontal Bar Plot")
plt.show()