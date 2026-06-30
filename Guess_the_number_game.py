import random
import os
import time
import pygame

pygame.mixer.init()

song_path= os.path.join("victory song.mp3")
num=random.randint(1,100)
attempts =0
max_attempts=15
print(" welcome to guess the number game !!!!")

while attempts < max_attempts:     
    guess=int(input("enter a your guess number"))
    attempts+=1

    if guess>num :
     print("too high!! select smaller number")
    elif guess<num:    
     print(" too small! select higher number")
    else:
     print("won! won!  you guess it right")
     #winsound.PlaySound("systemEclamation",winsound.SND_ALIAS)
     pygame.mixer.music.load(song_path)
     pygame.mixer.music.play()

     time.sleep(5)
     break;     
if guess != num:
  print("game over!!!! you ran out of moves")