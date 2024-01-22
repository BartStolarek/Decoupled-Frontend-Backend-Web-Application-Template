import re
import os

# FOR LINUX
# 1. tree -a > tree.txt
# obtains the directory structure from current folder

# 2. python clean_tree_linux.py
# runs clean_tree.py and cleans the directory structure from tree /f /a > tree.t. Inside file i can specific exclusions

def process_tree_file(input_filename, output_filename, words_to_match):
    with open(input_filename, 'r') as f, open(output_filename, 'w') as out:
        ignore = False
        ignore_level = 0
        for line in f:
            
            #print(f"#####################################################################")
            #print(f"Handling line: {line}")
            
            ignore_this_line = False

            # Determine if it is a directory or a file
            is_folder = True if "." not in line else False
            #print(f"is_folder: {is_folder}")
            
            # Determine level
            level_symbol_match = re.search(r'[├└]──', line)
            #print(f"level_symbol_match: {level_symbol_match}")
            if level_symbol_match is not None:
                level_symbol_position = level_symbol_match.start()
                #print(f"level_symbol_position: {level_symbol_position}")
                level = level_symbol_position // 4
                #print(f"level: {level}")
            else:
                ignore_this_line = True
                #print(f"ignore_this_line: {ignore_this_line}")

            # Check if we are still ignoring lines
            #print(f"checking if we are still ignoring lines")
            if ignore and level > ignore_level:
                #print(f"ignore: {ignore} and level: {level} > ignore_level: {ignore_level}")
                ignore_this_line = True
                #print(f"ignore_this_line: {ignore_this_line}")
            elif ignore:
                ignore = False
                #print(f"same or higher level so resetting ignore: {ignore}")


            # Get file or directory name
            name = line.strip().split(' ')[-1]
            #print(f"file/directory name: {name}")

            # Check if name matches or contains any word in the list
            if not ignore_this_line:
                if any(word == name for word in words_to_match):
                    ignore = True
                    ignore_level = level
                    #print(f"Word matched in ignore list so ignore is set to True and ignore_level is set to {ignore_level}")
                    ignore_this_line = True
                
            if not ignore_this_line:
                if any(word in name for word in contains_words):
                    ignore = True
                    ignore_level = level
                    ignore_this_line = True
                    #print(f"Word contained in ignore list so ignore is set to True and ignore_level is set to {ignore_level}")
                    
            if not ignore_this_line:
                if any(word == name for word in leave_this_but_ignore_children):
                    ignore = True
                    ignore_level = level
                    ignore_this_line = False
                    #print(f"Word matched in leave_this_but_ignore_children list so ignore is set to True and ignore_level is set to {ignore_level}")
                    

            if not ignore_this_line:
                #print(f"Writing line: {line}")
                out.write(line)
            else:
                #print(f"Ignoring line: {line}")
                pass


# File and directory names to match and exclude
words_to_match = [
    "cache",
    ".vscode",
    "last_run",
    "venv",
    ".flake8",
    ".git",
    "__pycache__",
    "ckeditor",
    "readme_media",
    
]

contains_words = [
    "cache",
    "tree",
    "last_run"
]

leave_this_but_ignore_children = [
    "ckeditor",
    "fonts",
    "images",
    "styles",
    "webassets-external",
    "node_modules",
    "htmlcov"  
]



# Get the current script's directory
current_script_directory = os.path.dirname(os.path.abspath(__file__))


# Get the projects root folder path
while not os.path.exists(os.path.join(current_script_directory, '.gitignore')):
    current_script_directory = os.path.dirname(current_script_directory)
project_root = current_script_directory

tree_path = os.path.join(project_root, 'tree.txt')
processed_tree_path = os.path.join(project_root, 'processed_tree.txt')

# Process tree file
process_tree_file(tree_path, processed_tree_path, words_to_match)
