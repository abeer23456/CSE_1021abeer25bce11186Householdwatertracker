# Project Statement: Household Water Usage Tracker
# Problem Statement
Households often struggle to accurately track their water consumption due to reliance on infrequent utility bills or a lack of granular, accessible tools. This lack of precise, real-time feedback makes it difficult to detect subtle leaks, identify major sources of waste (like long showers or appliance inefficiency), and implement effective conservation measures. The manual process of logging usage is tedious and prone to human error, hindering genuine behavioral change toward water conservation.

# Scope of the Project
The Household Water Usage Tracker is implemented as a simple, robust Command Line Interface (CLI) application using Python. Its scope is defined by the following boundaries:

# In Scope:
Accepting user inputs for water consumption across three main categories (General, Wastage, Hygiene).

Performing accurate floating-point arithmetic to compute total usage and average daily usage.

Implementing structured control flow (using match case) for menu navigation and session management.

Integrating external libraries (matplotlib) to perform data visualization (plotting comparison bar charts).

Handling the edge case of zero-division protection (specifically checking if num_days is 0).

 # Out of Scope:
Data persistence (the application does not save historical usage data across sessions).

Development of a Graphical User Interface (GUI) or web interface.

Real-time sensor integration (all data is manually entered).

Automated unit conversion (e.g., liters to gallons).

# Target Users
The primary users of this project are individuals or small groups interested in improving resource management and reducing utility costs.

Homeowners and Renters: Individuals focused on tracking monthly expenses and reducing their water footprint.

Students Learning Analytics: Users who require a functional program to demonstrate the application of data aggregation and visualization concepts.

Environmentally Conscious Users: Those seeking quantitative data to monitor and validate their conservation efforts.

# High-Level Features
Categorization: An interactive feature that prompts the user to categorize consumption into General, Wastage, or Hygiene usage.

Aggregation Engine: The core module responsible for performing immediate summation and maintaining three distinct running totals plus a grand total.

Analytical Reporting: The feature that computes the Average Daily Usage and displays a summary of the tracking period.

Visualization Module: The module responsible for generating the visual bar chart comparison of user average vs. external benchmark.

Session Management: The feature that sustains the program's operation, allowing the user to perform multiple entries and calculations without requiring a restart.
