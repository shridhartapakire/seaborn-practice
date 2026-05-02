import seaborn as sns
import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

# Line plot
sns.lineplot(x=x, y=y)

plt.title("Seaborn Line Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")

plt.savefig("images/line_plot.png")

plt.show()