import os
import shutil

path = 'C:/Users/user/Desktop/folder/'
files = os.listdir(path)

new_path = 'C:\attribute_3rd_dataset2\filter_39class\1_infant_man\filter\copy_img3'
if not os.path.exists(new_path):
    os.mkdir(new_path)

# move
for file in files:
    if 'jpg' in file:
        shutil.move(path + file, new_path + file)
        print('{} has been moved to new folder!'.format(file))

# copy
for file in files:
    if 'pdf' in file:
        shutil.copy(path + file, new_path + file)
        print('{} has been copied in new folder!'.format(file))