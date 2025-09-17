from inline_markdown import markdown_to_html_node 
from extract import extract_title
import os
from pathlib import Path

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    from_contents = None 
    with open(from_path, 'r') as data:
        from_contents = data.read()

    # print("From content: ", from_contents)
    template_contents = None 
    with open(template_path, 'r') as data:
        template_contents = data.read()

    html_node = markdown_to_html_node(from_contents)

    html = html_node.to_html()

    title = extract_title(from_contents)

    page = template_contents.replace("{{ Title }}", title)
    page = page.replace("{{ Content }}", html)

    dest_path = Path(dest_path)
    dest_path = dest_path.with_suffix(".html") # change extension of md file to html

    if os.path.isdir(dest_path):
        os.makedirs(os.path.dirname(dest_path), exist_ok = True)
    with open(dest_path, "w") as data:
        data.write(page)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    abs_src = os.path.abspath(dir_path_content)
    dest_src = os.path.abspath(dest_dir_path)

    list_content = os.listdir(dir_path_content)

    print("list content: ", list_content)

    for file in list_content:
        src_path = os.path.join(abs_src, file)
        dest_path = os.path.join(dest_src, file)

        if os.path.isfile(src_path) and file.endswith(".md"):
            os.makedirs(os.path.dirname(dest_path), exist_ok = True)
            generate_page(src_path, template_path, dest_path)
        else:
            os.makedirs(os.path.dirname(dest_path), exist_ok = True)
            generate_pages_recursive(src_path, template_path, dest_path)

