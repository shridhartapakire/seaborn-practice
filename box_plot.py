import seaborn as sns
import matplotlib.pyplot as plt

# Data
expenses = [100, 200, 150, 300, 250, 400, 350, 200, 150, 300]

# Box plot
sns.boxplot(x=expenses)

plt.title("Expense Box Plot")
plt.xlabel("Amount")

plt.show()