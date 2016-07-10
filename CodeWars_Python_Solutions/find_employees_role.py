def find_employees_role(name):

    split_name = name.split()

    if len(split_name) <= 1:
        return "Does not work here!";

    first_name = name.split(' ')[0]
    last_name = name.split(' ')[1]

    return (next((item['role'] for item in employees if item["first_name"] ==  first_name and item["last_name"] == last_name),'Does not work here!'))