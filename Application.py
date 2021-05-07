# -*- coding:Utf-8 -*-
from Tkinter import *
from Ball import *
from Racket import *
from Block import *
from random import randrange, uniform
import tkMessageBox



class Application:
    def __init__(self):
        
        #main window parameters
        self.root = Tk()
        self.root.title("HardBlock")
        self.root.protocol("WM_DELETE_WINDOW", self.main_quit)
        self.root.bind('<Escape>',self.main_quit)
        self.width = 640
        self.height = 480
       
        self.frame = Frame(self.root, width=self.width, \
            height=self.height, bg = 'black')
            
        # menu creation
        menu=Menu(self.root)
        self.root.config(menu=menu)
        
        gameMenu = Menu(menu)
        menu.add_cascade(label="Game", menu=gameMenu)
        gameMenu.add_command(label="New game", command=self.newGame)
        gameMenu.add_command(label="Preferences")
        gameMenu.add_command(label="Quit", command=self.main_quit)
        
        helpMenu = Menu(menu)
        menu.add_cascade(label="Help", menu=helpMenu)
        helpMenu.add_command(label="aide")
        

        self.can =  Canvas(self.frame, width=self.width-5, \
            height=self.height-5, bg = 'grey')
            
        # racket initialization
        self.racket_player = Racket(self.can)
        
         # ball initialization
        self.ball = Ball(self.can, self.root)
        
        self.root.bind_all('<Left>', self.racket_player.move_left)
        self.root.bind_all('<Right>', self.racket_player.move_right)
        self.root.bind_all('<Up>', self.launch)
        

       
        self.can.pack()
        self.frame.pack()
        
        
        
        
    def launch(self, event):
        global game_started
        if game_started == 1:
            return 1
        else:
            game_started = 1
            print "game started !"
            self.play()
            return 0 
           
    def play(self):
        if game_started == 1:
            self.ball.move(self.racket_player.x, self.racket_player.x + self.racket_player.width)
            self.ball.redraw()
            self.root.after(10, self.play)
        else:
            return 1
        
    
    def main_quit(self, event=None):
        #~ if tkMessageBox.askokcancel("Quit", "Do you really wish to quit?"):
        self.root.destroy()
            
    def newGame(self):
        self.root.destroy()
        app=Application()
