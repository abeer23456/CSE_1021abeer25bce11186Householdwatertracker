import numpy as np
import math
import matplotlib.pyplot as plt

x = 0.0
y = 0.0
z = 0.0
total_usage = 0.0
num_days = 0
general_house_avg = 0.0

def calculate_averages():
    global total_usage, num_days
    if num_days > 0:
        avg_daily_usage = total_usage / num_days
        print("--- daily average report ---")
        print("we have tracked usage for" , num_days, "days")
        print("total water used" , total_usage, "units")
        print("your calculated average daily usage is" , avg_daily_usage, "units")
        return avg_daily_usage
    else:
        print("we need data for at least one day before we can calculate the average")
        return 0.0

def plot_comparison(user_avg):
    global general_house_avg

    if general_house_avg == 0.0:
        avg = float(input("tell us the general average daily usage for other homes (in units) "))
        general_house_avg = avg

    if user_avg > 0.0 and general_house_avg > 0.0:
        labels = ['your average', 'general household average']
        values = [user_avg, general_house_avg]

        plt.figure(figsize=(8, 5))
        plt.bar(labels, values, color=['red', 'green'])
        plt.ylabel('water usage (units)')
        plt.title('daily water usage comparison')
        plt.grid(axis='y', alpha=0.5)
        plt.show()
    else:
        print("we cant generate a plot yet make sure you have entered enough data and a comparison average")

print("--- welcome to your household water tracker ---")

case = int(input("enter 1 (add general) 2 (add waste) 3 (add hygiene) 4 (view totals) 5 (plot averages) 0 (exit) "))

while(case != 0):
    match case:
        case 1:
            print("general usage " )
            x_add = float(input("how much water was used for general purposes "))
            x = x + x_add
            total_usage = total_usage + x_add
            num_days = num_days + 1
            print("usage added your running total is" , total_usage, "units youve tracked" , num_days, "day(s)")

        case 2:
            print(" water wastage ")
            y_add = float(input("how much water was wasted (e g leaks) "))
            y = y + y_add
            total_usage = total_usage + y_add
            print("wastage logged running total is" , total_usage, "units")

        case 3:
            print("hygiene usage")
            z_add = float(input("how much water was used for hygiene "))
            z = z + z_add
            total_usage = total_usage + z_add
            print("hygiene usage recorded running total is" , total_usage, "units")

        case 4:
            print("your current usage breakdown")
            print("general usage" , x, "units")
            print("wastage" , y, "units")
            print("hygiene usage" , z, "units")
            print("total usage" , total_usage, "units")
            print("days tracked" , num_days)

        case 5:
            current_avg = calculate_averages()
            plot_comparison(current_avg)

        case _:
            print("not a valid option please try again")

    case = int(input("enter 1-3 to add usage 4 to view totals 5 to plot averages 0 to exit "))

print("program closed")