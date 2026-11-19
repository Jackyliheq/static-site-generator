import unittest
from textnode import TextNode, TextType, extract_title


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_neq_different_text_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)
        
    def test_neq_different_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
        
    def test_neq_different_url(self):
        node = TextNode("This is a link", TextType.LINK, "https://www.boot.dev")
        node2 = TextNode("This is a link", TextType.LINK)
        self.assertNotEqual(node, node2)
        
        # test extract_title function
    
    def test_extract_title_basic(self):
        self.assertEqual(extract_title("# Hello"), "Hello")

    def test_extract_title_whitespace(self):
        self.assertEqual(extract_title("#   Tolkien Fan Club   "), "Tolkien Fan Club")

    def test_extract_title_multiline_ignores_h2(self):
        md = """
## Subtitle first

Some intro paragraph.

# The Real Title

More body text.
"""
        self.assertEqual(extract_title(md), "The Real Title")

    def test_extract_title_none_raises(self):
        md = """
## Only an H2

No H1 header anywhere in this file.
"""
        with self.assertRaises(Exception):
            extract_title(md)


if __name__ == "__main__":
    unittest.main()