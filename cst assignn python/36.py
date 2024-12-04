def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print("File content:")
            print(content)
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")
    except Exception as e:
        print(f"Unexpected error: {e}")

def main():
    file_name = input("Enter the name of the file to read: ")
    read_file(file_name)

if __name__ == "__main__":
    main()
