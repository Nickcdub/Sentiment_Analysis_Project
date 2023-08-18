import matplotlib.pyplot as plt
import pandas as pd

# Read data from your provided data
data = pd.read_csv('Comparison.csv')  # Replace with your data file's path

# Count correct and incorrect predictions for each model
model_a_counts = data['BoW'].value_counts()
model_b_counts = data['CNN'].value_counts()
actual_counts = data['Actual'].value_counts()

# Create a figure and axis
fig, ax = plt.subplots()

# Define categories
categories = ['Negative', 'Positive']

# Set bar width
bar_width = 0.2

# Calculate positions for bars
index = range(len(categories))
index_model_a = index
index_model_b = [i + bar_width for i in index]
index_actual = [i + 2 * bar_width for i in index]

# Define custom colors for each bar
color_bow = 'purple'   # Change this to your desired color for BoW
color_cnn = '#0990B8'  # Change this to your desired color for CNN
color_actual = 'gray'  # Change this to your desired color for Actual

# Plot bars for Model A, Model B, and actual answers
ax.bar(index_model_a, model_a_counts, bar_width, label='BoW', color=color_bow)
ax.bar(index_model_b, model_b_counts, bar_width, label='CNN', color=color_cnn)
ax.bar(index_actual, actual_counts, bar_width, label='Actual', color=color_actual)

# Add labels and title
ax.set_xlabel('Sentiment')
ax.set_ylabel('Count')
ax.set_title('Comparison of Model Predictions with Actual Answers')
ax.set_xticks([i + bar_width for i in index])
ax.set_xticklabels(categories)

# Add legend
ax.legend()

# Show the plot
plt.show()
