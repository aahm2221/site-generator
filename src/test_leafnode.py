import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("p", "This is a paragraph of text.")
        node_html = node.to_html()
        self.assertEqual(node_html, '<p>This is a paragraph of text.</p>')

    def test_to_html_with_prop(self):
        node =LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        node_html = node.to_html()
        self.assertEqual(node_html, '<a href="https://www.google.com">Click me!</a>')

    def test_to_html_with_props(self):
        node =LeafNode("a", "Click me!", {"href": "https://www.google.com", "prop2": "something"})
        node_html = node.to_html()
        self.assertEqual(node_html, '<a href="https://www.google.com" prop2="something">Click me!</a>')

    def test_to_html_no_tag(self):
        node = LeafNode(None, "This is a paragraph of text.")
        node_html = node.to_html()
        self.assertEqual(node_html, 'This is a paragraph of text.')

    def test_to_html_empty_value(self):
        node = LeafNode("p", "")
        with self.assertRaises(ValueError):
            node.to_html()

if __name__ == "__main__":
    unittest.main()