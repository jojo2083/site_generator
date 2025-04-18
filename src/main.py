from textnode import TextNode, TextType

def main():
    node = TextNode("I will figure this out", TextType.LINK, "https://boot.dev")
    print(node)

if __name__ == "__main__":
    main()