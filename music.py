import pygame, os
from tkinter import *
from pygame import mixer
import pygame
import time



class music:

 pygame.init()
 __songs= []

 def __init__(self):

  for root, dirs, files in os.walk( r"C:\Users\Peace\atomprojects"):  # get the files in the directory and subfolders
      for file in files:
          if file.endswith(".ogg"):
             self.__songs.append(file)  # it adds the file that has the extension .ogg

 def print_playlist(self):
     print("\n list of music:")

     for i in range(len(self.__songs)):
         print(i + 1, '-', self.__songs[i])

 def sound_selection(self,sound):
     self.__soundchoice=sound
     for i in range(len(self.__songs)):

         if (self.__soundchoice + ".ogg") == self.__songs[i]:
             pygame.mixer.music.load(self.__soundchoice + ".ogg")
             self.__music_number = i
     for i in range(len(self.__songs)):
         if self.__soundchoice.isdigit():
             pygame.mixer.music.load(self.__songs[int(self.__soundchoice) - 1])
             self.__music_number = int(self.__soundchoice) - 1
             self.__soundchoice = self.__songs[int(self.__soundchoice) - 1]

     pygame.mixer.music.play()
     print("Now Playing: ", self.__soundchoice )



 def nextsong(self):


    mixer.music.stop() #stop the current music


    if self.__music_number+1==len(self.__songs):
        self.__music_number=0
    else:
        self.__music_number=self.__music_number+1
    #music_number = int(music_number2 + 1)
    #music_number2 = (music_number)
    #print (music_number)
    self.current_music = (self.__songs[self.__music_number])
    mixer.music.load(self.current_music)#loads the next music





    time.sleep(0.5)
    mixer.music.play()
    print ("Now Playing: ",self.current_music)
    if self.__music_number + 1 == len(self.__songs):
      self.next_music = (self.__songs[0])
    else:
      self.next_music=self.__songs[self.__music_number+1]
    pygame.mixer.music.queue(self.next_music)
    print ("NEXT SONG: ", self.next_music)



 def prevsong(self):

    mixer.music.stop()
    if self.__music_number == 0:
        self.__music_number = len(self.__songs)-1
    else:
        self.__music_number = self.__music_number - 1


    current_music = (self.__songs[self.__music_number])
    mixer.music.load(current_music)




    print ("Now Playing: ",current_music)

    time.sleep(0.5) #sleep for half a second
    mixer.music.play()



 def playsong(self):
    pygame.mixer.music.play()
    print("Now Playing:",self.__soundchoice)
 def displaysoundchoice(self):
     return self.__soundchoice



 def pausesong(self):
    pygame.mixer.music.pause()


 def resumesong(self):
    pygame.mixer.music.unpause()


 def volumedown(self):
    pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() - 0.1)


 def volumeup(self):
    pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.1)

 def stopsong(self):
    pygame.mixer.music.stop()
