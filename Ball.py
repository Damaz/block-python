from Tkinter import *
from Ball import *
from Racket import *
from Block import *
import main

class Ball:
    def __init__(self, canvas, root):
        # ball caracteristics
        self.radius = 10
        self.x = 350
        self.y = 379
        self.canvas = canvas
        self.alive = 1
        # ball path
        self.a = 1
        self.b = -1
        
        self.root = root
        
        self.ball = self.canvas.create_oval(self.x-self.radius, \
            self.y-self.radius, self.x+self.radius, self.y+self.radius, \
            fill='Purple', outline='black', width=2)
        return

    def redraw(self):
        print self.x , self.y
        self.canvas.coords(self.ball, self.x-self.radius, self.y-self.radius, self.x+self.radius, self.y+self.radius)
        return
        
    def move(self, leftside, rightside):
        if (self.alive == 1):
            bool_top = self.top_contact()
            bool_right = self.right_contact()
            bool_left = self.left_contact()
            bool_bottom = self.bottom_contact(leftside,rightside)
            self.x = self.a + self.x
            self.y = self.b + self.y
            
            return True
        else:
            return False

    # Fonctions de test pour les bords du canevas
    def top_contact(self):
        if (self.y-self.radius <= 0):
            self.b = -self.b
    
    def bottom_contact(self, leftside, rightside):
        global game_started
        if (self.y+self.radius >= 390):
            if (self.x > leftside) & (self.x < rightside):
                self.b = -self.b
            else:
                game_started = 0
                
    
    def right_contact(self):
        if (self.x+self.radius >= 635):
            self.a = -self.a
        
    def left_contact(self):
        if (self.x-self.radius <= 0):
            self.a = -self.a




    def bounce(self):
        return
    
    
