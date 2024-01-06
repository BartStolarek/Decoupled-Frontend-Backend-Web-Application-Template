import re


def process_tree_file(input_filename, output_filename, words_to_match):
    with open(input_filename, 'r', encoding='cp1252') as f, open(output_filename, 'w') as out:
        ignore = False
        ignore_level = 0
        for line in f:
            ignore_this_line = False
            line = line.replace('\0', '')

            # Determine if it is a directory or a file
            is_folder = '---' in line

            # If it's not a file or a directory, continue to the next line
            if not is_folder and '|' not in line:
                ignore_this_line = True

            if not ignore_this_line:
                # Determine level
                
                first_alnum_punct_match = re.search('\w|[\.\-_]', line)
                if first_alnum_punct_match is not None:
                    first_alnum_punct = first_alnum_punct_match.start()
                    level = first_alnum_punct // 4
                else:
                    ignore_this_line = True
                
            
            if not ignore_this_line:
                # Check if we are still ignoring lines
                if ignore and level > ignore_level:
                    ignore_this_line = True
                else:
                    ignore = False

            if not ignore_this_line:
                # Get file or directory name
                name = line.split()[-1]

            if not ignore_this_line:
                # Check if name matches or contains any word in the list
                if any(word in name for word in words_to_match):
                    if is_folder:
                        ignore = True
                        ignore_level = level
                    ignore_this_line = True

            if not ignore_this_line:
                out.write(line)
            else:
                pass
        out.write("+---venv")
# File and directory names to match and exclude
words_to_match = [
    "cache", 
    "chrome_user_data",
    "tree",
    ".vscode",
    "last_run",
    "venv"
    ]



# Process tree file
process_tree_file('tree.txt', 'processed_tree.txt', words_to_match)
