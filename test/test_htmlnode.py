import unittest

from src.htmlnode import HtmlNode


class TestHtmlNode(unittest.TestCase):
    def test_prop_to_html(self):
        node = HtmlNode(props={"href": "aurl"})
        props_html = node.props_to_html()
        self.assertEqual(props_html, ' href="aurl"')

    def test_props_to_html(self):
        node = HtmlNode(props={"href": "aurl", "prop2": "value"})
        props_html = node.props_to_html()
        self.assertEqual(props_html, ' href="aurl" prop2="value"')

    def test_empty_props(self):
        node = HtmlNode(props={})
        props_html = node.props_to_html()
        self.assertEqual(props_html, "")

    def test_none_props(self):
        node = HtmlNode(tag ="something", value="other thing")
        props_html = node.props_to_html()
        self.assertEqual(props_html, "")

if __name__ == "__main__":
    unittest.main()
