from inline_markdown import markdown_to_html_node 
from extract import extract_title
import os
import re

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    from_contents = None 
    with open(from_path, 'r') as data:
        from_contents = data.read()

    # print("From content: ", from_contents)
    template_contents = None 
    with open(template_path, 'r') as data:
        template_contents = data.read()

    # print("Template: ", template_contents)
    html_node = markdown_to_html_node(from_contents)
    # print("Type: ", type(html_node))
    # print("Node html: ", html_node)


    html = html_node.to_html()

    # print("HTML: ", html)
    title = extract_title(from_contents)

    # re.sub("{{\s+Title\s+}}", title, template_contents)
    # re.sub("{{\s+Content\s+}}", html, template_contents)
    page = template_contents.replace("{{ Title }}", title)
    page = page.replace("{{ Content }}", html)

    print("Template: ", template_contents)
    
    if os.path.isdir(dest_path):
        os.makedirs(os.path.dirname(dest_path), exist_ok = True)
    with open(dest_path, "w") as data:
        data.write(page)

