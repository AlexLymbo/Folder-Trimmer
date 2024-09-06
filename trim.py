import os
import sys
import shutil
import zipfile
import traceback
from tqdm import tqdm

#color code for coolness
COLOR_RESET = "\033[0m"
COLOR_GREEN_INTENSE = "\033[92m"
COLOR_RED_INTENSE = "\033[91m"
COLOR_WHITE_INTESE = "\033[97m"
COLOR_PURPLE_INTENSE = "\033[95m"
COLOR_YELLOW_INTENSE = "\033[93m"

#ASCII art for coolness(says folder trimmer)
ASCII_ART = r'''
 _____     _     _             _____     _                               
|  ___|__ | | __| | ___ _ __  |_   _| __(_)_ __ ___  _ __ ___   ___ _ __ 
| |_ / _ \| |/ _` |/ _ \ '__|   | || '__| | '_ ` _ \| '_ ` _ \ / _ \ '__|
|  _| (_) | | (_| |  __/ |      | || |  | | | | | | | | | | | |  __/ |   
|_|  \___/|_|\__,_|\___|_|      |_||_|  |_|_| |_| |_|_| |_| |_|\___|_|   

'''

#find the path of the script to use for relative paths
script_path = os.getcwd()

#important folders
target_folder = "target"
output_folder = "output"
zip_folder = "zip"

#update with patterns to trim
trim_patterns = [
    ".kicad_prl",
    "-backups",
    "-cache",
    "sym-lib-table",
    "fp-lib-table",
    "3dshapes",
    "3dshapes.pretty",
    ".gbr",
    ".drl",
    ".pos",
    ".rpt",
    ".rpt",
    ".ps",
    ".pdf",
    ".dxf",
    ".plt"   
]

def main():
    print(COLOR_PURPLE_INTENSE + ASCII_ART + COLOR_RESET)
    print(COLOR_WHITE_INTESE + "Trimming folders with patterns: " + str(trim_patterns) + COLOR_RESET)


#test this script
if __name__ == "__main__":
    main()





