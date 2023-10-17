import shutil
import os
desktop_dir = '/Users/raphaelco/Desktop/'
files_on_desktop = os.listdir('/Users/raphaelco/Desktop')
for file in files_on_desktop:
    if file.endswith(".png") or file.endswith(".jpg"):
        file_dir = desktop_dir + '/' + file
        shutil.move(file_dir, '/Users/raphaelco/Desktop/balls')
        print(f"Moved {file} into balls")
print("Moving files completed")
/Users/raphaelco/PycharmProjects/cleanDesktop