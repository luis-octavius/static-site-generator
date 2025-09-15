from blocks import *
from htmlnode import *
from textnode import *
import re 
from split_nodes import markdown_to_blocks, text_to_text_nodes

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)

    format_blocks = []
    for block in blocks:
        block_type = block_to_block_type(block) # define o tipo do bloco

        if block_type == BlockType.ORDERED_LIST:
            format_blocks.append(clean_ordered(block))
            continue 
        if block_type == BlockType.UNORDERED_LIST:
            format_blocks.append(clean_unordered(block))
            continue 
        if block_type == BlockType.CODE:
            format_blocks.append(ParentNode("pre", [LeafNode("code", clean_code(block))]))
            continue
        if block_type == BlockType.HEADING:
            content, hashes = clean_heading(block)
            children = text_to_children(clean)
            format_blocks.append(ParentNode(f"h{hashes}", content))
            continue
        if block_type == BlockType.QUOTE:
            clean = clean_quote(block)
            children = text_to_children(clean)
            format_blocks.append(ParentNode("blockquote", children))
            continue
        if block_type == BlockType.PARAGRAPH:
            clean = clean_paragraph(block)
            children = text_to_children(clean)
            format_blocks.append(ParentNode("p", children))
            continue
    return ParentNode("div", format_blocks)

def text_to_children(str):
    text_nodes = text_to_text_nodes(str)

    children = []

    for tn in text_nodes:
        child = text_node_to_html_node(tn)
        children.append(child)
    return children

# def remove_block_markers(text, block_type):
#     if block_type == BlockType.HEADING:
#         return clean_heading(text)
#     if block_type == BlockType.QUOTE:
#         return clean_quote(text)
#     if block_type == BlockType.ORDERED_LIST:
#         return clean_ordered(text)
#     if block_type == BlockType.UNORDERED_LIST:
#         return clean_unordered(text)
#     if block_type == BlockType.CODE:
#         return clean_code(text)

def clean_heading(text):
    first = text.lstrip().splitlines()[0]
    hashes = len(first) - len(first.lstrip('#'))
    lines = text.splitlines()
    if lines:
        lines[0] = re.sub(rf'^\s*#{{{hashes}}}\s+', '', lines[0])
    content = " ".join(line.strip() for line in lines if line.strip != "")
    return content, hashes 

def clean_paragraph(text):
    return " ".join(line.strip() for line in text.splitlines() if line.strip != "")

def clean_quote(text):
    lines = []
    for line in text.splitlines():
        line = re.sub(r'^\s*>\s?', '', line).strip()
        if line:
            lines.append(line)
    return " ".join(lines)

def clean_unordered(text):
    li_nodes = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue 
        line = re.sub(r'^\s*([-*])\s+', '', line)
        li_nodes.append(ParentNode("li", text_to_children(str)))
    return ParentNode("ul", li_nodes)

def clean_ordered(text):
    li_nodes = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        line = re.sub(r'^\s*\d+\.\s+', '', line)
        li_nodes.append(ParentNode("li", text_to_children(str)))
    return ParentNode("ol", li_nodes)

def clean_code(text):
    lines = text.splitlines(True) # mantém \n 
    if lines and lines[0].strip() == "```":
        lines = lines[1:]
    if lines and lines[-1].strip() == "```":
        lines = lines[:-1]
    return "".join(lines)

