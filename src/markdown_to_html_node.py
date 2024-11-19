from blocks import markdown_to_blocks, block_to_block_type
from parentnode import ParentNode
from leafnode import LeafNode
from textnode import TextNode, TextType
from text_to_textnodes import text_to_textnodes
from text_to_html import text_node_to_html_node

def markdown_to_html_node(markdown):
    children = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        node = block_to_node(block, block_type)
        children.append(node)
    return ParentNode("div", children)
    


def block_to_node(block, block_type):
    match block_type:
        case "heading":
            return heading_to_node(block)
        case "code":
            return code_to_node(block)
        case "quote":
            return quote_to_node(block)
        case "unordered_list":
            return unordered_list_to_node(block)
        case "ordered_list":
            return ordered_list_to_node(block)
        case "paragraph":
            return paragraph_to_node(block)
        case _:
            raise Exception("Error: Invalid block type")

def heading_to_node(block):
    split_block = block.split(" ", 1)
    return ParentNode(f"h{len(split_block[0])}", text_to_children(split_block[1]))

def code_to_node(block):
    code = ParentNode("code", [text_node_to_html_node(TextNode(block.strip("```"), TextType.TEXT))])
    return ParentNode("pre", [code])

def quote_to_node(block):
    children = []
    split_block = block.split("\n")
    for quote in split_block:
        children.extend(text_to_children(quote.lstrip("> ")))
    return ParentNode("blockquote", children)


def unordered_list_to_node(block):
    children = []
    list_marker = block[0:2]
    split_block = block.split("\n")
    for item in split_block:
        if item:
            children.append(ParentNode("li", text_to_children(item.lstrip(list_marker))))
    return ParentNode("ul", children)

def ordered_list_to_node(block):
    children = []
    split_block = block.split("\n")
    for item in split_block:
        if item:
            children.append(ParentNode("li", text_to_children(item.split(". ", 1)[1])))
    return ParentNode("ol", children)

def paragraph_to_node(block):
    return ParentNode("p", text_to_children(block))

def text_to_children(text):
    children = []
    text_nodes = text_to_textnodes(text)
    for node in text_nodes:
        children.append(text_node_to_html_node(node))
    return children
