import unittest

from htmlnode import HTMLNode, LeafNode 

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("br")
        node2 = HTMLNode("br")
        self.assertEqual(node, node2)

    def test_props_to_html(self):
        dict_props = {
            "href": "https://www.boot.dev",
            "target": "_blank",
        }
        node = HTMLNode("a", props=dict_props)
        str_props = node.props_to_html()
        print("Str props: ", str_props)
        str_output_test = ' href="https://www.boot.dev" target="_blank"'
        self.assertEqual(str_props, str_output_test)

    def test_props_to_html2(self):
        dict_props = {
            "href": "https://www.google.com",
            "target": "_blank",
            "download": "file",
        }
        node = HTMLNode("a", props=dict_props)
        str_props = node.props_to_html()
        str_output_test = ' href="https://www.boot.dev target="_blank download="file"'
        self.assertNotEqual(str_props, str_output_test)

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        print("Node: ", node)
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click here!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click here!</a>')

    def test_leaf_to_html_h1(self):
        node = LeafNode("h1", "Hey Jude")
        self.assertEqual(node.to_html(), '<h1>Hey Jude</h1>')
