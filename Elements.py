def get_elements(html: str):
    ...

class Element:
    def __init__(self, children: list, type: str, attributes: dict):
        self.children = children

        self.type = type

        self.attrs = attributes
        
    def __getitem__(self, key):
        return self.attrs[key]
    
    def __setitem__(self, key, value):
        self.attrs[key] = value

if __name__ == "__main__":
    element = Element([], 'div', {'class': 'container'})

    element['id'] = 'main'

    print(element['id'])