import unittest

from src.parentnode import ParentNode
from src.leafnode import LeafNode
from src.markdown_to_html_node import markdown_to_html_node


class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_ordered_list(self):
        # Test case 1: Simple ordered list
        markdown = "1. First item\n2. Second item\n3. Third item"
        html_node = markdown_to_html_node(markdown)
        
        # Check if the root node is a div
        assert html_node.tag == "div"
        
        # Check if it has one child (the ol)
        assert len(html_node.children) == 1
        assert html_node.children[0].tag == "ol"
        
        # Check if ol has three li children
        ol_node = html_node.children[0]
        assert len(ol_node.children) == 3
        assert ol_node.children[0].tag == "li"
        assert ol_node.children[1].tag == "li"
        assert ol_node.children[2].tag == "li"
        assert ol_node.children[0].children[0].value == "First item"
        assert ol_node.children[1].children[0].value == "Second item"
        assert ol_node.children[2].children[0].value == "Third item"

    def test_heading1(self):
        markdown = "# heading 1"
        html_node = markdown_to_html_node(markdown)
        
        assert html_node.children[0].tag == "h1"
        
        # Check if ol has three li children
        assert html_node.children[0].children[0].value == "heading 1"

    def test_heading2(self):
        markdown = "## heading"
        html_node = markdown_to_html_node(markdown)
        
        assert html_node.children[0].tag == "h2"
        
    def test_heading3(self):
        markdown = "### heading"
        html_node = markdown_to_html_node(markdown)
        
        assert html_node.children[0].tag == "h3"
        
    def test_heading4(self):
        markdown = "#### heading"
        html_node = markdown_to_html_node(markdown)
        
        assert html_node.children[0].tag == "h4"
        
    def test_heading5(self):
        markdown = "##### heading"
        html_node = markdown_to_html_node(markdown)
        
        assert html_node.children[0].tag == "h5"
        
    def test_heading6(self):
        markdown = "###### heading"
        html_node = markdown_to_html_node(markdown)
        
        assert html_node.children[0].tag == "h6"

    def test_code(self):
        markdown = "```this is a code block```"
        html_node = markdown_to_html_node(markdown)
        
        assert html_node.children[0].tag == "pre"
        pre_node = html_node.children[0]
        assert pre_node.children[0].tag == "code"
        assert pre_node.children[0].children[0].value == "this is a code block"

    def test_quote(self):
        markdown = ">line*something*1\n>line2"
        html_node = markdown_to_html_node(markdown)
        
        assert html_node.children[0].tag == "blockquote"
        quote_node = html_node.children[0]
        assert quote_node.children[0].tag == "p"
        assert quote_node.children[0].children[0].value == "line"
        assert quote_node.children[0].children[1].tag == "i"
        assert quote_node.children[0].children[1].value == "something"

    def test_unordered_list(self):
        markdown = "* item 1\n* item2"
        html_node = markdown_to_html_node(markdown)
        
        assert html_node.children[0].tag == "ul"
        list_node = html_node.children[0]
        assert list_node.children[0].tag == "li"
        assert list_node.children[0].children[0].value == "item 1"

    def test_ordered_list(self):
        markdown = "1. item 1\n2. item2"
        html_node = markdown_to_html_node(markdown)
        
        assert html_node.children[0].tag == "ol"
        list_node = html_node.children[0]
        assert list_node.children[0].tag == "li"
        assert list_node.children[0].children[0].value == "item 1"

    def test_paragraph(self):
        markdown = "This is a paragraph"
        html_node = markdown_to_html_node(markdown)
        
        assert html_node.children[0].tag == "p"
        assert html_node.children[0].children[0].value == "This is a paragraph"

if __name__ == "__main__":
    unittest.main()