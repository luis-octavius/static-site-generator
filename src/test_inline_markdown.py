from inline_markdown import markdown_to_html_node
import unittest

class TestInlineMD(unittest.TestCase):
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

    def test_quote(self):
        md = """
> This is quote text 
> with a paragraph at the end

para para 

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is quote text with a paragraph at the end</blockquote><p>para para</p></div>"
        )


    def test_ordered_list(self):
        md = """
1. One item
2. Two item 
3. Three item
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
                "<div><ol><li>One item</li><li>Two item</li><li>Three item</li></ol></div>"
        )

    def test_unordered_list(self):
        md = """
- One item 
- Two item 
- Three item
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>One item</li><li>Two item</li><li>Three item</li></ul></div>"
        )


    def test_many_types(self):
        md = """
```
some code
more code
```

> a quote 

- A item in a list 
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        print("HTML: ", html)
        self.assertEqual(
            html,
            """<div><pre><code>some code
more code
</code></pre><blockquote>a quote</blockquote><ul><li>A item in a list</li></ul></div>"""
        )

    def test_many_many_types(self):
        md = """
para para 

> quote
> nietzsche's quote 

- Nietzsche list 
- Schopenhauer list 

1. Nietzsche 
2. Plato 
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>para para</p><blockquote>quote nietzsche's quote</blockquote><ul><li>Nietzsche list</li><li>Schopenhauer list</li></ul><ol><li>Nietzsche</li><li>Plato</li></ol></div>"
        )
