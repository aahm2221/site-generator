import os
import shutil

def copy_file(source, destination):
    if os.path.exists(destination):
        shutil.rmtree(destination)
    os.mkdir(destination)
    current_dir = os.listdir(source)
    for item in current_dir:
        if os.path.isfile(os.path.join(source, str(item))):
            shutil.copy(os.path.join(source, str(item)),os.path.join(destination, str(item)))
        else:
            copy_file(os.path.join(source, str(item)), os.path.join(destination, str(item)))