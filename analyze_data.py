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


# Function to print out the merged data for visualization
def print_merged_data():
    print(merge_data.head(25))
    group_by_name = merge_data.groupby('NAME')
    for name, group in group_by_name:
        print(f'Group {name}')
        print(tabulate(group, headers='keys', tablefmt='pretty'))


# Function to generate histograms for each group
def generate_histograms():
    group_by_name = merge_data.groupby('NAME')

    # Create a figure for the histograms
    fig = plt.figure(figsize=(12, 8))  # Increase figure size for more space

    # Create a colormap and set up normalization
    cmap = plt.get_cmap('viridis')  # Replace 'viridis' with any colormap name
    norm = plt.Normalize(vmin=0, vmax=1)  # Normalize the colormap to match the range of scores

    # Loop over each group and plot its histogram on the same axes
    for name, group in group_by_name:
        # Plot histogram for the current group
        counts, bins, patches = plt.hist(group['CVSS_SCORE'], bins=10, alpha=0.5, edgecolor='black', label=name)

        # Calculate the average CVSS_SCORE for the group
        avg_score = group['CVSS_SCORE'].mean()

        # Apply a color to the bars based on the colormap
        for count, patch in zip(counts, patches):
            color = cmap(norm(count / max(counts)))  # Normalize each count for colormap
            patch.set_facecolor(color)

        # Add average score annotation
        plt.text(0.95, avg_score, f'{name}: Avg={avg_score:.2f}', ha='right', va='center', fontsize=10, color='black',
                 weight='bold')

    # Set the title, labels, and grid
    plt.title('Combined Histogram of CVSS Scores for All Groups')
    plt.xlabel('CVSS Score')
    plt.ylabel('Frequency')

    # Add grid for better readability
    plt.grid(axis='y', alpha=0.75)

    # Add legend to differentiate groups (adjust position with bbox_to_anchor)
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))

    # Adjust the layout to ensure everything fits
    plt.subplots_adjust(right=0.85)  # Allow more space for the legend and annotations

    # Display the plot
    plt.show()

    return fig


# Function to generate individual histograms for each group
def generate_group_histograms():
    group_by_name = merge_data.groupby('NAME')

    for name, group in group_by_name:
        plt.figure(figsize=(8, 6))

        # Plot histogram for the current group and retrieve the data
        counts, bins, patches = plt.hist(group['CVSS_SCORE'], bins=10, alpha=0.7, edgecolor='black', label=name)

        # Apply a colormap to the bars
        cmap = plt.get_cmap('plasma')  # You can choose any colormap
        norm = plt.Normalize(vmin=0, vmax=max(counts))  # Normalize counts for consistent color mapping
        for count, patch in zip(counts, patches):
            color = cmap(norm(count))  # Get color based on count
            patch.set_facecolor(color)

        # Add title and labels
        plt.title(f'Histogram of CVSS Scores for Group: {name}')
        plt.xlabel('CVSS Score')
        plt.ylabel('Frequency')

        # Add grid for better readability
        plt.grid(axis='y', alpha=0.75)

        # Add legend
        plt.legend(loc='upper right')

        # Display the plot
        plt.tight_layout()
        plt.show()

