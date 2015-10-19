#!/usr/bin/python

from __future__ import print_function
import sys
try:
    import json
    import jinja2
except ImportError as e:
    print("Unable to import some modules" + str(e))
    sys.exit(1)

# Declaring some global variables
MASTER_DICT = {}
# Trying to separate View from Logic and so, we have a jinja template file here.
HTML_TEMPLATE = "template.j2"
# Output file
HTML_OUTPUT = "index.html"

def usage():
    """ Just to print the usage of the script compare_ilo_ahs.py """
    print("""Usage:
        This script accepts two files as arguments to compare and prints out the results in html format.
        {0} path_to_file1 path_to_file2 """.format(sys.argv[0]))
    sys.exit(1)


def loadjson(path_to_file1, path_to_file2):
    """
    :param path_to_file1: Takes the path of file1
    :param path_to_file2: Takes the path of file2
    :return: Returns a tuple of dictionaries with loaded data from json files.
    """
    try:
        with open(path_to_file1) as data_file1, open(path_to_file2) as data_file2:
            return json.load(data_file1), json.load(data_file2)
    except EnvironmentError as e:
        print("Oh Boy, Something went really wrong in loading the files: " + str(e))
        sys.exit(1)


def format_results(data, item):
    """
    :param data: Take a tuple of dictionaries to compare and then modifies the MASTER_DICT.
    """
    MASTER_DICT[item] = MASTER_DICT.setdefault(item, [])
    union_of_keys = data[0].keys() + data[1].keys()
    current_item = {}
    for key in union_of_keys:
        element1 = data[0].setdefault(key, "No_Data")
        element2 = data[1].setdefault(key, "No_Data")
        if element1 == element2:
            status = "PASS"
        else:
            status = "FAIL"
        current_item[key] = [element1, element2, status]
    MASTER_DICT[item].append(current_item)


def compare(data1, data2):
    """
    :param file1_data: Takes a first file data as a dictionary
    :param file2_data: Takes a second file data as a dictionary
    """
    common_keys = []
    for key in data1:
        if key in data2:
            common_keys.append(key)
    # print(common_keys)

    for common_key in common_keys:
        if len(data1[common_key]) == len(data2[common_key]):
            for d1 in zip(data1[common_key], data2[common_key]):
                format_results(d1, common_key)
        else:
            print("Mismatch found. Ignoring!")


def render(master_dict):
    """
    :param master_dict: Takes a dictionary and creates a html page using the HTML_TEMPLATE file and jinja2 engine.
    """
    templateLoader = jinja2.FileSystemLoader(searchpath=".")
    templateEnv = jinja2.Environment(loader=templateLoader)
    template = templateEnv.get_template(HTML_TEMPLATE)
    templateVars = {"favorites": MASTER_DICT}
    outputText = template.render(templateVars)
    with open(HTML_OUTPUT, "w") as text_file:
        text_file.write(outputText)
    print("index.html file has been created")
    sys.exit(0)


# Just to make this script a module, so that others can import the functions if needed.
if __name__ == "__main__":
    if len(sys.argv) != 3:
        usage()
    else:
        data1, data2 = loadjson(sys.argv[1], sys.argv[2])
        compare(data1, data2)
        render(MASTER_DICT)
