import os



# 1. Get the current working directory
print(os.getcwd())

print(os.__file__)

# 2. List all files and directories in the current directory
print("Directory Contents:", os.listdir())



# 3. Create a new directory
new_dir = "test_directory"
os.makedirs(new_dir, exist_ok=True)
print(f"Directory '{new_dir}' created!")

# 4. Remove a directory
os.rmdir(new_dir)
print(f"Directory '{new_dir}' removed!")



# 5. Get the size of a file
file_path = os.path.basename(__file__)  # The name of the current script file
if os.path.exists(file_path):
    print(f"Size of '{file_path}': {os.path.getsize(file_path)} bytes")



# 6. Check if a path is a file or directory
# The path = "."  is a shorthand way to refer to the current working directory. 
# path = ".."  # Refers to the parent directory
path = "."
print(f"Is '{path}' a directory? {os.path.isdir(path)}")
print(f"Is '{path}' a file? {os.path.isfile(path)}")



# 7. Get absolute path of a file or directory
print("Absolute Path of Current Directory:", os.path.abspath("."))



# 8. Check if a file or directory exists
print(f"Does '{new_dir}' exist? {os.path.exists(new_dir)}")




# 9. Rename a file or directory
temp_file = "temp_file.txt"

with open(temp_file, "w") as f:
    f.write("Temporary file for demonstration.")  # Create a temp file

new_name = "renamed_file.txt"

os.rename(temp_file, new_name)
print(f"Renamed '{temp_file}' to '{new_name}'")