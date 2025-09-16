from blocks import * 
import unittest

class TestBlock(unittest.TestCase):
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
    def test_block_to_blocktype(self): 
        block = "# Title"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

        block = "> quote \n> more quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

        block = "- list\n- items"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

        block = "some text"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
