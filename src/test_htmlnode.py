import unittest
from htmlnode import HTMLNode  # Adjust the import as necessary

class TestHTMLNode(unittest.TestCase):

    def test_empty_props(self):
        node = HTMLNode(tag="div", props=None)
        self.assertEqual(node.props_to_html(), "")

    def test_single_prop(self):
        node = HTMLNode(tag="a", props={"href": "https://example.com"})
        self.assertEqual(node.props_to_html(), ' href="https://example.com"')

    def test_multiple_props(self):
        node = HTMLNode(tag="a", props={"href": "https://example.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://example.com" target="_blank"')

    def test_special_characters_in_props(self):
        node = HTMLNode(tag="img", props={"alt": 'An "example" image', "src": "image.png"})
        self.assertEqual(node.props_to_html(), ' alt="An &quot;example&quot; image" src="image.png"')

if __name__ == "__main__":
    unittest.main()