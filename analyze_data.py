import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate
import matplotlib.cm as cm

# Define file paths for the CSV files
file_path = "Products.csv"
file_path2 = "CVE_RECORDS2.csv"

# Load the CSV files into pandas DataFrames
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

# If you want to call this function to generate and display the histograms directly
# generate_group_histograms()
