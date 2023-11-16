import os

def create_shortcut(source_folder, destination_folder):
    # Loop through all directories and files in the source_folder and filter by extention
    for root, dirs, files in os.walk(source_folder):
        target_files = [file for file in files if file.endswith('.py')]
        
        for file in target_files:
            file_path = os.path.join(root, file)
            destination_path = os.path.join(destination_folder, file)
            
            # Check if the shortcut already exists in the destination_folder
            if not os.path.exists(destination_path):
                os.symlink(file_path, destination_path)
                print(f"Shortcut created for: {file_path} --> {destination_path}")
            else:
                print(f"File already exists in the destination: {destination_path}")

source_directory = '/your/source/directory/here'
destination_directory = '/your/destination/directory/here'

create_shortcut(source_directory, destination_directory)
