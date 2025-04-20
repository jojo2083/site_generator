from textnode import TextNode, TextType
from htmlnode import HTMLNode, ParentNode, LeafNode
from utilities import text_node_to_html_node

def main():
    node = TextNode("I will figure this out", TextType.LINK, "https://boot.dev")
    print(node)

if __name__ == "__main__":
    main()