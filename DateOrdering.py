from datetime import datetime

# Prompt the user to enter the dates
print("Enter the dates (Press Enter when done):")
dates = []
while True:
    date_input = input("Date (YYYY-MM-DD): ")
    if not date_input:
        break

    # Parse the inputted dates
    try:
        date = datetime.strptime(date_input, "%Y-%m-%d")
        dates.append(date)
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")

# Sort the dates in ascending order
dates.sort()

# Print the timeline
print("Timeline:")
for date in dates:
    formatted_date = date.strftime("%Y-%m-%d")
    print(formatted_date)
