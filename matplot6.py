import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

days=[1,2,3,4,5]
sleeping=[9,3,7,4,1]
working=[2,8,4,2,8]
playing=[4,7,3,7,9]
eating=[6,8,4,2,7]
plt.stackplot(days,sleeping,eating,working,playing,labels=['sleep','eat','work','play'])
plt.legend(loc="lower right")                                        
plt.title("Stacked Area Plot")
plt.show()