import os

def count_files_in_directory():
    directory = os.getcwd()  # Get the current working directory
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    file_count = len(files)
    print(f'The number of files in the directory is: {file_count}')

# Call the function to count files and print the output
count_files_in_directory()