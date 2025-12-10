import os


def find(path, dir_name):
    try:
        entries = os.listdir(path)
    except PermissionError:
        return
    except FileNotFoundError:
        print(f"Path {path} not found.")
        return

    for entry in entries:
        full_path = os.path.join(path, entry)

        if os.path.isdir(full_path):
            if entry == dir_name:
                print(os.path.abspath(full_path))

            # Recurse into the directory to search in its subdirectories
            find(full_path, dir_name)
