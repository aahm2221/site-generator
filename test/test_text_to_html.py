import unittest

from src.leafnode import LeafNode
from src.textnode import TextNode, TextType
from src.text_to_html import text_node_to_html_node


class TestTextToHtml(unittest.TestCase):
    def test_text_node_to_html_node(self):
        node = TextNode("This is a paragraph of text.", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertIsInstance(html_node, LeafNode)

    def test_text_node_to_html_node_value(self):
        node = TextNode("This is a paragraph of text.", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        comparison_node = LeafNode(tag=None, value="This is a paragraph of text.")
        equals = (html_node.tag == comparison_node.tag 
                    and html_node.value == comparison_node.value 
                    and html_node.props == comparison_node.props)
        self.assertEqual(equals, True)

    def test_text_node_to_html_text_tag(self):
        node = TextNode("This is text.", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)

    def test_text_node_to_html_bold_tag(self):
        node = TextNode("This is text.", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
    
    def test_text_node_to_html_italic_tag(self):
        node = TextNode("This is text.", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")

    def test_text_node_to_html_code_tag(self):
        node = TextNode("This is text.", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")

    def test_text_node_to_html_link_tag(self):
        node = TextNode("This is text.", TextType.LINK)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")

    def test_text_node_to_html_link_prop(self):
        node = TextNode("This is text.", TextType.LINK, "aurl")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.props["href"], "aurl")

    def test_text_node_to_html_image_tag(self):
        node = TextNode("This is text.", TextType.IMAGE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")

    def test_text_node_to_html_image_value(self):
        node = TextNode("This is text.", TextType.IMAGE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.value, None)

    def test_text_node_to_html_image_props(self):
        node = TextNode("This is text.", TextType.IMAGE, "aurl")
        html_node = text_node_to_html_node(node)
        equals = html_node.props["alt"] == "This is text." and html_node.props["src"] == "aurl"
        self.assertEqual(equals, True)

    
if __name__ == "__main__":
    unittest.main()
