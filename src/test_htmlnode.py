import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode, markdown_to_html_node

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

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children_with_props(self):
        node = ParentNode("p", [
            LeafNode("a", "Go to Google", {"href": "https://www.google.com"}),
            LeafNode("p", "Bold Text", {"class": "bold-mode"}),
            LeafNode("span", "Relax", {"class": "span-mode"}),
            ],
        )
        self.assertEqual(
            node.to_html(),
            '<p><a href="https://www.google.com">Go to Google</a><p class="bold-mode">Bold Text</p><span class="span-mode">Relax</span></p>'
        )
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
        html,
        "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
    )

    def test_codeblock(self):
        md = """
    ```
    This is text that _should_ remain
    the **same** even with inline stuff
    ```
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )
