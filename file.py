import os
import shutil

directory = input("Enter directory path: ")

for filename in os.listdir(directory):
    if os.path.isfile(os.path.join(directory, filename)):
        ext = filename.split('.')[-1].lower()
        folder = os.path.join(directory, ext)
        
        if not os.path.exists(folder):
            os.makedirs(folder)
        
        shutil.move(os.path.join(directory, filename), 
                   os.path.join(folder, filename))

print("Files organized!")