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

