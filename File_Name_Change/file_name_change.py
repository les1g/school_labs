# collect input
photo_file_names = input().strip()

# read file
with open(photo_file_names, 'r') as file_names:
    file_names_list = file_names.readlines() # store file contents as a list
    if not file_names_list:
        print("The file is empty")

# modify file
for name in file_names_list:
    # handle edge case when file is empty
    if name == '':
        print('Nothing to modify.')
    new_txt_file = name.replace('_photo.jpg', '_info.txt') # replace file name
    # put modified file name to output
    print(new_txt_file, end='')