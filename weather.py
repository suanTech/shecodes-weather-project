import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    date = datetime.fromisoformat(iso_string)
    return date.strftime('%A %d %B %Y')


def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    temp_in_celcius = (float(temp_in_farenheit) - 32) * 5/9
    return round(temp_in_celcius, 1)


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    # for i in range(len(weather_data)):
    #     total_value += float(weather_data[i])
    total = sum([float(num) for num in weather_data])
        
    return total / len(weather_data)
    

def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    rows = []
    with open(csv_file, newline='') as f:
        reader = csv.reader(f)
        # skip header
        next(reader)
        for row in reader:
            date = row[0]
            min_temp = int(row[1])
            max_temp = int(row[2])
            rows.append([date, min_temp, max_temp])
    return rows

def find_last_occurence(list, value):
    """Finds the last occurence of item in the list.

    Args:
        list: A list of numbers.
        value: A matching item in the list.
    Returns:
        The last index of the matching item.
    """
    all_indexes = []
    for i in range(len(list)):
        if list[i] == value:
            all_indexes.append(i)
    return max(all_indexes)

def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
    if len(weather_data) > 0:
        min_value = min(weather_data)
        return float(min(weather_data)), find_last_occurence(weather_data, min_value)
    else:
        return ()

def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    if len(weather_data) > 0:
        max_value = max(weather_data)
        return float(max(weather_data)), find_last_occurence(weather_data, max_value)
    else:
        return ()
    
def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    # Get lists of minimum and maximum temperatures
    all_min_temp = []
    all_max_temp = []
    for i in range(len(weather_data)):
        all_min_temp.append(weather_data[i][1]) 
        all_max_temp.append(weather_data[i][2])

    days_count = len(weather_data)
    summary = f"{days_count} Day Overview\n"

    min_temp_in_f, min_pos = find_min(all_min_temp)
    min_day = convert_date(weather_data[min_pos][0])
    summary += f"  The lowest temperature will be {convert_f_to_c(min_temp_in_f)}°C, and will occur on {min_day}.\n"

    max_temp_in_f, max_pos = find_max(all_max_temp)
    max_day = convert_date(weather_data[max_pos][0])
    summary += f"  The highest temperature will be {convert_f_to_c(max_temp_in_f)}°C, and will occur on {max_day}.\n"

    min_average_in_f = calculate_mean(all_min_temp)
    max_average_in_f = calculate_mean(all_max_temp)
    summary += f"  The average low this week is {convert_f_to_c(min_average_in_f)}°C.\n"
    summary += f"  The average high this week is {convert_f_to_c(max_average_in_f)}°C.\n"
    return summary


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    summary = ""
    for data in weather_data:
        summary += f"---- {convert_date(data[0])} ----\n"
        summary += f"  Minimum Temperature: {convert_f_to_c(data[1])}°C\n"
        summary += f"  Maximum Temperature: {convert_f_to_c(data[2])}°C\n\n"
    return summary
