import os
import shutil
import traceback
from tqdm import tqdm

# color code for coolness
COLOR_RESET = "\033[0m"
COLOR_GREEN_INTENSE = "\033[92m"
COLOR_RED_INTENSE = "\033[91m"
COLOR_WHITE_INTESE = "\033[97m"
COLOR_PURPLE_INTENSE = "\033[95m"
COLOR_YELLOW_INTENSE = "\033[93m"

# ASCII art for coolness
ASCII_ART = r'''
 _____     _     _             _____     _                               
|  ___|__ | | __| | ___ _ __  |_   _| __(_)_ __ ___  _ __ ___   ___ _ __ 
| |_ / _ \| |/ _` |/ _ \ '__|   | || '__| | '_ ` _ \| '_ ` _ \ / _ \ '__|
|  _| (_) | | (_| |  __/ |      | || |  | | | | | | | | | | | |  __/ |   
|_|  \___/|_|\__,_|\___|_|      |_||_|  |_|_| |_| |_|_| |_| |_|\___|_|   

'''

# Find the path of the script to use for relative paths
script_path = os.getcwd()

# Update with patterns to trim
trim_patterns = [
    ".kicad_prl", "-backups", "-cache", "sym-lib-table", "fp-lib-table", 
    "3dshapes", "3dshapes.pretty", ".gbr", ".drl", ".pos", ".rpt", 
    ".ps", ".pdf", ".dxf", ".plt" ,"auto-save", ".bak", ".bck", ".swp",
]

def calculate_folder_size(folder_path):
    total_size = 0
    for dirpath, _, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            total_size += os.path.getsize(file_path)
    return total_size    

def main():
    print(COLOR_PURPLE_INTENSE + ASCII_ART + COLOR_RESET)
    print(COLOR_YELLOW_INTENSE + "Trimming folders with patterns: " + COLOR_RESET + COLOR_RED_INTENSE + str(trim_patterns) + COLOR_RESET)

    # User input for the target folder
    target_folder_path = input(COLOR_WHITE_INTESE + "\nEnter the target folder path: \n" + COLOR_RESET)
    target_folder_path = os.path.join(script_path, target_folder_path)

    # Path for the output "trim" folder
    trim_folder_path = os.path.join(script_path, "trim")

    # Ensure the trim folder exists
    if not os.path.exists(trim_folder_path):
        os.makedirs(trim_folder_path)

    # Copy the contents of the target folder to the "trim" folder
    print(COLOR_YELLOW_INTENSE + "\nCopying target folder contents to the 'trim' folder..." + COLOR_RESET)
    try:
        for item in tqdm(os.listdir(target_folder_path), desc="Copying", unit="file", colour="cyan"):
            source = os.path.join(target_folder_path, item)
            destination = os.path.join(trim_folder_path, item)

            if any(pattern in item for pattern in trim_patterns):
                continue
            
            if os.path.isdir(source):
                shutil.copytree(source, destination, dirs_exist_ok=True)
            else:
                shutil.copy2(source, destination)
    except Exception as e:
        print(COLOR_RED_INTENSE + "Error copying target folder contents to the 'trim' folder: " + str(e) + COLOR_RESET)
        traceback.print_exc()
        return            

    #add line to separate the output
    print(COLOR_PURPLE_INTENSE + "--------------------------------" + COLOR_RESET)  

    # Calculate saved size
    target_folder_size = calculate_folder_size(target_folder_path)
    trimmed_folder_size = calculate_folder_size(trim_folder_path)
    space_saved = target_folder_size - trimmed_folder_size
    print(COLOR_GREEN_INTENSE + "Space saved: " + str(space_saved) + " bytes" + COLOR_RESET)

    print(COLOR_GREEN_INTENSE + "Done!" + COLOR_RESET)

# Run the script
if __name__ == "__main__":
    main()
