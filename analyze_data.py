import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate
import matplotlib.cm as cm

# Define file paths for the CSV files
file_path = "Products.csv"
file_path2 = "CVE_RECORDS2.csv"

# Load the CSV files into pandas DataFrame
product_table = pd.read_csv(file_path)
cve_records_table = pd.read_csv(file_path2)

# Merge the two tables on the 'ID' column
merge_data = pd.merge(product_table, cve_records_table, on='ID')

# Clean the CVSS_SCORE column (ensure it's numeric and drop rows with NaN)
merge_data['CVSS_SCORE'] = pd.to_numeric(merge_data['CVSS_SCORE'], errors='coerce')
merge_data = merge_data.dropna(subset=['CVSS_SCORE'])

# Define custom colors for each database
color_map = {
    'MySQL': 'yellow',
    'OracleDB': 'red',
    'PostgreSQL': 'lightblue',
    'MariaDB': 'magenta',
    'MSSQLSERVER': 'darkgreen'
}

# Function to generate individual histograms for each group
def generate_group_histograms():
    group_by_name = merge_data.groupby('NAME')

    # Create a figure for the combined histogram
    fig, ax = plt.subplots(figsize=(10, 8))

    # Iterate over each group and plot a histogram for each
    for name, group in group_by_name:
        print(f"Plotting histogram for group: {name}")  # Debugging line

        # Get the color for the current group from the color map
        color = color_map.get(name, 'gray')  # Default to gray if the group is not in the color map

        # Plot histogram for the current group and retrieve the data
        counts, bins, patches = ax.hist(group['CVSS_SCORE'], bins=10, alpha=0.7, edgecolor='black', label=name,
                                        color=color)

    # Add title and labels
    ax.set_title('Combined Histogram of CVSS Scores by Product Group')
    ax.set_xlabel('CVSS Score')
    ax.set_ylabel('Frequency')

    # Add grid for better readability
    ax.grid(axis='y', alpha=0.75)

    # Add legend
    ax.legend(loc='upper right')

    # Tight layout for better spacing
    plt.tight_layout()

    # Return the figure object to embed in Tkinter
    return fig

# Function to generate a pie chart for average CVSS scores grouped by 'NAME'
def generate_avg_cvss_pie_chart():
    # Calculate the average CVSS score for each product group
    avg_cvss_scores = merge_data.groupby('NAME')['CVSS_SCORE'].mean()

    # Identify the product with the highest and lowest average CVSS scores
    highest_cvss_product = avg_cvss_scores.idxmax()  # Product with the worst score
    lowest_cvss_product = avg_cvss_scores.idxmin()  # Product with the best score

    # Define colors: Red for highest (worst), Green for lowest (best), random for others
    colors = []
    for name in avg_cvss_scores.index:
        if name == highest_cvss_product:
            colors.append('red')
        elif name == lowest_cvss_product:
            colors.append('green')
        else:
            colors.append(plt.cm.Paired(len(colors) / len(avg_cvss_scores)))  # Random distinct color

    # Create the pie chart
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.pie(
        avg_cvss_scores,
        labels=avg_cvss_scores.index,
        autopct='%1.1f%%',
        startangle=140,
        colors=colors
    )

    # Add title
    ax.set_title('Average CVSS Scores by Product Group (Highlighting Best and Worst)')

    # Return the figure object to embed in Tkinter or display
    return fig


# Generate and display the histograms and average CVSS pie chart
if __name__ == "__main__":
    generate_group_histograms()
    generate_avg_cvss_pie_chart()
    plt.show()
