import os
import glob
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

path = './data'
all_files = glob.glob(os.path.join(path, "*.csv"))
df = pd.concat((pd.read_csv(f) for f in all_files), ignore_index=True)
df.dropna(inplace=True)

summary = df.groupby('Year').mean(numeric_only=True) .reset_index()
slope, intercept, r_value, p_value, std_err = stats.linregress(df['Temperature'], df['Yield'])

# Plot 1: Trend
plt.figure(figsize=(6, 4))
plt.plot(summary['Year'], summary['Yield'], marker='o', color='teal')
plt.title('Crop Yield Trend Over Time')
plt.xlabel('Year [Annum]')
plt.ylabel('Yield [tons/ha]')
plt.grid(True)
plt.tight_layout()
plt.savefig('trend_analysis.png')
plt.close()

# Plot 2: Categorical
plt.figure(figsize=(6, 4))
region_summary = df.groupby('Region')['Yield'].mean().reset_index()
plt.bar(region_summary['Region'], region_summary['Yield'], color='forestgreen')
plt.title('Average Crop Yield by Region')
plt.xlabel('Region')
plt.ylabel('Yield [tons/ha]')
plt.grid(axis='y')
plt.tight_layout()
plt.savefig('categorical_comparison.png')
plt.close()

# Plot 3: Correlation
plt.figure(figsize=(6, 4))
plt.scatter(df['Temperature'], df['Yield'], alpha=0.6, color='darkorange')
x_line = np.linspace(df['Temperature'].min(), df['Temperature'].max(), 100)
plt.plot(x_line, slope * x_line + intercept, color='red', label=f'R = {r_value:.2f}')
plt.title('Temperature vs. Crop Yield')
plt.xlabel('Temperature [°C]')
plt.ylabel('Yield [tons/ha]')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig('correlation_plot.png')
plt.close()

print("Plots generated successfully!")

import matplotlib.pyplot as plt
import pandas as pd

# 1. Load the authentic FAOSTAT file you just uploaded
fao_file = "data/FAOSTAT_data_en_7-2-2026.csv"
df = pd.read_csv(fao_file)

# 2. Filter data for a specific element (e.g., Yield vs Production Quantity)
# Standard FAOSTAT elements: "Yield" or "Production"
yield_data = df[df["Element"] == "Yield"].sort_values("Year")
prod_data = df[df["Element"] == "Production"].sort_values("Year")

# 3. Generate a dual-axis trend visualization
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot Yield Trend
color = "tab:green"
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("Yield (Hg/Ha)", color=color, fontsize=12)
ax1.plot(
    yield_data["Year"],
    yield_data["Value"],
    color=color,
    marker="o",
    linewidth=2,
    label="Yield",
)
ax1.tick_params(axis="y", labelcolor=color)
ax1.grid(True, linestyle="--", alpha=0.5)

# Plot Production Volume Trend on secondary axis
ax2 = ax1.twinx()
color = "tab:blue"
ax2.set_ylabel("Total Production (Tonnes)", color=color, fontsize=12)
ax2.plot(
    prod_data["Year"],
    prod_data["Value"],
    color=color,
    marker="s",
    linewidth=2,
    linestyle="--",
    label="Production",
)
ax2.tick_params(axis="y", labelcolor=color)

plt.title("Tanzania Agricultural Trends (FAOSTAT Data)", fontsize=14, pad=15)
fig.tight_layout()

# Save the real-world engineering visualization output
plt.savefig("trend_analysis.png", dpi=300)
print(
    "Analysis complete! Updated trend_analysis.png with authentic FAOSTAT data."
)

