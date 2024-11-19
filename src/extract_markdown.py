import re
from blocks import markdown_to_blocks

def extract_markdown_images(text):
    images = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return images


def extract_markdown_links(text):
    links = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return links

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block[0] == "#":
            return block.lstrip("#").strip()
    raise Exception("Error: No Title Found")
