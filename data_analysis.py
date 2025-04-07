# data_analysis.py

# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create the dataset using the provided student data
data = {
    "ID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Major": ["Psychology", "Computer Science", "Business", "Biology", "History", 
              "Mathematics", "Engineering", "Sociology", "Biology", "Education"],
    "Study_Hours": [15, 20, 10, 25, 12, 30, 18, 22, 16, 14],
    "GPA": [3.5, 3.8, 3.2, 2.5, 3.1, 4.0, 3.6, 3.7, 2.4, 3.3],
    "Sleep_Hours": [7, 6, 5, 8, 6, 7, 6, 8, 5, 6]
}

# Create a DataFrame from the dataset
df = pd.DataFrame(data)

# Perform statistical analysis on numerical columns
# Calculate statistics for Study Hours
study_mean = df["Study_Hours"].mean()
study_median = df["Study_Hours"].median()
study_mode = df["Study_Hours"].mode()[0]  # Take first mode if multiple exist
study_std = df["Study_Hours"].std()

# Calculate statistics for GPA
gpa_mean = df["GPA"].mean()
gpa_median = df["GPA"].median()
gpa_mode = df["GPA"].mode()[0]
gpa_std = df["GPA"].std()

# Calculate statistics for Sleep Hours
sleep_mean = df["Sleep_Hours"].mean()
sleep_median = df["Sleep_Hours"].median()
sleep_mode = df["Sleep_Hours"].mode()[0]
sleep_std = df["Sleep_Hours"].std()

# Print the statistical analysis
print("Statistical Analysis of Student Data:")
print("\nFor Study Hours per Week:")
print(f"  Mean: {study_mean:.2f}")
print(f"  Median: {study_median:.2f}")
print(f"  Mode: {study_mode}")
print(f"  Standard Deviation: {study_std:.2f}")

print("\nFor GPA:")
print(f"  Mean: {gpa_mean:.2f}")
print(f"  Median: {gpa_median:.2f}")
print(f"  Mode: {gpa_mode}")
print(f"  Standard Deviation: {gpa_std:.2f}")

print("\nFor Sleep Hours per Week:")
print(f"  Mean: {sleep_mean:.2f}")
print(f"  Median: {sleep_median:.2f}")
print(f"  Mode: {sleep_mode}")
print(f"  Standard Deviation: {sleep_std:.2f}")

# Create a histogram for Study Hours distribution
plt.figure(figsize=(10, 6))  # Set figure size
plt.hist(df["Study_Hours"], bins=5, edgecolor='black')  # Create histogram with 5 bins
plt.title("Distribution of Study Hours per Week")  # Add title
plt.xlabel("Study Hours")  # Label x-axis
plt.ylabel("Number of Students")  # Label y-axis
plt.grid(True, alpha=0.3)  # Add a light grid
plt.show()  # Display the histogram
