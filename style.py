class Style:
    def __init__(self, element):
        self.element = element
        self.styles = {}
    
    def from_attr(self, attr: str):
        attr = attr.split(";")
        for style in attr:
            if style == "":
                continue
            style = style.split(":")
            self.styles[style[0].lstrip().strip()] = style[1].lstrip().strip()
    
    def __getitem__(self, key):
        try:
            return self.styles[key]
        except KeyError:
            return None

    def __setitem__(self, key, value):
        self.styles[key] = value
    
    def __delitem__(self, key):
        try:
            del self.styles[key]
        except KeyError:
            return None
    
    def __repr__(self):
        return str(self.styles)