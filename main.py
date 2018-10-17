from music import music
from tkinter import *
from os import system
import time

def main():
    system('cls')


    playlist=music()
    playlist.print_playlist()
    " "
    " "
    sound = input("Enter the name of the song you want to play: or select sound according to position: ")
    playlist.sound_selection(sound)

    # WINDOW SETTINGS
    window = Tk()
    window.title("Music Player")
    window.geometry("700x50")

    topFrame = Frame(window)
    topFrame.pack()

    bottomFrame = Frame(window)
    bottomFrame.pack(side=BOTTOM)
    window.resizable(width=False, height=False)


    window["bg"] = "black"

    def quitprogram():
        time.sleep(0.25)
        window.destroy()
        time.sleep(0.25)
        quit()

    playBUTTON = Button(text="PLAY", fg="white")
    playBUTTON.pack(side=LEFT)
    playBUTTON.configure(command=playlist.playsong)
    playBUTTON["bg"] = "black"

    pauseBUTTON = Button(text="PAUSE", fg="white")
    pauseBUTTON.pack(side=LEFT, padx=10)
    pauseBUTTON.configure(command=playlist.pausesong)
    pauseBUTTON["bg"] = "black"

    stopBUTTON = Button(text="Stop", fg="white")
    stopBUTTON.pack(side=LEFT, padx=10)
    stopBUTTON.configure(command=playlist.stopsong)
    stopBUTTON["bg"] = "black"

    nextBUTTON = Button(text=">>>", fg="white")
    nextBUTTON.pack(side=LEFT, padx=10)
    nextBUTTON.configure(command=playlist.nextsong)
    nextBUTTON["bg"] = "black"

    prevBUTTON = Button(text="<<<", fg="white")
    prevBUTTON.pack(side=LEFT, padx=10)
    prevBUTTON.configure(command=playlist.prevsong)
    prevBUTTON["bg"] = "black"

    resumeBUTTON = Button(text="resume", fg="white")
    resumeBUTTON.pack(side=LEFT, padx=10)
    resumeBUTTON.configure(command=playlist.resumesong)
    resumeBUTTON["bg"] = "black"

    volumedownBUTTON = Button(text="VOL -", fg="white")
    volumedownBUTTON.pack(side=LEFT, padx=10)
    volumedownBUTTON.configure(command=playlist.volumedown)
    volumedownBUTTON["bg"] = "black"

    volumeupBUTTON = Button(text="VOL +", fg="white")
    volumeupBUTTON.pack(side=LEFT, padx=10)
    volumeupBUTTON.configure(command=playlist.volumeup)
    volumeupBUTTON["bg"] = "black"

    '''songLABEL = Label(text=playlist.displaysoundchoice(), fg="white")
    songLABEL.pack(side=TOP)
    songLABEL["bg"] = "black"'''
    window.protocol('WM_DELETE_WINDOW', quitprogram)

    # THE WINDOW BEING KEPT OPEN
    window.mainloop()

    #pygame.quit()  # clean exit
if __name__ == '__main__':
    main()
