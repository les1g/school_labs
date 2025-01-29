# collect file name from user
photo_file_names = input().strip()

# read the file contents
with open(photo_file_names, 'r') as file_names:
    file_names_list = file_names.readlines() # store file contents as a list