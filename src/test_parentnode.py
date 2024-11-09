import unittest

from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        node = ParentNode("p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        node_html = node.to_html()
        self.assertEqual(node_html, '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>')

    def test_to_html_parent(self):
        node = ParentNode( "t",
            [ParentNode("p",
                [
                    LeafNode("b", "Bold text"),
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text"),
                ],
            )]
        )

        node_html = node.to_html()
        self.assertEqual(node_html, '<t><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p></t>')

    def test_to_html_empty_tag(self):
        node = ParentNode("", [LeafNode("b", "Bold text")])
        with self.assertRaises(ValueError, msg="error: no tag"):
            node.to_html()

    def test_to_html_no_tag(self):
        node = ParentNode(None, [LeafNode("b", "Bold text")])
        with self.assertRaises(ValueError, msg="error: no tag"):
            node.to_html()

    def test_to_html_no_children(self):
        node = ParentNode("p", None)
        with self.assertRaises(ValueError, msg="error: no children"):
            node.to_html()

    def test_to_html_empty_children(self):
        node = ParentNode("p", [])
        with self.assertRaises(ValueError, msg="error: no children"):
            node.to_html()

    def test_to_html_props(self):
        node = ParentNode("p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ], props = {"prop": "value"}
        )
        node_html = node.to_html()
        self.assertEqual(node_html, '<p prop="value"><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>')

if __name__ == "__main__":
    unittest.main()