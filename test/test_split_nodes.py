import unittest

from src.textnode import TextNode, TextType
from src.split_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link


class TestSplitNodesDelimiter(unittest.TestCase):

    def test_split_nodes_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ])

    def test_unequal_delimiters(self):
        node = TextNode("This is text with a `code block word", TextType.TEXT)
        with self.assertRaises(Exception, msg="Invalid markdown: Number of delimiters is not even"):
            new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

    def test_multiple_delimiter_instances(self):
        node = TextNode("This is `text` with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.CODE),
            TextNode(" with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ])

    def test_delimiter_only_string(self):
        node = TextNode("**bold**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [TextNode("bold", TextType.BOLD)])

    def test_spacing_in_delimited_text(self):
        node = TextNode("** bold **", TextType.TEXT)
        with self.assertRaises(Exception, msg="Invalid markdown: Spacing between delimiter and text"):
            new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)

    def test_delimiter_empty(self):
        node = TextNode("This is **** something", TextType.TEXT)
        with self.assertRaises(Exception, msg="Invalid markdown: no text within delimiters"):
            new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)    

    def test_non_text_node(self):
        node = TextNode("already bold", TextType.BOLD)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertEqual(new_nodes, [TextNode("already bold", TextType.BOLD)])

    def test_italic_nodes_delimiter(self):
        node = TextNode("This is text with a *code* word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code", TextType.ITALIC),
            TextNode(" word", TextType.TEXT),
        ])

    def test_multiple_nodes_delimiter(self):
        node = TextNode("This is text with a *code* word", TextType.TEXT)
        node2 = TextNode("Another *italic* node", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node, node2], "*", TextType.ITALIC)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code", TextType.ITALIC),
            TextNode(" word", TextType.TEXT),
            TextNode("Another ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" node", TextType.TEXT),
        ])

    def test_image_nodes(self):
        node = TextNode("This is text with images ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertEqual(new_nodes, [
            TextNode("This is text with images ", TextType.TEXT),
            TextNode("to boot dev", TextType.IMAGE, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("to youtube", TextType.IMAGE, "https://www.youtube.com/@bootdotdev"),
        ])
    
    def test_split_images_on_other_nodes(self):
        nodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code", TextType.ITALIC),
            TextNode(" word", TextType.TEXT),
            TextNode("Another ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" node", TextType.TEXT)
        ]
        new_nodes = split_nodes_image(nodes)
        self.assertEqual(new_nodes, nodes)

    def test_split_images_on_many_nodes(self):
        nodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code", TextType.ITALIC),
            TextNode("This is text with images ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)", TextType.TEXT)
        ]
        new_nodes = split_nodes_image(nodes)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code", TextType.ITALIC),
            TextNode("This is text with images ", TextType.TEXT),
            TextNode("to boot dev", TextType.IMAGE, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("to youtube", TextType.IMAGE, "https://www.youtube.com/@bootdotdev"),
        ])

    def test_links_nodes(self):
        node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.TEXT,)
        new_nodes = split_nodes_link([node])
        self.assertEqual(new_nodes, [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
        ])
 

if __name__ == "__main__":
    unittest.main()