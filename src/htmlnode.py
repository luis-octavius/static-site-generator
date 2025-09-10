

class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value 
        self.children = children  
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
        return 

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

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value:
            raise ValueError 
        
        if not self.tag:
            return str(self.value)

        print("Props: ", self.props)
        
        if self.props == None:
            return f'<{self.tag}>{self.value}</{self.tag}>'
        else:
            return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
