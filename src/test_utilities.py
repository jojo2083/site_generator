import unittest
from textnode import TextNode, TextType
from htmlnode import LeafNode
from utilities import text_node_to_html_node

class TestTextNodeToHtmlNode(unittest.TestCase):
    def test_text_node_to_html_node_text(self):
        # Create a TextNode
        text_node = TextNode("hello world", TextType.TEXT)
        
        # Convert it to an HTMLNode
        html_node = text_node_to_html_node(text_node)
        
        # Check that the conversion worked correctly
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "hello world")


