import os
from tkinter import PhotoImage
from PIL import Image
class Album:
    def __init__(self, path=None):
        jpath = os.path.join(path, 'cover.jpg')
        ppath = os.path.join(path, 'cover.png')
        self._icon = PhotoImage(file='./assets/notes.png')
        self._path = path
        if os.path.exists(jpath) and not os.path.exists(ppath):
            cover = Image.open(jpath)
            w, h = cover.size
            if w > 140:
                ratio = (140, int(h * (140 / w)))
                cover = cover.resize(ratio)
                cover.save(ppath)
        if os.path.exists(ppath):
            self._icon = PhotoImage(file=ppath)
    
    @property
    def albumpath(self):
        return self._path
    
    @property
    def albumicon(self):
        return self._icon
