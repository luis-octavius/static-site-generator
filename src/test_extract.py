import unittest 
from extract import * 

class TextExtract(unittest.TestCase):
    def test_eq_image(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        self.assertEqual(
            extract_markdown_images(text), 
            [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        )

    def test_eq_link(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"

        self.assertEqual(
            extract_markdown_links(text),
            [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        )


    def test_extract_title(self):
        md = "# Hello moto"
        self.assertEqual(extract_title(md), "Hello moto")
        md = """
- Nothing 
## You know 

some shitty code
"""
        self.assertRaises(Exception, extract_title, md)
