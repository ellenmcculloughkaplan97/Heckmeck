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
        self.score=0
    
    #function to roll the dice randomly
    def roll_dice(self):
        self.score=random.randint(1,6)
        return self.score
    
    #method has been created but not yet implemented. 
    def worm_conversion(self):
        self.go_count['worm'] = self.go_count['6']
        del self.go_count['6']
        return self.go_count
    
    
    def one_roll_sim(self,dice_left): #dice left will be inputted externally
        self.go=[self.roll_dice() for i in range(dice_left)] #rolls 6 dice 
        #fills go_count dictionary with values from that roll
        self.go_count= {str(i):self.go.count(i) for i in self.go}
        #convert into including worms
        if '6' in self.go_count.keys(): #if any sixes were rolled, do conversion
            self.go_count=self.worm_conversion()
        return self.go_count
    
          
"Scoring simulator class"  
class Round(): 
    def __init__(self):
        #dictionary to store the dice a player has saved     
        self.dice_left=8 #initialise the dice left at 8 
        self.saved={'worm':0,'5':0,'4':0,'3':0,'2':0,'1':0}
        self.score=0 #initialise score at 0
        self.overlap_lst=[] #list to check overlap of saved and go count to check if play still possible

    def calc_score(self):
        self.score=sum([int(i)*self.saved[i] for i in self.saved if i!="worm"])
        self.score+=self.saved["worm"]*5 #multiply number of worms by 5 for the score
        return self.score


#how to integrate this into a class, it shares lots of information with Saved_dice, but
#also from Roll class, perhaps it can interact with both of them. 
    def dice_select(self,go_count):
        choice="" #empty string to begin
        while choice not in self.saved.keys(): #re-prompts if user mistypes
            choice=input("Select which number to save: ")
            
            
        if self.saved[choice]!=0:
            print(f"You have already saved {choice}s")
            return self.dice_select(go_count)
            
        elif choice not in go_count.keys(): #make sure they haven't already saved that number: 
            print(f"You did not roll a {choice}")
            return self.dice_select(go_count)
        
        #need to add in a condtion for if all dice are ones that have already been selected
        
        else:
            self.saved[choice]=go_count[choice]
            self.dice_left-=go_count[choice]
            return self.dice_left, self.saved
            
        
    def worm_check(self):
        if self.saved["worm"]==0:
            print("You did not roll any worms, so your go is KAPUT")
            self.score=0
        return self.score
    
    def able_to_save_dice(self,go_count):
        #if all elements are non-zero then all rolled dice have already been saved
        self.overlap_lst=[self.saved[i] for i in go_count.keys()]
        if all(self.overlap_lst)!=0: #if every element of overlap list are not zero then we cant choose
            print("You have already saved all the dice you just rolled, you have gone KAPUT")
            return False #they are no longer able to play on
        else: 
            return True #they can play on
        
        

"simulate an entire go"
def Round_simulation():
    this_round=Round()
    while this_round.dice_left>0: #ends loop if run out of dice, calls attribute from this round
        
        roll=Roll() #create instance of Roll class to simulate a roll has taken place
        #throw_dice=str(input("Press Enter to roll the dice: "))
        go_count=roll.one_roll_sim(this_round.dice_left)
        print(" You rolled ")
        print(go_count) #displays dice rolled in that round, including worm
        
        #end go if they can't save anymore dice
        if not this_round.able_to_save_dice(go_count):
            #set score to 0 and end round
            score=0
            break
            
        #currently uses a procedural function, need to change into a class
        dice_left, saved=this_round.dice_select(go_count)
        score=this_round.calc_score()
        print(f"Your score is {score}") 
        print(f"You have {dice_left} dice left")
        if score>=21 and dice_left>0: #can't keep playing if no dice are left to throw 
            play_on=str(input("Do you want to keep rolling? (y/n)"))
            if play_on=="n":
                break
            
    score=this_round.worm_check() #check if the go had worms in it 
    print(f"Your score for this round is {score}")
    return score
  

Round_simulation()


    
    



