# Complete the following functions.
# Please do not rename or modify the function names or parameters as this may cause the grader to crash.
# For all the questions given below, your program needs to read the the us_city_population.txt file.

# HINTS:
# the split function is your friend! https://www.programiz.com/python-programming/methods/string/split
# The readlines() function might be helpful to you. Check the code example in method 1: https://www.geeksforgeeks.org/read-a-file-line-by-line-in-python/

# Q1) Write a function that reads the us_city_population.txt file,
# and returns a list of cities that have 1 million or more residents.
# To receive full credit, the list needs to be sorted alphabetically.
def big_cities():
    ''' 4 Line solution for fun '''
    # with open("us_city_population.txt", "r") as file:
    #     cities = [line[0] for line in [line.strip().split(',')
    #                                    for line in file.readlines()] if int(line[2]) >= 1000000]
    #     cities.sort()
    #     return cities

    # Open file and read lines into variable {lines}
    file = open("us_city_population.txt", "r")

    # Strip the newline character and split for each line in file
    lines = file.readlines()

    # Create an empty list to store output
    cities = []

    for line in lines:
        city = line.split(',')[0]
        population = int(line.split(',')[2].strip())

        if population >= 1000000:
            cities.append(city)

    file.close()
    cities.sort()
    return cities

# Q2) Write a function that reads the us_city_population.txt file and
# returns a dictionary indicating how many cities we have from each state.
# For instance, if we have 10 cities from CA, one entry in the dictionary should be "CA" : 10
# Hint: checkout the split function in python
def state_city_count():
    # Open file and read lines into variable {lines}
    file = open("us_city_population.txt", "r")
    lines = file.readlines()

    # Create an empty dictionary to store output
    states = dict()

    # Loop through the list of lines
    for line in lines:
        state = line.split(',')[0]


        if state in states:
            cities[city] += 1

        else:
            city['state'] = 0
    return {}

# Q3) Some cities in different states have the same names.
# For instance, Selma is a city in both CA and AL, while Sun City is both in AZ and CA.
# Write a function that returns a list of popular city names
# (defined as names that appear at least 7 times in the file).
# Washington is one such name, appearing 7 times in the file.
# The list should include each city only once.
# To receive full credit, the list must be sorted alphabetically and the list must contain only city names (no state or population information)
# def popular_names():
#     return []


# Q4) Write a function that takes line number as input and returns the name of the city on that line.
# For instance, if the input is 2, your function should return the string "Albertville" (not the whole line!)
# If the input is an invalid number (negative number, zero, too large), return an empty string.
# def city_on_line(line_number):
#     return ""
