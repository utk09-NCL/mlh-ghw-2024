# Function to allow the user to write a poem
def write_poem():
    print("Please write your poem (type 'exit' on a new line to finish):\n")

    # List to store each line of the poem
    poem_lines = []

    # Continue taking input until the user types 'exit'
    while True:
        line = input()
        if line.lower() == 'exit':
            break
        poem_lines.append(line)

    # Join the lines to create the complete poem
    return '\n'.join(poem_lines)


# Function to save the poem to a specified file
def save_poem(poem, file_name):
    try:
        # Open the file in write mode and save the poem
        with open(file_name, 'w') as file:
            file.write(poem)
        print(f'\nPoem successfully saved to {file_name}.')
    except Exception as e:
        # Handle any exceptions that might occur during the file saving process
        print(f'\nError occurred while saving the poem: {str(e)}')


# Function to read and display the contents of a file
def read_and_display_poem(file_name):
    try:
        # Open the file in read mode and read the content
        with open(file_name, 'r') as file:
            poem_content = file.read()
            print(f'\nContents of {file_name}:\n')
            print(poem_content)
    except FileNotFoundError:
        # Handle the case when the file is not found
        print(f"\nThe file '{file_name}' does not exist.")
    except Exception as e:
        # Handle any other exceptions that might occur during the file reading process
        print(f'\nError occurred while reading the poem: {str(e)}')


# Main function to orchestrate the process
def main():
    # Get the poem from the user
    poem_content = write_poem()

    # Get the file name from the user
    file_name = input(
        "\nEnter the file path to save the poem (include the extension, e.g., beginners_week/poem.txt): ")

    # Save the poem to the specified file
    save_poem(poem_content, file_name)

    # Read and display the contents of the saved file
    print("\nLet's read the poem we just saved.\n")
    print("-----------------------------------\n")
    read_and_display_poem(file_name)
    print("\n-----------------------------------")


# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()
