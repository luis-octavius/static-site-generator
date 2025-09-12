import unittest
from textnode import TextNode, TextType 
from split_nodes import (
        split_nodes_delimiter, 
        split_nodes_image, 
        split_nodes_link, 
        text_to_text_nodes,
        markdown_to_blocks
)

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

   
    def test_italic(self):
        node = TextNode("This is a _italic_ text", TextType.TEXT)
        splitted_node = split_nodes_delimiter([node], "_", TextType.ITALIC)
        test = [
            TextNode("This is a ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.TEXT)
        ]

        self.assertEqual(splitted_node, test)

    def test_exception(self):
        node = TextNode("This is a failing test", TextType.TEXT)
        self.assertRaises(Exception, split_nodes_delimiter, node, "/", TextType.BOLD)

    def test_split_two_images(self):
        node = TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )

    def test_split_two_links(self):
        node = TextNode("This is a text with an [link](https://www.boot.dev) and another [second link](https://www.google.com)", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is a text with an ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second link", TextType.LINK, "https://www.google.com"), 
            ],
            new_nodes,
        )

    def test_split_one_image(self):
        node = TextNode("This is a text with an image ![image](https://i.imgur.com/3elNhQu.png)", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is a text with an image ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png")
            ],
            new_nodes,
        )

    def test_split_one_link(self):
        node = TextNode("This is a text with a link [link](https://www.boot.dev)", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is a text with a link ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://www.boot.dev")
            ],
            new_nodes,
        )

    def test_text_to_text_nodes_one(self):
        node = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        new_nodes = text_to_text_nodes(node)

        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            new_nodes
        )
    
    def test_text_to_text_nodes_two(self):
        node = "This is a text with an image ![image](https://www.imgur.com) and a link [google link](https://www.google.com) with a _italic_ shape and a `code block`, don't you dare to forget the **BOLD TEXT**"

        new_nodes = text_to_text_nodes(node)

        self.assertListEqual(
            [
                TextNode("This is a text with an image ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://www.imgur.com"),
                TextNode(" and a link ", TextType.TEXT),
                TextNode("google link", TextType.LINK, "https://www.google.com"),
                TextNode(" with a ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" shape and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(", don't you dare to forget the ", TextType.TEXT),
                TextNode("BOLD TEXT", TextType.BOLD)
            ],
            new_nodes
        )
    

    def test_markdown_to_blocks_one(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_two(self):
        md = """
# This is a heading

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

- This is the first list item in a list block
- This is a list item
- This is another list item
"""

        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "# This is a heading",
                "This is a paragraph of text. It has some **bold** and _italic_ words inside of it.",
                "- This is the first list item in a list block\n- This is a list item\n- This is another list item"
         ]
        )
