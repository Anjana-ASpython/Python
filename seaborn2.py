import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
data=pd.DataFrame({
    "category":['A','B','C','D'],
    "value":[8,4,2,5]
})
sns.barplot(x="category",y="value",data=data)
plt.title("Normal Bar Chart(Seaborn)")
plt.show()