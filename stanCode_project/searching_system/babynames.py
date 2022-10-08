"""
File: babynames.py
Name: Neil
--------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import sys


def add_data_for_name(name_data, year, rank, name):
    """
    Adds the given year and rank to the associated name in the name_data dict.

    Input:
        name_data (dict): dict holding baby name data
        year (str): the year of the data entry to add
        rank (str): the rank of the data entry to add
        name (str): the name of the data entry to add

    Output:
        This function modifies the name_data dict to store the provided
        name, year, and rank. This function does not return any value.
    """
    name_d = {}
    name_d[year] = rank
    if name not in name_data:
        name_data[name] = name_d
    for p in name_data:
        if name == p:
            if year not in name_data[p] or rank < name_data[p][year]:
                name_data[p][year] = rank


def add_file(name_data, filename):
    """
    Reads the information from the specified file and populates the name_data
    dict with the data found in the file.

    Input:
        name_data (dict): dict holding baby name data
        filename (str): name of the file holding baby name data

    Output:
        This function modifies the name_data dict to store information from
        the provided file name. This function does not return any value.
    """
    with open(filename, 'r') as f:
        year = filename[filename.find('.txt')-4:filename.find('.txt')]
        for line in f:   # The type of line is string in the each line in the file.
            info_lst = line.split(',')  # Split the line into each list
            if len(info_lst) > 1:
                rank = info_lst[0].strip()  # strip is a method to erase the \n in the string.
                name1 = info_lst[1].strip()
                name2 = info_lst[2].strip()
                add_data_for_name(name_data, year, rank, name1)
                add_data_for_name(name_data, year, rank, name2)


def read_files(filenames):
    """
    Reads the data from all files specified in the provided list
    into a single name_data dict and then returns that dict.

    Input:
        filenames (List[str]): a list of filenames containing baby name data

    Returns:
        name_data (dict): the dict storing all baby name data in a structured manner
    """
    name_data = {}

    for filename in filenames:  # loop over each file
        # Using the constructed function 'add_file' to add each data of the files into name_data.
        add_file(name_data, filename)
    return name_data    # Return name_data to main function.


def search_names(name_data, target):
    """
    Given a name_data dict that stores baby name information and a target string,
    returns a list of all names in the dict that contain the target string. This
    function should be case-insensitive with respect to the target string.

    Input:
        name_data (dict): a dict containing baby name data organized by name
        target (str): a string to look for in the names contained within name_data

    Returns:
        matching_names (List[str]): a list of all names from name_data that contain
                                    the target string
    """
    target = target.lower()
    matching_name = []      # matching_name is a list that contain the whole name that consist with the condition.
    for name in name_data:
        num = 0     # 'num' is to check whether the name in name_data is consist with the condition we set.
        name = name.lower()
        for i in range(len(target)):
             for j in range(len(name)):

                if target[i] == name[i]:
                    num += 1
                if num == len(target):
                     matching_name.append(name)
    return matching_name


def print_names(name_data):
    """
    (provided, DO NOT MODIFY)
    Given a name_data dict, print out all its data, one name per line.
    The names are printed in alphabetical order,
    with the corresponding years data displayed in increasing order.

    Input:
        name_data (dict): a dict containing baby name data organized by name
    Returns:
        This function does not return anything
    """
    for key, value in sorted(name_data.items()):
        print(key, sorted(value.items()))


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # Two command line forms
    # 1. file1 file2 file3 ..
    # 2. -search target file1 file2 file3 ..

    # Assume no search, so list of filenames to read
    # is the args list
    filenames = args

    # Check if we are doing search, set target variable
    target = ''
    if len(args) >= 2 and args[0] == '-search':
        target = args[1]
        filenames = args[2:]  # Update filenames to skip first 2

    # Read in all the filenames: baby-1990.txt, baby-2000.txt, ...
    names = read_files(filenames)

    # Either we do a search or just print everything.
    if len(target) > 0:
        search_results = search_names(names, target)
        for name in search_results:
            print(name)
    else:
        print_names(names)


if __name__ == '__main__':
    main()
