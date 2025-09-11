import re 

pattern = r"\[(.*?)\]\((.*?)\)"

def extract_markdown_images(text):
    matches = re.findall(pattern, text)
    return matches 

def extract_markdown_links(text):
    matches = re.findall(pattern, text)
    return matches 

