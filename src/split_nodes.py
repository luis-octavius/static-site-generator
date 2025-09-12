from textnode import TextNode, TextType 
from extract import extract_markdown_images, extract_markdown_links

delimiters = ["**", "_", "`"]

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    if delimiter not in delimiters:
        raise Exception("Invalid markdown syntax")

    new_list = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_list.append(old_node)
        else:
            splitted_text = old_node.text.split(delimiter)
            new_list.append(TextNode(splitted_text[0], TextType.TEXT))
            new_list.append(TextNode(splitted_text[1], text_type))
            new_list.append(TextNode(splitted_text[2], TextType.TEXT))
    return new_list


def split_nodes_image(old_nodes):
    new_list = []

    for old_node in old_nodes:
        images = extract_markdown_images(old_node.text)
        if len(images) == 0:
            return [old_nodes]

        original_text = old_node.text 
        for image in images: 
            splitted = original_text.split(f"![{image[0]}]({image[1]})", 1)
            original_text = splitted[1]
            new_list.append(TextNode(splitted[0], TextType.TEXT))
            new_list.append(TextNode(image[0], TextType.IMAGE, image[1]))
            print("Splinter: ", splitted)
        print("New list: ", new_list)
    return new_list
        

def split_nodes_link(old_nodes):
    new_list = []

    for old_node in old_nodes:
        links = extract_markdown_links(old_node.text)
        if len(links) == 0:
            return [old_nodes]

        original_text = old_node.text 
        for link in links:
            splitted = original_text.split(f"[{link[0]}]({link[1]})", 1)
            print("Splitted link: ", splitted)
            print("Original: ", original_text)
            original_text = splitted[1]
            new_list.append(TextNode(splitted[0], TextType.TEXT))
            new_list.append(TextNode(link[0], TextType.LINK, link[1]))


    return new_list 



