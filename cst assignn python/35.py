
def sort_dict_list(dict_list, key):
    """Sorts a list of dictionaries by the specified key."""
    try:
        
        sorted_list = sorted(dict_list, key=lambda x: x[key])
        return sorted_list
    except KeyError:
        print(f"Error: The key '{key}' is not found in one or more dictionaries.")
    except Exception as e:
        print(f"Unexpected error: {e}")


def main():
    
    people = [
        {"name": "John", "age": 25},
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 20}
    ]

    print("Original list of dictionaries:")
    print(people)

    sorted_people = sort_dict_list(people, "age")

    if sorted_people:
        print("\nSorted list by 'age':")
        print(sorted_people)

   
    sorted_people_by_name = sort_dict_list(people, "name")

    if sorted_people_by_name:
        print("\nSorted list by 'name':")
        print(sorted_people_by_name)

if __name__ == "__main__":
    main()
