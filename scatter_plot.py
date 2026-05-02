import seaborn as sns
import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [5, 15, 20, 25, 30]

# Scatter plot
sns.scatterplot(x=x, y=y)

plt.title("Seaborn Scatter Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")

plt.savefig("images/scatter_plot.png")

plt.show()