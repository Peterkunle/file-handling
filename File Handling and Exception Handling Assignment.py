def read_and_modify_file():
    # Ask the user for the input file name
    filename = input("Enter the name of the file to read: ")

    try:
        # Open the file in read mode
        with open("Keyboard lesson", "r") as file:
            content = file.read()
        
        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()

        # Write the modified content to a new file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)
        
        print(f"Modified content has been written to '{new_filename}'")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except IOError:
        print(f"Error: Could not read the file '{filename}'.")

# Run the program
read_and_modify_file()
