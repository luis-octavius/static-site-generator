import unittest
from textnode import TextNode, TextType 
from split_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link

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

