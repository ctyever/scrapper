import pandas as pd
import matplotlib.pyplot as plt

# Create a sample data frame
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [2, 4, 6, 8, 10],
    'C': [3, 6, 9, 12, 15]
})

# Calculate the column average
col_avg = df.mean()

# Plot the distribution of the data
fig, ax = plt.subplots()
df.plot.density(ax=ax)
ax.set_xlabel('Values')
ax.set_ylabel('Density')

# Draw the column average line
for i, col in enumerate(df.columns):
    ax.axvline(x=col_avg[col], color='r', linestyle='--')
plt.savefig(f'example.png')