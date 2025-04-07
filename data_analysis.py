# data_analysis.py

"""
This script is my project for data analysis using Pandas, NumPy, and Matplotlib.
It creates a dataset about students, performs descriptive statistical analysis,
and visualizes the distribution of study hours per week.

Dataset columns:
- ID: Unique identifier for each student
- Study_Hours: Number of study hours per week
- GPA: Student's grade point average
- Sleep_Hours: Hours of sleep per week
"""

# Importing the required libraries
import pandas as pd       # Used for data manipulation and analysis
import numpy as np        # Provides numerical operations
import matplotlib.pyplot as plt  # Used for data visualization

# Step 1: Create a dataset with at least 4 columns and 10 entries.
# I created a dictionary where each key represents a column in the dataset.
data = {
    'ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Study_Hours': [15, 20, 10, 25, 12, 30, 18, 22, 16, 14],
    'GPA': [3.5, 3.8, 3.2, 2.5, 3.1, 4.0, 3.6, 3.7, 2.4, 3.3],
    'Sleep_Hours': [7, 6, 5, 8, 6, 7, 6, 8, 5, 6]
}

# Step 2: Load the data into a Pandas DataFrame.
df = pd.DataFrame(data)

# Print out the dataset to ensure it's loaded correctly.
print("Dataset preview:")
print(df)

# Step 3: Perform descriptive statistical analysis on the dataset.
# I will calculate the mean, median, mode, and standard deviation for Study_Hours, GPA, and Sleep_Hours.
columns_to_analyze = ['Study_Hours', 'GPA', 'Sleep_Hours']

for col in columns_to_analyze:
    mean_val = df[col].mean()       # Calculate the mean (average) of the column.
    median_val = df[col].median()   # Calculate the median (middle value) of the column.
    mode_val = df[col].mode()[0]      # Calculate the mode (most frequent value); using the first mode if there are multiple.
    std_val = df[col].std()           # Calculate the standard deviation of the column.
    
    # Print the results with a clear format.
    print(f"\nFor {col}:")
    print(f"  Mean: {mean_val:.2f}")
    print(f"  Median: {median_val:.2f}")
    print(f"  Mode: {mode_val}")
    print(f"  Standard Deviation: {std_val:.2f}")

# Step 4: Create a histogram to visualize the distribution of study hours per week.
# This histogram will help me see how study hours are spread across the dataset.
plt.figure(figsize=(8, 5))  # Set the figure size for the histogram.
plt.hist(df['Study_Hours'], bins=5, edgecolor='black')  # Create a histogram with 5 bins and black borders for clarity.
plt.title("Distribution of Study Hours per Week")  # Title for the histogram.
plt.xlabel("Study Hours per Week")  # X-axis label.
plt.ylabel("Frequency")  # Y-axis label.
plt.grid(True)  # Add grid lines for better readability.

# Optionally, save the histogram as an image file.
plt.savefig("study_hours_histogram.png")

# Display the histogram.
plt.show()
