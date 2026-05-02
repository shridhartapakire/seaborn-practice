import seaborn as sns
import matplotlib.pyplot as plt

# Data
expenses = [100, 200, 150, 300, 250, 400, 350, 200, 150, 300]

# Histogram
sns.histplot(expenses, bins=5)

plt.title("Expense Distribution")
plt.xlabel("Amount")
plt.ylabel("Frequency")

plt.savefig("images/histogram.png")

plt.show()