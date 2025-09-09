

class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value 
        self.children = value 
        self.props = props 

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props:
            str = ""
            for k, v in self.props.items():
                str += f' {k}="{v}"'

            print("String: ", str)
            return str 

    def __repr__(self):
        return f"""
tag: {self.tag}
value: {self.value}
children: {self.children}
props: {self.props}
"""

    def __eq__(self, other):
        if isinstance(other, HTMLNode):
            return self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props 



