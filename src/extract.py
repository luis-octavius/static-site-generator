import re 

pattern = r"\[(.*?)\]\((.*?)\)"

def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches


def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

def extract_title(markdown):
    for line in markdown.splitlines():
        stripped = line.strip()
        if re.match(r'^#\s+', stripped):
            title = re.sub('^#\s*', '', stripped)
            return title 
    raise Exception("No H1 header found in Markdown")
