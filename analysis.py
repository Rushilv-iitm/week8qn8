"""
Healthcare Patient Satisfaction Analysis - 2024
Author: 23f2000060@ds.study.iitm.ac.in

This script:
- Loads quarterly patient satisfaction data
- Computes the average satisfaction score
- Compares it against the industry target (4.5)
- Creates visualizations:
    1. Line chart of satisfaction over quarters
    2. Bar chart with industry target reference line
- Prints key metrics to the console
"""

import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# 1. Load the quarterly data
# -------------------------------
df = pd.read_csv("data.csv")

# Industry benchmark target
INDUSTRY_TARGET = 4.5

# -------------------------------
# 2. Basic statistics
# -------------------------------
average_score = df["Patient_Satisfaction_Score"].mean()

print("Quarterly Patient Satisfaction Scores (2024):")
print(df)
print()
print(f"Average patient satisfaction score (2024): {average_score:.2f}")
print(f"Industry benchmark target: {INDUSTRY_TARGET}")
print(f"Gap to target: {INDUSTRY_TARGET - average_score:.2f}")

# -------------------------------
# 3. Line chart of quarterly trend
# -------------------------------
plt.figure(figsize=(8, 5))
plt.plot(
    df["Quarter"],
    df["Patient_Satisfaction_Score"],
    marker="o",
    linewidth=2,
)
plt.axhline(
    INDUSTRY_TARGET,
    linestyle="--",
    linewidth=1.5,
)
plt.title("Patient Satisfaction Score - 2024 Quarterly Trend")
plt.xlabel("Quarter")
plt.ylabel("Satisfaction Score")
plt.ylim(0, max(df["Patient_Satisfaction_Score"].max(), INDUSTRY_TARGET) + 1)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("quarterly_trend.png")
plt.close()

# -------------------------------
# 4. Bar chart vs target
# -------------------------------
plt.figure(figsize=(8, 5))
bars = plt.bar(
    df["Quarter"],
    df["Patient_Satisfaction_Score"],
)

plt.axhline(
    INDUSTRY_TARGET,
    linestyle="--",
    linewidth=1.5,
    label=f"Industry Target ({INDUSTRY_TARGET})",
)

plt.title("Patient Satisfaction by Quarter vs Industry Target")
plt.xlabel("Quarter")
plt.ylabel("Satisfaction Score")
plt.legend()
plt.ylim(0, max(df["Patient_Satisfaction_Score"].max(), INDUSTRY_TARGET) + 1)

# Annotate bars with values
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height + 0.05, f"{height:.2f}",
             ha="center", va="bottom", fontsize=9)

plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.savefig("quarterly_vs_target.png")
plt.close()

print("\nVisualizations saved as:")
print(" - quarterly_trend.png")
print(" - quarterly_vs_target.png")
print("\nAnalysis complete.")
