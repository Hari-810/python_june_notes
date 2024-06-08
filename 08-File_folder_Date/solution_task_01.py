import os

def create_file(file_name):
    try:
        with open(file_name, 'w') as file:
            print(f"File '{file_name}' created successfully.")
    except OSError as e:
        print(f"Error: {e}")

def write_to_file(file_name, content):
    try:
        with open(file_name, 'w') as file:
            file.write(content)
            print(f"Content written to '{file_name}' successfully.")
    except OSError as e:
        print(f"Error: {e}")

def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print(f"Content of '{file_name}':\n{content}")
    except FileNotFoundError as e:
        print(f"Error: {e}")

def append_to_file(file_name, content):
    try:
        with open(file_name, 'a') as file:
            file.write(content)
            print(f"Content appended to '{file_name}' successfully.")
    except OSError as e:
        print(f"Error: {e}")

def create_folder(folder_name):
    try:
        os.mkdir(folder_name)
        print(f"Folder '{folder_name}' created successfully.")
    except FileExistsError:
        print(f"Folder '{folder_name}' already exists.")
    except OSError as e:
        print(f"Error: {e}")

def list_files_in_folder(folder_name):
    try:
        files = os.listdir(folder_name)
        print(f"Files in folder '{folder_name}':")
        for file in files:
            print(file)
    except FileNotFoundError as e:
        print(f"Error: {e}")

# Example usage
def main():
    while True:
        print("\nChoose an option:")
        print("1. Create a file")
        print("2. Write to a file")
        print("3. Read from a file")
        print("4. Append to a file")
        print("5. Create a folder")
        print("6. List files in a folder")
        print("7. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            file_name = input("Enter file name: ")
            create_file(file_name)
        elif choice == '2':
            file_name = input("Enter file name: ")
            content = input("Enter content: ")
            write_to_file(file_name, content)
        elif choice == '3':
            file_name = input("Enter file name: ")
            read_file(file_name)
        elif choice == '4':
            file_name = input("Enter file name: ")
            content = input("Enter content to append: ")
            append_to_file(file_name, content)
        elif choice == '5':
            folder_name = input("Enter folder name: ")
            create_folder(folder_name)
        elif choice == '6':
            folder_name = input("Enter folder name: ")
            list_files_in_folder(folder_name)
        elif choice == '7':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
