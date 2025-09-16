import os 
import shutil
from textnode import TextNode

def copy_dir_contents(src_dir, dst_dir):
    abs_src = os.path.abspath(src_dir) # 
    dst_src = os.path.abspath(dst_dir)
    list_dir = os.listdir(abs_src)
    print("list dir: ", list_dir)

    for file in list_dir:
        src_path = os.path.join(abs_src, file)
        print("Src path file: ", src_path)
        dst_path = os.path.join(dst_src, file) 
        print("Dst path file: ", dst_path)

        if os.path.isfile(src_path):
            os.makedirs(os.path.dirname(dst_path), exist_ok = True)
            shutil.copy(src_path, dst_path)
            print("Arquivo copiado para: ", dst_path)

        if os.path.isdir(src_path):
            os.makedirs(dst_path, exist_ok = True)
            copy_dir_contents(src_path, dst_path)

def check_public():
    public_path = os.path.abspath(os.path.join("./", "public")) 
    print("public path: ", public_path)
    if os.path.exists(public_path):
        print("EXISTS")
        shutil.rmtree(public_path)
        os.mkdir(public_path)
        


def main():
    check_public()
    copy_dir_contents("static", "public")


main()


