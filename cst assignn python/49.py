##49.	Develop a function that sorts a list of dictionaries based on the values of a specific key.
def sort_dicts_by_key(dict_list,key):

    return sorted(dict_list,key=lambda x: x.get(key))

data=[
    {"name":"nikhil","age":20},
    {"name":"devanshu","age":19},
    {"name":"tanisha","age":19}
]

sorted_data = sort_dicts_by_key(data,'age')
print(sorted_data)