import seaborn as sns
import matplotlib.pyplot as plt

# Set style
sns.set_style("darkgrid")

# Data
categories = ['Food', 'Travel', 'Shopping', 'Bills']
amounts = [500, 300, 700, 400]

# Bar plot with color palette
sns.barplot(x=categories, y=amounts, palette="pastel")

plt.title("Styled Expense Chart")
plt.xlabel("Category")
plt.ylabel("Amount")

plt.show()