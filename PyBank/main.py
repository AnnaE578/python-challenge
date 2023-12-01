# First we'll import the csv module
import csv

# Provide the paths for your CSV file and output text file
file_path = "PyBank/Resources/budget_data.csv"
output_file_path = "PyBank/Resources/output_file.text"

def analyze_financial_data(file_path, output_file_path):
    # Initialize variables
    total_months = 0
    total_profit = 0
    previous_profit = 0
    profit_changes = []
    months = []

    # Read the CSV file
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)

        # Loop through each row in the CSV
        for row in reader:
            # Count total months
            total_months += 1

            # Sum total profit
            total_profit += int(row["Profit/Losses"])

            # Track profit changes
            if total_months > 1:
                profit_change = int(row["Profit/Losses"]) - previous_profit
                profit_changes.append(profit_change)
                months.append(row["Date"])

            # Update previous profit for the next iteration
            previous_profit = int(row["Profit/Losses"])

    # Calculate average change
    average_change = sum(profit_changes) / len(profit_changes)

    # Find greatest increase and decrease
    greatest_increase = max(profit_changes)
    greatest_decrease = min(profit_changes)

    # Find the corresponding months for greatest increase and decrease
    increase_month = months[profit_changes.index(greatest_increase)]
    decrease_month = months[profit_changes.index(greatest_decrease)]

    # Print the results to the terminal
    print("Financial Analysis")
    print("-------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_profit}")
    print(f"Average Change: ${average_change:.2f}")
    print(f"Greatest Increase in Profits: {increase_month} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})")

    # Save the results to a text file
    with open(output_file_path, 'w') as output_file:
        output_file.write("Financial Analysis\n")
        output_file.write("-------------------------\n")
        output_file.write(f"Total Months: {total_months}\n")
        output_file.write(f"Total: ${total_profit}\n")
        output_file.write(f"Average Change: ${average_change:.2f}\n")
        output_file.write(f"Greatest Increase in Profits: {increase_month} (${greatest_increase})\n")
        output_file.write(f"Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})\n")

# Call the function to analyze financial data and save results
analyze_financial_data(file_path, output_file_path)