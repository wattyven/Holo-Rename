import os

# CHANGE THESE VARIABLES AS NEEDED
directory = r'YOUR\DIRECTORY\HERE'
wrong_encoding = 'cp437'
correct_encoding = 'cp932'

def rename_files(directory):
    # topdown=False to walk directory tree from bottom to top
    for root, dirs, files in os.walk(directory, topdown=False):
        for file in files:
            try:
                # define original + new file paths
                original_file_path = os.path.join(root, file)
                new_file_path = os.path.join(root, file.encode(wrong_encoding).decode(correct_encoding))
                os.rename(original_file_path, new_file_path)
                # print(f"Renamed file {original_file_path} to {new_file_path}")
            except Exception as e:
                print(f"Failed to rename {file}: {e}")

        for dir in dirs:
            try:
                # define original + new directory paths
                original_dir_path = os.path.join(root, dir)
                new_dir_path = os.path.join(root, dir.encode(wrong_encoding).decode(correct_encoding))
                os.rename(original_dir_path, new_dir_path)
                # print(f"Renamed directory {original_dir_path} to {new_dir_path}")
            except Exception as e:
                print(f"Failed to rename {dir}: {e}")

rename_files(directory)
