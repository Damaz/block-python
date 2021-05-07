from Tkinter import *
from Ball import *
from Racket import *
from Block import *
from main import *
from Application import *

class Racket:
    def __init__(self, canvas):
        self.width = 100
        self.height = 10
        self.speed = 1
        self.x = 300
        self.y = 390
        self.canvas = canvas
        self.racket = self.canvas.create_rectangle(self.x, \
            self.y, self.x+self.width, self.y+self.height, \
            fill='SlateBlue', outline='DarkSlateBlue', width=3)
        return 
    
    def move_left(self, event):
        global game_started
        
        if (self.x - 25 > 0):
            self.x = self.x - 25
            self.redraw()
            return 0
            
        elif (self.x - 25 <= 0):
            self.x = 0
            self.redraw()
            return 0
        else:
            return 1
    
    def move_right(self, event):
        global game_started
        
        if ((self.x+25+self.width) < 635):
            self.x = self.x+25
            self.redraw()
            return 0
            
        elif ((self.x+self.width+25) >= 635):
            self.x = 635 - self.width
            self.redraw()
            return 0

        else:
            return 1


    def redraw(self):
        self.canvas.coords(self.racket, self.x, self.y, \
            self.x+self.width, self.y+self.height)
        return 0
