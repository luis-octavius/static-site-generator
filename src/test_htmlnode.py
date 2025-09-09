import unittest

from htmlnode import HTMLNode 

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
