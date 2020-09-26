import random
import sys
import time
import os
from color import *

from datetime import datetime




def Controls():
    print(eu.C+'Welcome to the guessing game version 1.2.5')
    print('--'*10)
    c2 = print('Press Enter to Start\n')
    input()
    
    global un
    un = input('Please enter a username!')
    
    
    time.sleep(0.4)
    if un.lower() == '':
        os.system('clear')
        print('HELLO: Guest')
      
      
    else:
        os.system('clear')
        print('HELLO: ', un)
      
    print('--'*10)
Controls()
    
    
def difficulty():
    print('Difficuty:')
    print('Press e for easy. Press h for Hard. ' )
    c3 = input('Easy, Hard: \n')
    os.system('clear')
    
    difficulty = 0
    e = 5
    h = 10
    global points
    points = 0
    if c3.lower() == 'e' :
        difficulty = e
        
        
        
        
        print('Setting to Easy')
        animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

        for i in range(len(animation)):
          
          time.sleep(0.001)
          sys.stdout.write("\r" + animation[i % len(animation)])
          sys.stdout.flush()

        print("\n")

        start_time = datetime.now()
        time.sleep(0.4)
    elif c3.lower() == 'h':
        difficulty = h
        
        
        
        print('Setting to Hard')
        animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

        for i in range(len(animation)):
          
          time.sleep(0.3)
          sys.stdout.write("\r" + animation[i % len(animation)])
          sys.stdout.flush()
          

        print("\n")

        start_time = datetime.now()
        time.sleep(0.8)
    
    def restart():
      
      choice = input("Want to play again y/n\n")
      if choice.lower() == "y":
          os.system('clear')
          game()

          
      elif choice.lower() =="n":
          os.system('clear')
      
          animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

          for i in range(len(animation)):
              t = random.randint(0, 1)
          
              time.sleep(t)
              sys.stdout.write("\r" + animation[i % len(animation)])
              sys.stdout.flush()
          
        
          print('GOOD BYE, PLAY AGAIN SOON!!')
          print('--'*10)
          end_time = datetime.now()
        
          print('Time of game play: {}'.format(end_time - start_time))
          print('--'*10)
          print(un,'! You Finished with ',points, ' points!!')
          q = input()
          if q.lower() == '':
              sys.exit()
        
        
        
    def game():
        
        print('Username: ', un)
        global points
        print("The computer can only guess 1-{0}".format(str(difficulty)))
        time.sleep(0.05)
        print('please pick a number')
        num = int(input())
        
        
        
          
        print("your number:",num)
        print('--'*10)
        g = random.randint(1,difficulty)
        print("computers number: ",g)
        print('--'*10)
        print("Try this number next! ",random.randint(1,difficulty))
        print('--'*10)
        
        if num == g:
            os.system('clear')
            print("Good job you won!! :)")
            print('☑️')
            print('--'*10)
            points = points + 1
            print('Points: ', points)
        else:
            os.system('clear')
            print("You lose :(")
            print('❗')
            print('--'*10)
            print('You earned no points.', '   your current points: ', points)
            print('--'*10)
        
        
        
        
        
        
            




        restart()

        


    game()


difficulty()
