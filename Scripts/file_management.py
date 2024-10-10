import os


def create_folder_with_filename(path):
    if not os.path.isdir(path):
        directory = os.path.dirname(path)
        filename = os.path.splitext(os.path.basename(path))[0]

        new_folder_path = os.path.join(directory, filename)

        if not os.path.exists(new_folder_path):
            # Create new folder
            os.makedirs(new_folder_path)
            print("Created new folder at " + new_folder_path)

        else:
            print(path + " is already a directory")


def scan_directory(directory_path):
    for item in os.listdir(directory_path):
        item_path =  os.path.join(directory_path, item)
        if os.path.isfile(item_path):
            create_folder_with_filename(item_path)        

path = "your path"
scan_directory(path)