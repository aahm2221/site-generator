import unittest

from src.blocks import markdown_to_blocks, block_to_block_type

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(blocks, ["# This is a heading", "This is a paragraph of text. It has some **bold** and *italic* words inside of it.", "* This is the first list item in a list block\n* This is a list item\n* This is another list item"])

    def test_markdown_to_blocks_strip(self):
        markdown = "   # This is a heading\n\n   This is a paragraph of text. It has some **bold** and *italic* words inside of it.    \n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(blocks, ["# This is a heading", "This is a paragraph of text. It has some **bold** and *italic* words inside of it.", "* This is the first list item in a list block\n* This is a list item\n* This is another list item"])

    def test_markdown_to_blocks_extra_lines(self):
        markdown = "# This is a heading\n\n\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(blocks, ["# This is a heading", "This is a paragraph of text. It has some **bold** and *italic* words inside of it.", "* This is the first list item in a list block\n* This is a list item\n* This is another list item"])

    def test_block_to_block_type_heading1(self):
        block = "# This is a heading"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, "heading")

    def test_block_to_block_type_heading2(self):
        block = "## This is a heading"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, "heading")

    def test_block_to_block_type_heading3(self):
        block = "### This is a heading"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, "heading")

    def test_block_to_block_type_heading_paragraph(self):
        block = "#This is a paragraph"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, "paragraph")

    def test_block_to_block_type_code(self):
        block = "```This is a code block```"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, "code")

    def test_block_to_block_type_quote(self):
        block = ">This is a quote block\n>quote2"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, "quote")

    def test_block_to_block_type_not_quote(self):
        block = ">This is a quote block\nquote2"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, "paragraph")
    
    def test_block_to_block_type_unordered_list(self):
        block = "* This is a list\n* item 2\n* item 3"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, "unordered_list")

    def test_block_to_block_type_unordered_list_dashes(self):
        block = "- This is a list\n- item 2\n- item 3"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, "unordered_list")

    def test_block_to_block_type_not_unordered_list(self):
        block = "*This is a list\n* item 2\n* item 3"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, "paragraph")

    def test_block_to_block_type_ordered_list(self):
        block = "1. This is a list\n2. next item\n3. next"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, "ordered_list")

    def test_block_to_block_type_not_ordered_list(self):
        block = "1.This is a list\n2. next item\n3. next"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, "paragraph")

    def test_block_to_block_type_unordered_ordered_list(self):
        block = "1. This is a list\n3. next item\n3. next"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, "paragraph")

if __name__ == "__main__":
    unittest.main()
