import random

def shuffle_file_lines(filename):
    """
    Shuffles the lines of text in a file and rewrites the shuffled content back to the same file.

    Args:
        filename (str): The path to the text file.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        random.shuffle(lines)

        with open(filename, 'w', encoding='utf-8') as file:
            file.writelines(lines)

        print(f"Successfully shuffled lines in '{filename}'.")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    file_to_shuffle = input("Enter the path to the text file you want to shuffle: ")
    shuffle_file_lines(file_to_shuffle)
