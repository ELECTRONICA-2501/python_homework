
import csv
import os
employees = ''
#os.getenv(get_this_value)
import custom_module
from datetime import datetime


def read_employees():
    #dict = {"feilds", "rows"} this is a set not a dict

    employee_dict = {"fields": [], "rows": []}
    #rows = []
    #key_dict = dict.keys()
    try:
        with open('../csv/employees.csv', 'r') as file:
            csv_content = csv.reader(file)
            first_row = next(csv_content)
            employee_dict["fields"] = first_row

            for row in csv_content:
                #employee_dict["fields"] = first_row
                employee_dict["rows"].append(row)
                # key = row[first_row] #store first row in the dict using key "fields"
                # rows = row[1:] #meant to store all the other rows besides the first in rows list
            return employee_dict
        
    except TypeError as e:
        print(f"error: {e}")

        return None
    

#task 3
    
employees = read_employees()
print(employees)
# Create a function called column_index. The input is a string. The function looks in employees["fields"] (an array of column headers) to find the index of the column header requested. There won't be much to this function, because you just use the index() method of the list class, like so:

# employees["fields"].index("first_name")

# The index() method returns the index of the matching value from the list.

# 1. The column_index function should return this index.

# 2. Run the test again to see if the test passes.

# 3. Call the column_index function in your program, passing the parameter "employee_id".  Store the column you get back in a variable called employee_id_column.  This global value is used for subsequent steps.



def column_index(str):
    try: 
        return employees["fields"].index(str)
            # looks at employees keys in fields, the .index() function works to find the index(position) of the first occurrence of a specified value withing a list or a string: 
            # my_list = ['apple', 'banana', 'cherry', 'banana', 'date']
            # index = my_list.index('banana')
            # print(index)
            # output is : 1
    except TypeError:
        print(f"Column index'{str} not found" )
        return None
    
employee_id_column = column_index("employee_id")
last_name_column = column_index("last_name")

def first_name(row_number):
    try:
        first_name_index = column_index("first_name")
        column_index("first_name")
        return employees["rows"][row_number][first_name_index]
    except ValueError:
        print(f"requested row:  {row_number} not found")

def employee_find(employee_id): #lets say we want to find employee who has 3 as their id num
    try:
       # you dont need a for loop, just work with the column index
        def employee_match(row): # we enter our code and start with the row, we want to return an int (index) for the
            
            return int(row[employee_id_column]) == employee_id
        matches = list(filter(employee_match, employees["rows"]))
        return matches
        #filter(function, iterable)
        # the function that tests each element of the iterable, it should return TRUE if the element is to be included in the result, otherwise false. 
        # iterable is the collection to be filtered, in this case a dictionary "rows"
    except TypeError as e:
        print(f"row numb not found: {row}")

print(3*"\n")
ya = employee_find(3)
print(ya)
# returns: [['3', 'Lauren', 'Martinez', '+250 8878764159']] hence func works.

#Lambda time
#task 6

def employee_find_2(employee_id):
    matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
    return matches

# task 7
def sort_by_last_name():
    #figure out which index column corresponds to last_name
    employees["rows"].sort(key = lambda row: row[last_name_column])
    return employees["rows"]

#task 8
def employee_dict(row):

    employee_id_index = employees["fields"].index("employee_id")
    headers = [field for i, field in enumerate(employees["fields"]) if i != employee_id_index]
    row_vals = [value for i, value in enumerate(row) if i != employee_id_index]

    employee_data = dict(zip(headers, row_vals))
    return employee_data

#task 9

def all_employees_dict():
    #create an empty dict
    employee_values = {}

    #find where employee id is stored
    employee_id_index = employees["fields"].index("employee_id")

    #loop
    for row in employees["rows"]:
        #grab the employee id
        emp_id = row[employee_id_index]
        emp_dict = employee_dict(row)
        employee_values[emp_id] = emp_dict
    return employee_values
print("\n")
print(all_employees_dict)


#task 10
def get_this_value():
    return os.getenv('THISVALUE')


#task 11
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

set_that_secret("Eid Mubarak")
print(custom_module.secret)

#task 12

# def read_minutes():

#     minutes1 = read_single_csv("../csv/minutes1.csv")
#     minutes2 = read_single_csv("../csv/minutes2.csv")


#     tuple_of_min1 = tuple(tuple(minutes1) for row in minutes1)
#     tuple_of_min2 = tuple(tuple(minutes2) for row in minutes2)


#     return minutes1, minutes2

def read_single_csv(path):
    # Open CSV file
    with open(path, "r", newline="", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)

        # First row = field names
        fields = next(reader)

        # Convert the rest of the rows to tuples
        rows = [tuple(row) for row in reader]

    return {
        "fields": fields,
        "rows": rows
    }

def read_minutes():
    # Use the helper twice
    minutes1 = read_single_csv("../csv/minutes1.csv")
    minutes2 = read_single_csv("../csv/minutes2.csv")

    return minutes1, minutes2


minutes1, minutes2 = read_minutes()
print(minutes1)
print(minutes2)

#task 13
def create_minutes_set():
    hashset1 = set(minutes1["rows"])
    hashset2 = set(minutes2["rows"])

    union_set = hashset1.union(hashset2)

    return union_set

minutes_set = create_minutes_set()
print(minutes_set)

#task 14
def create_minutes_list():
    tmp_list = list(minutes_set)
    res = list(map(lambda x: (x[0], datetime.strptime(x[1],"%B %d, %Y" )), tmp_list))
    return res

# task 15
def write_sorted_list():
    sorted_list = sorted(minutes_list, key = lambda x: x[1])
    result = list(map(lambda x:(x[0], x[1].strftime("%B %d, %Y")),
        sorted_list))
    
    with open("./minutes.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        
        # Write the header from minutes1["fields"]
        writer.writerow(minutes1["fields"])
        
        # Write each row
        for row in result:
            writer.writerow(row)
    
    return result

minutes_list = create_minutes_list()  
print(minutes_list)                   

converted_list = write_sorted_list()  
print(converted_list) 