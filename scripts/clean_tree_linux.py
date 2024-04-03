import re
import os

# FOR LINUX
# 1. tree -a > tree.txt
# obtains the directory structure from current folder

# 2. python clean_tree_linux.py
# runs clean_tree.py and cleans the directory structure from tree /f /a > tree.t. Inside file i can specific exclusions

"""
A script to clean the directory structure tree.txt file created by the linux tree command.

How to use:
1. In your root directory of your project run command "tree -a > tree.txt"
This will create a tree directory structure in your root project folder. 

2. Then run the terminal command "python clean_tree_linux.py".
This will create a processed_tree.txt file in your root project folder. 

"""

def process_tree_file(input_filename: str, output_filename: str, words_to_match: list):
    """Process the tree file and remove any files or directories that match the words_to_match list.

    Args:
        input_filename (str): The input filename with tree to process
        output_filename (str): The output file name for processed tree
        words_to_match (list): A list of words to match in the file or directory name
    """
    with open(input_filename, 'r') as f, open(output_filename, 'w') as out:
        ignore = False
        ignore_level = 0
        for line in f:
            
            
            
            
            ignore_this_line = False

            # Determine if it is a directory or a file
            is_folder = True if "." not in line else False
            
            
            # Determine level
            level_symbol_match = re.search(r'[├└]──', line)
            
            if level_symbol_match is not None:
                level_symbol_position = level_symbol_match.start()
                
                level = level_symbol_position // 4
                
            else:
                ignore_this_line = True
                

            # Check if we are still ignoring lines
            
            if ignore and level > ignore_level:
                
                ignore_this_line = True
                
            elif ignore:
                ignore = False
                


            # Get file or directory name
            name = line.strip().split(' ')[-1]
            

            # Check if name matches or contains any word in the list
            if not ignore_this_line:
                if any(word == name for word in words_to_match):
                    ignore = True
                    ignore_level = level
                    
                    ignore_this_line = True
                
            if not ignore_this_line:
                if any(word in name for word in contains_words):
                    ignore = True
                    ignore_level = level
                    ignore_this_line = True
                    
                    
            if not ignore_this_line:
                if any(word == name for word in leave_this_but_ignore_children):
                    ignore = True
                    ignore_level = level
                    ignore_this_line = False
                    
                    

            if not ignore_this_line:
                
                out.write(line)
            else:
                
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
    "htmlcov",
    ".next"
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
