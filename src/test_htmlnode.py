import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode  # Adjust the import as necessary

class TestHTMLNode(unittest.TestCase):
## Test HTML Node cases
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
## Test LeafNode cases
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_no_value(self):
        with self.assertRaises(ValueError) as context:
            LeafNode("p", None)
        self.assertEqual(str(context.exception), "LeafNode must have a value.")
    
    def test_leaf_with_empty_props(self):
        node = LeafNode("p", "No props!", {})
        self.assertEqual(node.to_html(), "<p>No props!</p>")

    def test_leaf_no_tag_returns_raw_value(self):
        node = LeafNode(None, "Raw text without tag")
        self.assertEqual(node.to_html(), "Raw text without tag")
##ParentNode tests
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

if __name__ == "__main__":
    unittest.main()