from textnode import TextNode, TextType 
from extract import extract_markdown_images, extract_markdown_links


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_list = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_list.append(old_node)
            continue 
        split_nodes = []
        splitted = old_node.text.split(delimiter)
        if len(splitted) % 2 == 0:
            raise ValueError("invalid markdown")
        for i in range(len(splitted)):
            if splitted[i] == "":
                continue 
            if i % 2 == 0:
                split_nodes.append(TextNode(splitted[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(splitted[i], text_type))
        new_list.extend(split_nodes)
    return new_list


def split_nodes_image(old_nodes):
    new_list = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_list.append(old_node)
            continue 
        images = extract_markdown_images(old_node.text)
        original_text = old_node.text 
        if len(images) == 0:
            new_list.append(old_node)
            continue 
        for image in images: 
            splitted = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(splitted) != 2:
                raise ValueError("invalid markdown")
            if splitted[0] != "":
                new_list.append(TextNode(splitted[0], TextType.TEXT))
            new_list.append(TextNode(image[0], TextType.IMAGE, image[1]))
            original_text = splitted[1]
        if original_text != "":
            new_list.append(TextNode(original_text, TextType.TEXT))
    return new_list
        

def split_nodes_link(old_nodes):
    new_list = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_list.append(old_node)
            continue 
        links = extract_markdown_links(old_node.text)
        if len(links) == 0:
            new_list.append(old_node)
            continue 
        original_text = old_node.text
        for link in links:
            splitted = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(splitted) != 2:
                raise ValueError("invalid markdown")
            if splitted[0] != "":
                new_list.append(TextNode(splitted[0], TextType.TEXT))
            new_list.append(TextNode(link[0], TextType.LINK, link[1]))
            original_text = splitted[1]
        if original_text != "":
            new_list.append(TextNode(original_text, TextType.TEXT))
    return new_list 

def text_to_text_nodes(text):
    new_list = []
    
    node = TextNode(text, TextType.TEXT)
    
    image_split = split_nodes_image([node])
    link_split = split_nodes_link(image_split)
    split_delimiters_bold = split_nodes_delimiter(link_split, "**", TextType.BOLD)
    split_delimiters_italic = split_nodes_delimiter(split_delimiters_bold, "_", TextType.ITALIC)
    split_delimiters_code = split_nodes_delimiter(split_delimiters_italic, "`", TextType.CODE)
    
    print("Split after: ", split_delimiters_code)

    return split_delimiters_code


