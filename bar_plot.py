import seaborn as sns
import matplotlib.pyplot as plt

# Data
categories = ['Food', 'Travel', 'Shopping', 'Bills']
amounts = [500, 300, 700, 400]

# Bar plot
sns.barplot(x=categories, y=amounts)

plt.title("Expenses by Category")
plt.xlabel("Category")
plt.ylabel("Amount")

plt.show()