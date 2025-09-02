def list_files(parent_directory, current_filepath=""):
    file_paths = []

    for name, value in parent_directory.items():
        # Update the current file_path
        new_file_path = current_filepath + "/" + name
        # check if its a file
        if value is None:
            file_paths.append(new_file_path)

        # else it's a directory call it recursively, returns a list
        else:
            file_paths.extend(list_files(value, new_file_path))


    return file_paths
            

        
