# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 14:31:13 2025

@author: ellen
"""

"""Heckmeck Simulator"""

class Tile:
    def __init__(self,number,worm_score):
        self.number=number
        self.worm_score=worm_score
        self.onboard=True
        self.flipped=False
        

"dictionary to store worm tiles"
worm_dict={}
"loop to create all tiles"
worm_score=1 #initialise worm_score at 1
counter=0
for i in range(21,37): #create tiles with numbers from 21 to 37
    worm_dict[i]=Tile(i,worm_score)
    #worm_score increases every 4 tiles
    counter+=1
    if counter%4==0: 
        worm_score+=1
        
        
import random
"Rolling simulator"
class Roll():
    def __init__(self):
        self.go_count={}
        self.go=[]
    
    #function to roll the dice randomly
    def roll_dice(self):
        score=random.randint(1,6)
        return score
    
    
    def one_roll_sim(self,dice_left): #dice left will be inputted externally
        self.go=[self.roll_dice() for i in range(dice_left)] #rolls 6 dice 
        #fills go_count dictionary with values from that roll
        self.go_count= {i:self.go.count(i) for i in self.go}
        return self.go_count
          
"Scoring simulator class"  
class Round(): 
    def __init__(self):
        #dictionary to store the dice a player has saved     
        self.saved={6:0,5:0,4:0,3:0,2:0,1:0}
        self.score=0 #initialise score at 0

    def calc_score(self):
        self.score=sum([i*self.saved[i] for i in self.saved])
        return self.score


#how to integrate this into a class, it shares lots of information with Saved_dice, but
#also from Roll class, perhaps it can interact with both of them. 
    def dice_select(self,go_count,dice_left):
        choice=int(input("Select which number to save: "))
        if choice in go_count.keys() and self.saved[choice]==0: #make sure they haven't already saved that number: 
            self.saved[choice]=go_count[choice]
            dice_left-=go_count[choice]
            return dice_left, self.saved
        else:
            print("You have already saved this number or you did not roll it")
            #force them to select again
            return self.dice_select(go_count,dice_left)

"simulate an entire go"
dice_left=8
this_round=Round()
while dice_left>0: #ends loop if run out of dice
    
    roll=Roll() #create instance of Roll class to simulate a roll has taken place
    go_count=roll.one_roll_sim(dice_left)
    print(" You rolled ")
    print(go_count) 
    
    #currently uses a procedural function, need to change into a class
    dice_left, saved=this_round.dice_select(go_count,dice_left)
    score=this_round.calc_score()
    print(f"Your score is {score}") 
    if score>=21:
        play_on=str(input("Do you want to keep rolling? (y/n)"))
        if play_on=="n":
            break
        
    #add in going kaput if you don't roll a worm (6) or if you don't hit 21
    #add in something that happens when you can't get over 21. 
    #or when the rolls come up with only numbers you've already save. 
    




    
    



