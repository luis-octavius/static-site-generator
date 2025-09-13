from enum import Enum 
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered"
    ORDERED_LIST = "ordered"

heading = r"(\#+)"
code = r"^(`{3}[\s\S]*?`{3})$"
quote = r"^\s*(>+)"
unordered_list = r"^\s*(\*|\-|\+)"
ordered_list = r"^\s*(\d+)\."


def block_to_block_type(markdown):
    if re.match(heading, markdown):
        return BlockType.HEADING
    if re.match(code, markdown, re.MULTILINE):
        return BlockType.CODE
    if re.match(quote, markdown):
        return BlockType.QUOTE
    if re.match(unordered_list, markdown):
        return BlockType.UNORDERED_LIST
    if re.match(ordered_list, markdown):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH
