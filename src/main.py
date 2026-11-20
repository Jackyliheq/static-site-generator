import os
import shutil
from textnode import generate_page
from pathlib import Path

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
            
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path)
        else:
            generate_pages_recursive(from_path, template_path, dest_path)

def main():
    source_dir = "./static"
    destination_dir = "./public"
    
    print("Deleting public directory...")
    if os.path.exists(destination_dir):
        shutil.rmtree(destination_dir)
        
    print("Copying files...")
    
    copy_files(source_dir, destination_dir)
    
    print("Generating content...")
    generate_pages_recursive("content", "template.html", "public")
    
main()