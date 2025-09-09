import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x=np.random.rand(90)
y=np.random.rand(90)
plt.scatter(x,y,color="purple",marker="x")
plt.title("Scatter Plot")
plt.show()