import unittest
from textnode import TextNode, TextType 
from split_nodes import split_nodes_delimiter

class TestSplitNodes(unittest.TestCase):
    def test_code(self):
        node = TextNode("This is a text with a `code block` word", TextType.TEXT)
        splitted_node = split_nodes_delimiter([node], "`", TextType.CODE)

        test = [
            TextNode("This is a text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(splitted_node, test)

    def test_bold(self):
        node = TextNode("This is a **bold** text", TextType.TEXT)
        splitted_node = split_nodes_delimiter([node], "**", TextType.BOLD)
        test = [
            TextNode("This is a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT)
        ]

        self.assertEqual(splitted_node, test)

    # def test_exception(self):
    #     node = TextNode("This is a **bold** text", TextType.TEXT)
    #     splitted_node = split_nodes_delimiter([node], "/", TextType.BOLD)

