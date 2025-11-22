import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Data
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
scores = [0.11, 1.29, 4.33, 7.59]
benchmark = 4.5

# Calculate Average
average_score = np.mean(scores)
print(f"Calculated Average: {average_score}")

# Create DataFrame
df = pd.DataFrame({'Quarter': quarters, 'Score': scores})

# Plot
plt.figure(figsize=(10, 6))
plt.plot(df['Quarter'], df['Score'], marker='o', linewidth=2, label='Patient Satisfaction')
plt.axhline(y=benchmark, color='r', linestyle='--', label=f'Target ({benchmark})')
plt.axhline(y=average_score, color='g', linestyle=':', label=f'Current Avg ({average_score:.2f})')

plt.title('2024 Quarterly Patient Satisfaction Trends')
plt.xlabel('Quarter')
plt.ylabel('Satisfaction Score')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('satisfaction_trend.png')
