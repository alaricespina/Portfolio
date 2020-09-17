import pygame as pg 

class Main
        def init:
                #variables
                #all commands (arrow keys)
                #quit button
        def collisiondetection(x1,y1,x2,y2):
                #check if player collided with Enemy
                #reward player if did not collide
                #return true or false
        def scoring (collisiondetection):
                #if true from collision detection
                #Remove HP (Starting 3)
                #If HP 0, self.state = lose
                #else if false from collision, detect if x1 <= x2
                #add score if true

class Player
        def init(surface,x,y,dimension):
                #variables
                #starting position
        def move(x,y):
                #move to blah blah
class Enemy
        def init(surface,x,y,dimension):
                #variables
                #starting position
        def move(x,y)
                #move to blah blah
