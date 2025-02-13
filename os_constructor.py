import os

def main():
    try:
        # Get current working directory
        current_dir = os.getcwd()
        print(f"Current working directory: {current_dir}")

        # List directory contents
        dir_contents = os.listdir()
        print("Directory contents:", dir_contents)

        # Create a new directory if it doesn't exist
        new_dir_name = "new_directory"
        if not os.path.exists(new_dir_name):
            os.makedirs(new_dir_name)
            print(f"Created new directory: {new_dir_name}")
        else:
            print(f"Directory '{new_dir_name}' already exists")

        # Change the current working directory
        try:
            os.chdir(new_dir_name)
            print(f"Changed to directory: {os.getcwd()}")
        except PermissionError:
            print(f"Permission denied when trying to change to {new_dir_name}")

        # Example of file creation (safely)
        file_name = "example.txt"
        with open(file_name, "w") as file:
            file.write("This is a test file.")
        print(f"Created file: {file_name}")

        # Safely remove the file we just created
        if os.path.exists(file_name):
            os.remove(file_name)
            print(f"Removed file: {file_name}")
        else:
            print(f"File {file_name} does not exist to remove.")

    except FileNotFoundError as e:
        print(f"File or directory not found: {e}")
    except PermissionError as e:
        print(f"Permission error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
