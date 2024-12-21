import sys
from time import sleep
import time
from threading import Thread
from pygame import mixer
import tkinter as tk
from tkinter import filedialog

def printLyrics():
    lines = [("Santa, tell me if you're really there", 0.1),
            ("Don't make me fall in love again", 0.08),
            ("If he won't be here next year", 0.07),
            ("Santa, tell me if he really cares", 0.099),
            ("'Cause I can't give it all away", 0.09),
            ("If he won't be here next year", 0.07),
            ("Feeling Christmas all around", 0.08),
            ("And I'm trying to play it cool", 0.08),
            ("But it's hard to focus when I see him walking 'cross the room", 0.06),
            ("Let it snow, it's blasting now", 0.08),
            ("But I won't get in the mood", 0.065),
            ("I'm avoiding every mistletoe until I know", 0.09),
            ("It's true love that he thinks of", 0.095),
            ("So next Christmas, I'm not all alone, boy", 0.115),
            ("Santa, tell me if you're really there", 0.1),
            ("Don't make me fall in love again", 0.09),
            ("If he won't be here next year", 0.07),
            ("Santa, tell me if he really cares", 0.11),
            ("'Cause I can't give it all away", 0.06),
            ("If he won't be here next year", 0.09),
            ("I've been down this road before", 0.08),
            ("Fell in love on Christmas night", 0.06),
            ("But on New Year's Day I woke up and he wasn't by my side", 0.06),
            ("Now I need someone to hold", 0.08),
            ("Be my fire in the cold", 0.1),
            ("But it's hard to tell if this is just a fling or if it's true love", 0.065),
            ("That he thinks of", 0.09),
            ("So next Christmas, I'm not all alone, boy", 0.115),
            ("Santa, tell me if you're really there", 0.1),
            ("Don't make me fall in love again", 0.08),
            ("If he won't be here next year", 0.09),
            ("Santa, tell me if he really cares", 0.1),
            ("'Cause I can't give it all away", 0.08),
            ("If he won't be here next year", 0.09),
            ("Oh, I wanna have him beside me like oh-oh-oh", 0.09),
            ("On the 25th by the fireplace, oh-oh-oh", 0.1),
            ("But I don't want a new broken heart", 0.09),
            ("This year I've got to be smart", 0.08),
            ("Oh, baby", 0.07),
            ("If you won't be, if you won't be here", 0.1),
            ("Oh-oh-oh", 0.06),
            ("Santa, tell me if you're really there", 0.1),
            ("Don't make me fall in love again", 0.08),
            ("If he won't be here next year", 0.09),
            ("Santa, tell me if he really cares", 0.099),
            ("'Cause I can't give it all away", 0.09),
            ("If he won't be here next year", 0.09),
            ("Santa, tell me if you're really there", 0.1),
            ("Don't make me fall in love again", 0.08),
            ("If he won't be here next year", 0.09),
            ("Santa, tell me if he really cares", 0.099),
            ("'Cause I can't give it all away", 0.09),
            ("If he won't be here next year", 0.09),
]

    delays = [0.3, 0.4, 0.7, 0.8, 0.35, 0.5, 0.3, 0.5, 0.6, 0.5, 
        0.45, 0.5, 1, 0.9, 0.3, 0.4, 0.8, 0.5, 0.4, 0.1, 
        0.2, 0.9, 0.8, 0.8, 0.65, 0.8, 1.7, 0.3, 0.4, 0.6, 
        0.7, 0.2, 1.1, 1.3, 0.4, 0.5, 1.6, 1, 3, 1, 
        1, 0.3, 0.7, 0.3, 0.3, 0.6, 0.4, 0.3, 0.7, 0.6, 
        0.5, 0.7
]

    text_box.delete("1.0", tk.END)

    for i, (line, char_delay) in enumerate(lines):
        if i < len(delays):
            sleep(delays[i])
        for char in line:
            text_box.insert(tk.END, char)
            text_box.update_idletasks()
            sleep(char_delay)
        text_box.insert(tk.END, "\n")
        text_box.update_idletasks()

        text_box.yview(tk.END)

def startLyrics():

    Thread(target=printLyrics).start()

def startMusic():
    mixer.init()
    mixer.music.load(music_file)
    mixer.music.play()
    
    root.after(11000, startLyrics)

def stopMusic():

    mixer.music.stop()


music_file = "/Users/andrewnguyen/Downloads/Ariana Grande – Santa Tell Me [ ezmp3.cc ].mp3"


root = tk.Tk()
root.title("Santa Tell Me Lyrics Player")
root.geometry("600x400")


text_box = tk.Text(root, wrap=tk.WORD, height=15, width=70, font=("Comic Sans MS", 14, "italic"), fg="#00FF00", bg="#8B0000", padx=10, pady=10)
text_box.pack(pady=10)

play_button = tk.Button(root, text="Play Music", command=startMusic, font=("Comic Sans MS", 12), fg="red", bg="green")
play_button.pack(side=tk.LEFT, padx=10, pady=10)

stop_button = tk.Button(root, text="Stop Music", command=stopMusic, font=("Comic Sans MS", 12), fg="red", bg="green")
stop_button.pack(side=tk.LEFT, padx=10, pady=10)

root.mainloop()
