import csv
from datetime import datetime
from email import header
from operator import indexOf

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    return f"{temp}{DEGREE_SYBMOL}"


def convert_date(iso_string):
    cr_date = datetime.strptime(iso_string, '%Y-%m-%dT%H:%M:%S+08:00')
    cr_date = cr_date.strftime('%A %d %B %Y')
    return cr_date


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
            if not row:
                continue
            row[1] = int(row[1])
            row[2] = int(row[2])
            list.append(row)
        return list


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

    minimum = weather_data[0][1]

    min_day = weather_data[0][0]

    for i in weather_data:

        if i[1] <= minimum:
            minimum = i[1]
            min_day = i[0]

    min_day = convert_date(min_day)

    minimum = convert_f_to_c(minimum)
    minimum = format_temperature(minimum)

    maximum = weather_data[0][2]
    max_day = weather_data[0][0]

    for i in weather_data:
        if i[2] >= maximum:
            maximum = i[2]
            max_day = i[0]

    max_day = convert_date(max_day)

    maximum = convert_f_to_c(maximum)
    maximum = format_temperature(maximum)

    low_total = 0

    for i in weather_data:
        low_total += i[1]

    low_total = low_total/(len(weather_data))

    low_total = convert_f_to_c(low_total)
    low_total = format_temperature(low_total)

    high_total = 0
    result = ""
    for i in weather_data:
        high_total += i[2]

    high_total = high_total/(len(weather_data))

    high_total = convert_f_to_c(high_total)
    high_total = format_temperature(high_total)

    num_days = len(weather_data)
    result += f"{num_days} Day Overview\n"
    result += f"  The lowest temperature will be {minimum}, and will occur on {min_day}.\n"
    result += f"  The highest temperature will be {maximum}, and will occur on {max_day}.\n"
    result += f"  The average low this week is {low_total}.\n"
    result += f"  The average high this week is {high_total}.\n"
    return result


def generate_daily_summary(weather_data):

    new_list = []

    for i in weather_data:
        new_list.append(convert_date(i[0]))
        new_list.append(convert_f_to_c(i[1]))
        new_list.append(convert_f_to_c(i[2]))

    weather_data_list = [new_list[i:i + 3] for i in range(0, len(new_list), 3)]

    result = ""
    for i in range(len(weather_data_list)):
        expected_date = weather_data_list[i][0]
        min_temp = format_temperature(weather_data_list[i][1])
        max_temp = format_temperature(weather_data_list[i][2])
        result += f"---- {expected_date} ----\n"
        result += f"  Minimum Temperature: {min_temp}\n"
        result += f"  Maximum Temperature: {max_temp}\n\n"

    return result
