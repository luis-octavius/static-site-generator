import os 
import shutil
import sys
from textnode import TextNode
from generate_page import generate_pages_recursive

def copy_dir_contents(src_dir, dest_dir): # copy the contents of a folder to another recursively
    abs_src = os.path.abspath(src_dir) # constructs the abspath of source directory
    dest_src = os.path.abspath(dest_dir) # same as above with the destination path 
    list_dir = os.listdir(abs_src) 

    for file in list_dir:
        src_path = os.path.join(abs_src, file) # constructs the abspath of file 
        dest_path = os.path.join(dest_src, file) # constructs the abspath of file in destination 

        if os.path.isfile(src_path):
            os.makedirs(os.path.dirname(dest_path), exist_ok = True)
            shutil.copy(src_path, dest_path)
            print("Arquivo copiado para: ", dest_path)

        if os.path.isdir(src_path):
            os.makedirs(dest_path, exist_ok = True)
            copy_dir_contents(src_path, dest_path)

def check_public():
    public_path = os.path.abspath(os.path.join("./", "public")) 
    if os.path.exists(public_path):
        shutil.rmtree(public_path) 
        os.mkdir(public_path)

def main():
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    check_public()
    copy_dir_contents("static", "public")
    generate_pages_recursive("content", "template.html", "docs", basepath)

main()


