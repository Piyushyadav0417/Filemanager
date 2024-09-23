import os
import time
import shutil

def Create_file(Filename):
    try:
        DisalloChar = '\/:*?"<>|'
        for char in Filename:
            if char in DisalloChar:
                print("A file name can't contain any of the following characters; \\/:*?\"<>|")
                return  # Exit early if invalid character found
        with open(Filename, 'x') as f:
            print(f"{Filename} is created successfully!")
    except FileExistsError:
        print(f"{Filename} already exists!")
    except Exception as e:
        print(f"An error occurred: {e}")


def View_files(file_type=None):
    try:
        files = os.listdir()
        if not files:
            print("No files found")
            return  # Early return if no files

        elif file_type:
            files = [file for file in files if file.endswith(file_type)]
        
        elif not files:
            print(f"No files found with the type '{file_type}'")
            return

        print("Files in directory:")
        for file in files:
            file_stat = os.stat(file)
            size = file_stat.st_size
            modified_time = time.ctime(file_stat.st_mtime)
            print(f"{file} - Size: {size} bytes, Last Modified: {modified_time}")
    except Exception as e:
        print(f"An error occurred: {e}")


def Delete_file(Filename):
    try:
        confirm = input(f"Are you sure you want to delete {Filename}? (Y/N): ").lower()
        if confirm == 'y':
            os.remove(Filename)
            print(f"{Filename} deleted successfully!")
        else:
            print(f"Deletion of {Filename} cancelled.")
    except FileNotFoundError:
        print(f"{Filename} not found")
    except Exception as e:
        print(f"An error occurred: {e}")


def Read_file(Filename):
    try:
        with open(Filename, 'r') as f:
            content = f.read()
            print(f"The content of {Filename} is:\n{content}")
    except FileNotFoundError:
        print(f"{Filename} not found")
    except Exception as e:
        print(f"An error occurred: {e}")

def Edit_file(Filename):
    try:
        with open(Filename, 'a') as f:
            content = input("Write in file: ")
            f.write(content + '\n')
            print("Content added successfully.")
    except FileNotFoundError:
        print(f"{Filename} not found")
    except Exception as e:
        print(f"An error occurred: {e}")

def Search_file(keyword):
    try:
        files = os.listdir()
        found_files = [file for file in files if keyword in file]
        if not found_files:
            print(f"No files found with the keyword '{keyword}'")
        else:
            print("Matching files:")
            for file in found_files:
                print(file)
    except Exception as e:
        print(f"An error occurred: {e}")
def Rename_file(old_name, new_name):
    try:
        os.rename(old_name, new_name)
        print(f"{old_name} has been renamed to {new_name}")
    except FileNotFoundError:
        print(f"{old_name} not found")
    except Exception as e:
        print(f"An error occurred: {e}")

BACKUP_DIR = "backup"

# Ensure the backup directory exists
if not os.path.exists(BACKUP_DIR):
    os.makedirs(BACKUP_DIR)

def Backup_file(Filename):
    try:
        shutil.copy(Filename, BACKUP_DIR)
        print(f"{Filename} backed up successfully!")
    except FileNotFoundError:
        print(f"{Filename} not found")
    except Exception as e:
        print(f"An error occurred: {e}")

def Restore_file(Filename):
    try:
        shutil.move(os.path.join(BACKUP_DIR, Filename), '.')
        print(f"{Filename} restored successfully!")
    except FileNotFoundError:
        print(f"{Filename} not found in backup")
    except Exception as e:
        print(f"An error occurred: {e}")
def View_files_sorted(sort_by="name"):
    try:
        files = os.listdir()
        if not files:
            print("No files found")
            return

        file_stats = [(file, os.stat(file)) for file in files]

        if sort_by == "name":
            sorted_files = sorted(file_stats, key=lambda x: x[0].lower())
        elif sort_by == "size":
            sorted_files = sorted(file_stats, key=lambda x: x[1].st_size, reverse=True)
        elif sort_by == "modified":
            sorted_files = sorted(file_stats, key=lambda x: x[1].st_mtime, reverse=True)
        else:
            print("Invalid sort option. Sorting by name.")
            sorted_files = sorted(file_stats, key=lambda x: x[0].lower())

        print("Files in directory:")
        for file, stat in sorted_files:
            size = stat.st_size
            modified_time = time.ctime(stat.st_mtime)
            print(f"{file} - Size: {size} bytes, Last Modified: {modified_time}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    try:
        while True:
            print("FILE MANAGEMENT APP:")
            print("1: Create File")
            print("2: View Files")
            print("3: Delete File")
            print("4: Read File")
            print("5: Edit File")
            print("6: Search File")
            print("7: Rename File")
            print("8: Backup File")
            print("9: Restore File")
            print("10: View Files (Sorted)")
            print("11: Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                Filename = input("Enter the file name: ")
                Create_file(Filename)
            elif choice == 2:
                file_type = input("Enter file type to filter by (e.g., .txt, .csv) or press Enter to view all files: ")
                View_files(file_type if file_type else None)
            elif choice == 3:
                Filename = input("Enter the file you want to delete: ")
                Delete_file(Filename)
            elif choice == 4:
                Filename = input("Enter the file name you want to read: ")
                Read_file(Filename)
            elif choice == 5:
                Filename = input("Enter the file name you want to edit: ")
                Edit_file(Filename)
            elif choice == 6:
                keyword = input("Enter the keyword to search for: ")
                Search_file(keyword)
            elif choice == 7:
                old_name = input("Enter the current file name: ")
                new_name = input("Enter the new file name: ")
                Rename_file(old_name, new_name)
            elif choice == 8:
                Filename = input("Enter the file you want to backup: ")
                Backup_file(Filename)
            elif choice == 9:
                Filename = input("Enter the file you want to restore: ")
                Restore_file(Filename)
            elif choice == 10:
                sort_by = input("Sort by 'name', 'size', or 'modified': ").lower()
                View_files_sorted(sort_by)
            elif choice == 11:
                print("FILE MANAGER TURNING OFF...")
                break
            else:
                print("Please enter a number between 1 and 11.")
    except ValueError:
        print("Please enter a number to proceed.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

main()
