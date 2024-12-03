def modify_file_content(input_file, output_file):
    try:
        # Open the input file in read mode
        with open(input_file, 'r') as infile:
            content = infile.read()

        # Modify the content (Example: Convert text to uppercase)
        modified_content = content.upper()

        # Write the modified content to a new file
        with open(output_file, 'w') as outfile:
            outfile.write(modified_content)

        print(f"Modified content has been written to {output_file}")

    except FileNotFoundError:
        print(f"Error: The file {input_file} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


def read_file_with_error_handling():
    filename = input("Enter the filename to read: ")

    try:
        # Open the file in read mode
        with open(filename, 'r') as file:
            content = file.read()
            print("File content:")
            print(content)

    except FileNotFoundError:
        print(f"Error: The file {filename} does not exist.")
    except PermissionError:
        print(f"Error: You don't have permission to read the file {filename}.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def main():
    print("Choose an option:")
    print("1. Modify file content and write to a new file.")
    print("2. Read a file with error handling.")

    choice = input("Enter the number of your choice: ")

    if choice == '1':
        input_filename = input("Enter the name of the file to read: ")
        output_filename = input("Enter the name of the file to write: ")
        modify_file_content(input_filename, output_filename)
    elif choice == '2':
        read_file_with_error_handling()
    else:
        print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()
