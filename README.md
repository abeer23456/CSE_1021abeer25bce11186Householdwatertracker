# Household Water Usage Tracker
# Overview of the Project
The Household Water Usage Tracker is a stand-alone Command Line Interface (CLI) application built in Python. It is designed to help users monitor, categorize, and analyze their daily water consumption. By manually inputting usage amounts across three categories, the program provides real-time analytical reports and a visual comparison plot against general household averages.

# Features
Categorized Tracking: Allows manual logging of water usage into General, Wastage, and Hygiene categories.

Average Daily Calculation: Automatically computes the Average Daily Usage based on the days tracked.

Comparative Plotting: Generates a dynamic bar chart using the matplotlib library to visually compare the user's average against a community average.

Incremental Aggregation: Maintains running totals for all categories during the session.

Structured Control: Uses Python's match case structure for clean and reliable menu navigation.

# Technologies/Tools Used
Programming Language: Python 3.10+ (Required for match/case)

Numerical Processing: numpy

Data Visualization: matplotlib.pyplot

Interface: Command Line / Terminal

# Steps to Run the Project:

Open the Terminal: In VS Code, go to the menu bar and select Terminal > New Terminal.

Install Dependencies: In the terminal window that appears, install the required external libraries:

Bash

pip install numpy matplotlib

Start the Program: Type the following command (using your script name) and press Enter:

Bash

python house_water_tracker.py
