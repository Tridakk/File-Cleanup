import os
import re

os.chdir('/Users/drake/OneDrive/Desktop/Music')

for file in os.listdir():
    # Separate the file name and extension
    name, ext = os.path.splitext(file)

    # Remove numbers, replace underscores with spaces, and capitalize first letter of each word
    new_name = re.sub(r'\d+', '', name).replace('_', ' ').strip().title() + ext

    # Rename the file
    os.rename(file, new_name)
    print(f"Renamed '{file}' to '{new_name}'")
