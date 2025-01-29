# collect input
photo_file_names = input().strip()

# handle exceptions
try:
    # read file
    with open(photo_file_names, 'r') as file_names:
        file_names_list = file_names.readlines() # store file contents as a list
        if not file_names_list:
            print("The file is empty")

except FileNotFoundError:
    print(f'The file {photo_file_names} does not exist.')
    
# modify file
for name in file_names_list:
    # handle edge case when file has empty new line
    if name == '\n':
        print('Nothing to modify.', end='')
    new_txt_file = name.replace('_photo.jpg', '_info.txt') # replace file name
    # put modified file name to output
    print(new_txt_file, end='')