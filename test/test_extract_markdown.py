import unittest

from src.extract_markdown import extract_markdown_images, extract_markdown_links, extract_title


class TestExtractMarkdown(unittest.TestCase):
    def test_extract_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        extracted_images = extract_markdown_images(text)
        self.assertEqual(extracted_images, [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])

    def test_extract_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        extracted_links = extract_markdown_links(text)
        self.assertEqual(extracted_links, [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")])
    
    def test_extract_no_images(self):
        text = "This is text"
        extracted_images = extract_markdown_images(text)
        self.assertEqual(extracted_images, [])
    
    def test_extract_no_links(self):
        text = "This is text"
        extracted_links = extract_markdown_links(text)
        self.assertEqual(extracted_links, [])

    def test_extract_images_with_links(self):
        text = "This is text with a [to boot dev](https://www.boot.dev) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        extracted_images = extract_markdown_images(text)
        self.assertEqual(extracted_images, [("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])

    def test_extract_links_with_images(self):
        text = "This is text with a [to boot dev](https://www.boot.dev) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        extracted_links = extract_markdown_links(text)
        self.assertEqual(extracted_links, [("to boot dev", "https://www.boot.dev")])

    def test_extract_title(self):
        markdown = "#    title   \n\n>quote#\n\n*something else\n\ntext here"
        title = extract_title(markdown)
        self.assertEqual(title, "title")

    def test_extract_title_error(self):
        markdown = ">quote#\n\n*something else\n\ntext here"
        with self.assertRaises(Exception, msg="Error: No Title Found"):
            extract_title(markdown)


if __name__ == "__main__":
    unittest.main()