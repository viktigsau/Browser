#!.venv/bin/python3
import re
from bs4 import BeautifulSoup
import rendr
import style


def removeComents(html: str):
    try:
        return html[:html.index("<!--")] + html[html.index("-->") + len("-->"):]
    except ValueError:
        return html

def splitElements(html: str):
    soup = BeautifulSoup(html, 'html.parser')
    # Get all elements directly inside the HTML tag
    top_level_elements_html = [str(child) for child in soup.contents if child.name]
    return top_level_elements_html

def get_attr_from_string(attr: str):
    attrs = {}
    current_attr_id = ""
    current_value = ""

    string_identifyer = ""

    getting_value = False

    for char in attr:
        if char == "=":
            current_attr_id = current_value
            current_value = ""
            getting_value = True
            continue
        if getting_value:
            if string_identifyer == "":
                string_identifyer = char
                continue
            if char == string_identifyer:
                getting_value = False
                attrs[current_attr_id] = current_value
                current_attr_id = ""
                current_value = ""
                string_identifyer = ""
                continue
            current_value += char
            continue
        current_value += char

    return attrs

self_closing = []

renderers = {"html": rendr.html,
             "head": rendr.head,
             "body": rendr.body,
             "title": rendr.title, 
            "h1":rendr.h1, 
            "div": rendr.div,
            "p": rendr.p,}

class Element:
    def __init__(self, children: list=None, type: str="div", attributes: dict=None, innerHTML: str="", innerText: str="", is_self_closing: bool=False):
        self.children = children if children else []

        self.type = type

        self.attrs = attributes

        self.is_self_closing = is_self_closing

        self.innerHTML = innerHTML
        self.innerText = innerText

        self.style = style.Style(self)

        if "style" in self.attrs:
            self.style.from_attr(self.attrs.get("style", ""))

        for child in splitElements(innerHTML):
            self.children.append(Element.from_html(child))
        
    def __getitem__(self, key):
        return self.attrs[key]
    
    def __setitem__(self, key, value):
        self.attrs[key] = value
    
    def __delitem__(self, key):
        del self.attrs[key]

    def from_html(html: str) -> "Element":
        html = removeComents(html)

        if html.lower().startswith("<!doctype html>"):
            html = html[len("<!DOCTYPE html>"):]

        html = html.removeprefix("\n")

        type = html.lstrip().removeprefix("<").split(" ")[0].split(">")[0]

        attrs_str = html.removeprefix(f"<{type}").split(">")[0].lstrip()

        attrs = get_attr_from_string(attrs_str)

        try:
            is_self_closing = False
            innerHTML = html[len(f"<{type}{' ' if attrs_str != '' else ''}{attrs_str}>"):html.index(f"</{type}>")].removeprefix("\n").removesuffix("\n")
        except ValueError:
            is_self_closing = True
            innerHTML = None

        element = Element(type=type, attributes=attrs, innerHTML=innerHTML, is_self_closing=is_self_closing)

        return element
    
    def __repr__(self, as_child=False):
        if as_child:
            string = ""

            string += f"\ttag: {self.type}\n"
            string += f"\tattributes: {self.attrs}\n"
            string += f"\tchildren: {len(self.children)}\n"
            string += f"\tinnerText length: {len(self.innerText)}\n"
            string += f"\tinnerHTML length: {len(self.innerHTML)}\n"

            return string

        string = ""

        string += f"tag: {self.type}\n"
        string += f"attributes: {self.attrs}\n"
        string += f"children: {len(self.children)}\n"
        string += f"innerText length: {len(self.innerText)}\n"
        string += f"innerHTML length: {len(self.innerHTML)}\n\n"

        string += "children:\n"
        for child in self.children:
            string += f"{child.__repr__(as_child=True)}"
            string += "\t"+"-"*20 + "\n"
        
        string = string.removesuffix("\t"+"-"*20 + "\n").removesuffix("\n")

        return string
    
    def render(self, window):
        if self.type in renderers:
            renderers[self.type](self, window)
            return True
        return False

if __name__ == "__main__":

    with open("test/index.html", "r") as file:
        html = file.read()

    element: Element = Element.from_html(html)

    print(element)