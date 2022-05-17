import csv
from datetime import datetime
from operator import indexOf
# testing123
DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    return f"{temp}{DEGREE_SYBMOL}"

# 2021-07-05T07:00:00+08:00
# Monday 05 July 2021"


def convert_date(iso_string):
    cr_date = datetime.strptime(iso_string, '%Y-%m-%dT%H:%M:%S+08:00')
    cr_date = cr_date.strftime('%A %d %B %Y')
    return cr_date

    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    pass


def convert_f_to_c(temp_in_farenheit):
    farenheit = float(temp_in_farenheit)
    celsius = (farenheit - 32) / 1.8
    format_celsius = float("{:.1f}".format(celsius))
    return format_celsius


def calculate_mean(weather_data):
    total = 0
    for i in weather_data:
        i = float(i)
        total += i
    return total/(len(weather_data))


def load_data_from_csv(csv_file):

    with open(csv_file) as file:
        file_reader = csv.reader(file)
        next(file_reader)

        list = []

        for row in file_reader:
            if row == " ":
                continue
            # if not ''.join(row).strip():
            #     continue
            list.append(row[0:3])
            # list.append(row[1])
            # list.append(row[2])

        print(list[0], list[1], list[2])

        # if len(row) == 0:
        #     continue
        # list.append(row)

        # for i in list:
        #     i.split(" ")
        # return list

    # list = print(f", ".join(row))
    # return list

    # return file_reader
    # """Reads a csv file and stores the data in a list.

    # Args:
    #     csv_file: a string representing the file path to a csv file.
    # Returns:
    #     A list of lists, where each sublist is a (non-empty) line in the csv file.
    # """
    # pass


def find_min(weather_data):

    if weather_data == []:
        return ()

    minimum = float(weather_data[0])
    index_count = 0
    min_location = 0

    for i in weather_data:
        i = float(i)
        if i <= minimum:
            minimum = i
            min_location = index_count
        index_count += 1

    return (minimum, min_location)


def find_max(weather_data):

    if weather_data == []:
        return ()

    maximum = float(weather_data[0])
    index_count = 0
    max_location = 0

    for i in weather_data:
        i = float(i)
        if i >= maximum:
            maximum = i
            max_location = index_count
        index_count += 1

    return (maximum, max_location)


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass
