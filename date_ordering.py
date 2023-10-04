from datetime import datetime
import os.path
from date_difference import Date


def create_timeline():
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

    return dates


def save_timeline(dates, file_path):
    try:
        with open(file_path, 'a') as file:
            for date in dates:
                formatted_date = date.strftime("%Y-%m-%d")
                file.write(formatted_date + '\n')
        print("Timeline appended successfully!")
    except IOError:
        print("An error occurred while appending the timeline.")


def create_or_append_timeline():
    choice = input("Do you want to create a new timeline or append to an existing one? (create/append): ")
    if choice.lower() == 'create':
        return create_timeline()
    elif choice.lower() == 'append':
        file_path = input("Enter the file path of the existing timeline: ")
        if not os.path.isfile(file_path):
            print("File does not exist. Creating a new timeline instead.")
            return create_timeline()
        else:
            return file_path
    else:
        print("Invalid choice. Creating a new timeline instead.")
        return create_timeline()


# Main program flow
timeline_data = create_or_append_timeline()

if isinstance(timeline_data, list):
    # If timeline_data is a list, it means a new timeline was created
    print("Timeline:")
    for date in timeline_data:
        formatted_date = date.strftime("%Y-%m-%d")
        print(formatted_date)

    file_path = input("Enter the file path to save the timeline: ")
    save_timeline(timeline_data, file_path)
else:
    # If timeline_data is a string, it means an existing timeline was appended
    file_path = timeline_data
    timeline = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            try:
                date = datetime.strptime(line, "%Y-%m-%d")
                timeline.append(date)
            except ValueError:
                print(f"Invalid date format found in {file_path}: {line}")

    print("Updated Timeline:")
    for date in timeline:
        formatted_date = date.strftime("%Y-%m-%d")
        print(formatted_date)

    save_timeline(timeline, file_path)
