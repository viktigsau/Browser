import tkinter as tk


def html(self, window):
    for child in self.children:
        child.render(window)

def head(self, window):
    for child in self.children:
        child.render(window)

def body(self, window):

    background_color = self.style['background-color']

    if background_color:
        window.configure(background=background_color)

    for child in self.children:
        child.render(window)

def title(self, window):
    window.title(self.innerHTML)

def h1(self, window):

    print(self.style)

    font = self.style['font']
    font_size = self.style['font-size']

    background_color = self.style['background-color']
    color = self.style['color']

    if not font:
        font = "Arial"
    
    if not font_size:
        font_size = 24
    
    if not color:
        color = "black"

    label = tk.Label(window, text=self.innerHTML, font=(font, font_size), anchor='w')
    
    if background_color:
        label.configure(bg=background_color)
    else:
        label.configure(bg=window.cget('bg'))  # Use the window's background color for transparency
    
    label.configure(fg=color)
    label.pack(anchor='nw')

def div(self, window):
    background_color = self.style['background-color']

    width = self.style['width']
    height = self.style['height']

    if not width:
        width = "0px"
    
    if not height:
        height = "0px"

    if background_color:
        frame = tk.Frame(window, bg=background_color)
    else:
        frame = tk.Frame(window, bg=window.cget('bg'))  # Use the window's background color for transparency

    for child in self.children:
        child.render(frame)
    
    frame.configure(width=width, height=height)

    frame.pack(anchor='nw')

def p(self, window):
    font = self.style['font']
    font_size = self.style['font-size']

    background_color = self.style['background-color']
    color = self.style['color']

    if not font:
        font = "Arial"
    
    if not font_size:
        font_size = 12
    
    if not color:
        color = "black"

    label = tk.Label(window, text=self.innerHTML, font=(font, font_size), anchor='w')
    
    if background_color:
        label.configure(bg=background_color)
    else:
        label.configure(bg=window.cget('bg'))  # Use the window's background color for transparency
    
    label.configure(fg=color)
    label.pack(anchor='nw')