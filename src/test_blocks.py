from blocks import BlockType, block_to_block_type
import unittest

class TestBlock(unittest.TestCase):
    def test_blocktype_heading(self):
        text = "# Heading 1"
        self.assertEqual(
            block_to_block_type(text),
            BlockType.HEADING 
        )

    def test_blocktype_code(self): 
        text = """
```
let a = 10;
const b = 15;
let c = a + b;
```
        """
        self.assertEqual(
            block_to_block_type(text.strip()),
            BlockType.CODE
        )
    
    def test_blocktype_quote(self):
        text = """
> Nietzsche once said:
> God is dead!
        """
        self.assertEqual(
            block_to_block_type(text),
            BlockType.QUOTE
        )

    def test_blocktype_unordered_list(self):
        text = """
- One item
- Two item
- Three item
        """
        self.assertEqual(
            block_to_block_type(text),
            BlockType.UNORDERED_LIST
        )

    def test_blocktype_ordered_list(self):
        text = """
1. One
2. Two
3. Three
        """
        self.assertEqual(
            block_to_block_type(text),
            BlockType.ORDERED_LIST
        )

    def test_blocktype_paragraph(self):
        text = """
Just a simple text
without any of these fancy things
        """
        self.assertEqual(
            block_to_block_type(text),
            BlockType.PARAGRAPH
        )
