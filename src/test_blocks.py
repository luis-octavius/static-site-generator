from blocks import BlockType, block_to_block_type
import unittest

class TestBlock(unittest.TestCase):
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
