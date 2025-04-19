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