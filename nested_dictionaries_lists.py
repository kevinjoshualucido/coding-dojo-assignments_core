# 1


x = [[5, 2, 3], [10, 8, 9]]
students = [
    {"first_name": "Michael", "last_name": "Jordan"},
    {"first_name": "John", "last_name": "Rosales"},
]
sports_directory = {
    "basketball": ["Kobe", "Jordan", "James", "Curry"],
    "soccer": ["Messi", "Ronaldo", "Rooney"],
}
z = [{"x": 10, "y": 20}]


# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
print(x)
x[1][0] = 15
print(x)
# Change the last_name of the first student from 'Jordan' to 'Bryant'
print(students[0])
students[0]["last_name"] = "Bryant"
print(students[0])
# In the sports_directory, change 'Messi' to 'Andres'
print(sports_directory["soccer"])
sports_directory["soccer"][0] = "Andres"
print(sports_directory["soccer"])
# Change the value 20 in z to 30
print(z)
z[0]["y"] = 30
print(z)


print("==============================\n==============================")

# 2


students = [
    {"first_name": "Michael", "last_name": "Jordan"},
    {"first_name": "John", "last_name": "Rosales"},
    {"first_name": "Mark", "last_name": "Guillen"},
    {"first_name": "KB", "last_name": "Tonel"},
]


def iterateDictionary(list):
    for s in range(0, len(list)):
        output = ""
        for first_var, sec_var in list[s].items():
            output += first_var + " - " + sec_var + " "
        print(output)


iterateDictionary(students)


print("==============================\n==============================")


# 3


def iterateDictionary2(stu_name, list):
    for i in range(0, len(list)):
        for key, val in list[i].items():
            if key == stu_name:
                print(val)


iterateDictionary2("last_name", students)


print("==============================\n==============================")


# 4


dojo = {
    "locations": ["San Jose", "Seattle", "Dallas", "Chicago", "Tulsa", "DC", "Burbank"],
    "instructors": [
        "Michael",
        "Amy",
        "Eduardo",
        "Josh",
        "Graham",
        "Patrick",
        "Minh",
        "Devon",
    ],
}


def print_info(dojo_dict):
    for key, val in dojo_dict.items():
        print("---")
        print(f"{len(val)} {key}")
        for i in range(0, len(val)):
            print(val[i])


print_info(dojo)
