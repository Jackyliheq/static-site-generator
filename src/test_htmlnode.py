import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_multiple(self):
        node = HTMLNode(
            "a",
            "Click me",
            None,
            {"href": "https://www.google.com", "target": "_blank"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' href="https://www.google.com" target="_blank"'
        )
    
    def test_props_to_html_none(self):
        node = HTMLNode("p", "Hello, world!")
        self.assertEqual(node.props_to_html(), "")
        
    def test_values(self):
        node = HTMLNode("div", "I wish I could read")
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "I wish I could read")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)
        
    def test_props_to_html_empty_dict(self):
        node = HTMLNode("div", None, None, {})
        self.assertEqual(node.props_to_html(), "")
    
    
    
    
    
    
    
if __name__ == "__main__":
    unittest.main()    