# Folder Trimmer 📁✂️
## Description 📝
Folder Trimmer is a tool designed to help you clean up unnecessary files from folders, specifically targeting KiCad files for now. 

## Current Functionality ⚙️
Trimming KiCad Files: The script removes specific unwanted files from a KiCad project folder based on predefined patterns.
Copying Files: It copies files from the target folder to a new folder called "trim," excluding files that match the trim patterns.

## Usage 🚀
1. Clone the Repository
```
git clone https://github.com/yourusername/folder-trimmer.git
cd folder-trimmer
```
2. Run the Script
```
python folder_trimmer.py
```
You will be prompted to enter the path to the target folder. The script will then process this folder, copying files to a "trim" folder and removing any files that match the trim patterns.

## Future Plans 🔮
- GUI Development: Adding a graphical user interface to make the tool more user-friendly.
- Support for Other Formats: Extending functionality to handle different types of files and formats, such as Matlab/Simulink and Altium.
