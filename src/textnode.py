from htmlnode import LeafNode
from enum import Enum 

class TextType(Enum): 
    PLAIN = "text" 
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode():
    def __init__(self, text, text_type, url = None, alt = None):
        self.text = text 
        self.text_type = text_type
        self.url = url 
        self.alt = alt 

    def __eq__(self, other):
        if isinstance(other, TextNode):
            return self.text_type == other.text_type and self.url == other.url and self.text == other.text 

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.PLAIN:
            return LeafNode(None, text_node.text) 
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.alt})
        case _:
            raise Exception("Invalid Text Type")

