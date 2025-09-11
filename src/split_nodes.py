from textnode import TextNode, TextType 

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
            print("Splitted: ", splitted_text)
            new_list.append(TextNode(splitted_text[0], TextType.TEXT))
            new_list.append(TextNode(splitted_text[1], text_type))
            new_list.append(TextNode(splitted_text[2], TextType.TEXT))
    return new_list






