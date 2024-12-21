#!.venv/bin/python3
import requests
import tkinter as tk
import Elements


protocals = ['http', 'https']

class Url:
    def __init__(self, url: str):
        self.url = url

        self.protocal = url.split('://')[0]

        self.domain = url.split('://')[1].split('/')[0]

        self.path = url.split('://')[1].split('/')[1:]

        self.response = None
    
    def get(self):
        if self.response:
            return self.response
        
        self.response = requests.get(self.url)
        return self.response

    def __repr__(self):
        return f'url: {self.url}\nprotocal: {self.protocal}\ndomain: {self.domain}\npath: {self.path}'

class Document:
    def __init__(self, url: Url):
        self.url = url
        self.text = url.get().text

        self.mime = url.get().headers['Content-Type'].split(';')[0]

        self.encoding = url.get().encoding

        if self.mime == 'text/html':
            self.html = Elements.Element.from_html(self.text)
    
    def render(self):
        window = tk.Tk()

        window.title(self.url.url)

        window.geometry('800x600')

        window.configure(background='white')

        self.html.render(window)

        window.mainloop()
    
    def getElementByTagName(self, tag: str) -> Elements.Element:
        for child in self.html.children:
            if child.type == tag:
                return child
        return None