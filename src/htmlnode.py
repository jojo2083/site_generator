import html

class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None:
            return ""
        
        html_parts = []  # Use a list to collect attribute strings
        for key, value in self.props.items():
            escaped_value = html.escape(value)
            html_parts.append(f' {key}="{escaped_value}"')
        return "".join(html_parts)

    
    def __repr__(self):
        return f"tag = {self.tag}, value= {self.value}, children= {self.children}, props = {self.props}"
    
class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        if value == None:
            raise ValueError("LeafNode must have a value.")
        super().__init__(tag, value = value, children = None, props= props)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value.")
        if self.tag is None:
            return str(self.value)  # Return raw value if no tag is specified
        # Generate tag attributes using parent class's method
        attributes = self.props_to_html()
        return f"<{self.tag}{attributes}>{html.escape(self.value)}</{self.tag}>"