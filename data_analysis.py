# data_analysis.py

# Import required libraries for data analysis and visualization
import pandas as pd  # Pandas for data manipulation and analysis
import numpy as np   # NumPy for numerical operations
import matplotlib.pyplot as plt  # Matplotlib for creating visualizations

# Define the dataset as a dictionary with student information
data = {
    "ID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],  # Unique identifier for each student
    "Major": ["Psychology", "Computer Science", "Business", "Biology", "History", 
              "Mathematics", "Engineering", "Sociology", "Biology", "Education"],  # Student's field of study
    "Study_Hours": [15, 20, 10, 25, 12, 30, 18, 22, 16, 14],  # Hours spent studying per week
    "GPA": [3.5, 3.8, 3.2, 2.5, 3.1, 4.0, 3.6, 3.7, 2.4, 3.3],  # Grade Point Average
    "Sleep_Hours": [7, 6, 5, 8, 6, 7, 6, 8, 5, 6]  # Hours of sleep per night
}

# Create a Pandas DataFrame from the dictionary for easier data handling
df = pd.DataFrame(data)

# Perform statistical analysis on numerical columns
# Study Hours statistics
study_mean = df["Study_Hours"].mean()  # Calculate average study hours
study_median = df["Study_Hours"].median()  # Find the middle value of study hours
study_mode = df["Study_Hours"].mode()[0]  # Get the most common study hours value (first mode if multiple)
study_std = df["Study_Hours"].std()  # Calculate the standard deviation of study hours

# GPA statistics
gpa_mean = df["GPA"].mean()  # Calculate average GPA
gpa_median = df["GPA"].median()  # Find the middle value of GPAs
gpa_mode = df["GPA"].mode()[0]  # Get the most common GPA (first mode if multiple)
gpa_std = df["GPA"].std()  # Calculate the standard deviation of GPAs

# Sleep Hours statistics
sleep_mean = df["Sleep_Hours"].mean()  # Calculate average sleep hours
sleep_median = df["Sleep_Hours"].median()  # Find the middle value of sleep hours (fixed typo)
sleep_mode = df["Sleep_Hours"].mode()[0]  # Get the most common sleep hours (first mode if multiple)
sleep_std = df["Sleep_Hours"].std()  # Calculate the standard deviation of sleep hours

# Display the statistical results in a formatted output
print("Statistical Analysis of Student Data:")  # Header for output
print("\nFor Study Hours per Week:")  # Section header
print(f"  Mean: {study_mean:.2f}")  # Print mean with 2 decimal places
print(f"  Median: {study_median:.2f}")  # Print median with 2 decimal places
print(f"  Mode: {study_mode}")  # Print mode
print(f"  Standard Deviation: {study_std:.2f}")  # Print standard deviation with 2 decimal places

print("\nFor GPA:")  # Section header
print(f"  Mean: {gpa_mean:.2f}")  # Print mean GPA
print(f"  Median: {gpa_median:.2f}")  # Print median GPA
print(f"  Mode: {gpa_mode}")  # Print mode GPA
print(f"  Standard Deviation: {gpa_std:.2f}")  # Print standard deviation of GPA

print("\nFor Sleep Hours per Week:")  # Section header
print(f"  Mean: {sleep_mean:.2f}")  # Print mean sleep hours
print(f"  Median: {sleep_median:.2f}")  # Print median sleep hours
print(f"  Mode: {sleep_mode}")  # Print mode sleep hours
print(f"  Standard Deviation: {sleep_std:.2f}")  # Print standard deviation of sleep hours

# Create a histogram to visualize the distribution of study hours
plt.figure(figsize=(10, 6))  # Set the figure size to 10 inches wide by 6 inches tall
plt.hist(df["Study_Hours"], bins=5, edgecolor='black')  # Create histogram with 5 bins and black edges
plt.title("Distribution of Study Hours per Week")  # Add a title to the plot
plt.xlabel("Study Hours")  # Label the x-axis
plt.ylabel("Number of Students")  # Label the y-axis
plt.grid(True, alpha=0.3)  # Add a light grid for better readability (alpha controls transparency)
plt.show()  # Display the histogram in a new window
