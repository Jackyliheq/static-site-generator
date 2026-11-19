import os
import shutil


def copy_files(source, destination):
    if not os.path.exists(destination):
        os.mkdir(destination)
        
    for filename in os.listdir(source):
        source_path = os.path.join(source, filename)
        dest_path = os.path.join(destination, filename)
        print(f" * {source_path} -> {dest_path}")
        if os.path.isfile(source_path):
            shutil.copy(source_path, dest_path)
        else:
            copy_files(source_path, dest_path)

def main():
    source_dir = "./static"
    destination_dir = "./public"
    
    print("Deleting public directory...")
    if os.path.exists(destination_dir):
        shutil.rmtree(destination_dir)
        
    print("Copying files...")
    
    copy_files(source_dir, destination_dir)
    
        
main()