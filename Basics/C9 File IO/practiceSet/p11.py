# Write a python program to rename a file to “renamed_by_ python.txt.

import os

old_name = "old_file_name.txt"   # replace with your current file name
new_name = "renamed_by_python.txt"

os.rename("Chapter9/practiceSet/p11old.txt", "Chapter9/practiceSet/renamed_by_python.txt")


print("File renamed successfully!")
