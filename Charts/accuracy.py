import matplotlib.pyplot as plt

# Sample data
categories = ['BoW Testing', 'BoW Training', 'CNN Testing', 'CNN Training']
values = [88.6, 99.97, 80.18, 99.95]

# Define custom colors for each bar
colors = ['#0990B8', 'purple', '#0990B8', 'purple']

# Create a horizontal bar graph with custom colors
plt.barh(categories, values, color=colors)

# Add labels and title
plt.xlabel('%Accuracy')
plt.title('Test & Training Accuracy')

# Show the plot
plt.show()
