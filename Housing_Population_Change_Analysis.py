"""
Name: Mark Richardson
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the Population Change CSV file
population_data = pd.read_csv(r"C:\Users\david\OneDrive\Desktop\SDEV 300\Week 5\Housing.csv")

# Load the Housing CSV file
housing_data = pd.read_csv(r"C:\Users\david\OneDrive\Desktop\SDEV 300\Week 5\Housing.csv")

# Function to perform histogram analysis and plots for selected variables
def hist_analysis(data, column_name):
    """Function that performs histogram analysis"""
    selected_column = data[column_name]

    # Calculate statistics
    count = selected_column.count()
    mean = selected_column.mean()
    std = selected_column.std()
    minimum = selected_column.min()
    maximum = selected_column.max()

    # Generate histogram plot
    selected_column.plot.hist(bins=10, edgecolor='black')
    plt.xlabel(column_name)
    plt.ylabel('Frequency')
    plt.title('Histogram Analysis: ' + column_name)
    plt.show()

    # Display statistics
    print("Statistics for column", column_name)
    print("Count:", count)
    print("Mean:", mean)
    print("Standard Deviation:", std)
    print("Min:", minimum)
    print("Max:", maximum)

# User interface for the data analysis app
while True:
    print("***************** Welcome to the Python Data Analysis App ****")
    print("Select the file you want to analyze:")
    print("1. Population Data")
    print("2. Housing Data")
    print("3. Exit the Program")

    choice = input()

    if choice == '1':
        print("You have entered Population Data.")
        print("Select the Column you want to analyze:")
        print("a. Pop Apr 1")
        print("b. Pop Jul 1")
        print("c. Change Pop")
        print("d. Exit Column")

        column_choice = input()

        if column_choice == 'a':
            hist_analysis(population_data, "Pop Apr 1")
        elif column_choice == 'b':
            hist_analysis(population_data, "Pop Jul 1")
        elif column_choice == 'c':
            hist_analysis(population_data, "Change Pop")
        elif column_choice == 'd':
            break
        else:
            print("Invalid column choice. Please try again.")

    elif choice == '2':
        print("You have entered Housing Data.")
        print("Select the Column you want to analyze:")
        print("a. AGE")
        print("b. BEDRMS")
        print("c. BUILT")
        print("d. ROOMS")
        print("e. UTILITY")
        print("f. Exit Column")

        column_choice = input()

        if column_choice == 'a':
            hist_analysis(housing_data, "AGE")
        elif column_choice == 'b':
            hist_analysis(housing_data, "BEDRMS")
        elif column_choice == 'c':
            hist_analysis(housing_data, "BUILT")
        elif column_choice == 'd':
            hist_analysis(housing_data, "ROOMS")
        elif column_choice == 'e':
            hist_analysis(housing_data, "UTILITY")
        elif column_choice == 'f':
            break
        else:
            print("Invalid column choice. Please try again.")

    elif choice == '3':
        break

    else:
        print("Invalid choice. Please try again.")
