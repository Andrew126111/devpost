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

    delays = [
    0.1,  # Santa, tell me if you're really there
    0.08,  # Don't make me fall in love again
    0.09,  # If he won't be here next year
    0.1,  # Santa, tell me if he really cares
    0.09,  # 'Cause I can't give it all away
    0.08,  # If he won't be here next year
    0.1,  # Feeling Christmas all around
    0.09,  # And I'm trying to play it cool
    0.1,  # But it's hard to focus when I see him walking 'cross the room
    0.08,  # Let it snow, it's blasting now
    0.09,  # But I won't get in the mood
    0.1,  # I'm avoiding every mistletoe until I know
    0.09,  # It's true love that he thinks of
    0.1,  # So next Christmas, I'm not all alone, boy
    0.1,  # Santa, tell me if you're really there
    0.08,  # Don't make me fall in love again
    0.1,  # If he won't be here next year
    0.1,  # Santa, tell me if he really cares
    0.09,  # 'Cause I can't give it all away
    0.08,  # If he won't be here next year
    0.1,  # I've been down this road before
    0.09,  # Fell in love on Christmas night
    0.09,  # But on New Year's Day I woke up and he wasn't by my side
    0.1,  # Now I need someone to hold
    0.1,  # Be my fire in the cold
    0.1,  # But it's hard to tell if this is just a fling or if it's true love
    0.1,  # That he thinks of
    0.1,  # So next Christmas, I'm not all alone, boy
    0.1,  # Santa, tell me if you're really there
    0.08,  # Don't make me fall in love again
    0.1,  # If he won't be here next year
    0.1,  # Santa, tell me if he really cares
    0.09,  # 'Cause I can't give it all away
    0.1,  # If he won't be here next year
    0.1,  # Oh, I wanna have him beside me like oh-oh-oh
    0.1,  # On the 25th by the fireplace, oh-oh-oh
    0.09,  # But I don't want a new broken heart
    0.1,  # This year I've got to be smart
    0.09,  # Oh, baby
    0.1,  # If you won't be, if you won't be here
    0.08,  # Oh-oh-oh
    0.1,  # Santa, tell me if you're really there
    0.08,  # Don't make me fall in love again
    0.1,  # If he won't be here next year
    0.1,  # Santa, tell me if he really cares
    0.09,  # 'Cause I can't give it all away
    0.1,  # If he won't be here next year
    0.1,  # Santa, tell me if you're really there
    0.09,  # Don't make me fall in love again
    0.1,  # If he won't be here next year
    0.1,  # Santa, tell me if he really cares
    0.09,  # 'Cause I can't give it all away
    0.1   # If he won't be here next year
]


    text_box.delete("1.0", tk.END)  # Clear the text box

    for i, (line, char_delay) in enumerate(lines):
        if i < len(delays):  # Apply line-specific delay from the delays list
            sleep(delays[i])  # Delay between lines
        for char in line:
            text_box.insert(tk.END, char)
            text_box.update_idletasks()
            sleep(char_delay)  # Delay between characters
        text_box.insert(tk.END, "\n")
        text_box.update_idletasks()

        # Auto-scroll the text box to show new lines
        text_box.yview(tk.END)

def startLyrics():
    """Starts printing lyrics in a separate thread."""
    Thread(target=printLyrics).start()

def startMusic():
    """Plays the song and schedules the lyrics to start after 11 seconds."""
    mixer.init()
    mixer.music.load(music_file)
    mixer.music.play()
    # Schedule lyrics to start after 11 seconds
    root.after(11000, startLyrics)

def stopMusic():
    """Stops the music."""
    mixer.music.stop()

# Path to the music file
music_file = "/Users/andrewnguyen/Downloads/Ariana Grande – Santa Tell Me [ ezmp3.cc ].mp3"

# Create the main Tkinter window
root = tk.Tk()
root.title("Santa Tell Me Lyrics Player")
root.geometry("600x400")

# Create GUI widgets with a Christmas-themed font and color (Comic Sans MS or a custom font)
text_box = tk.Text(root, wrap=tk.WORD, height=15, width=70, font=("Comic Sans MS", 14, "italic"), fg="#00FF00", bg="#8B0000", padx=10, pady=10)
text_box.pack(pady=10)

play_button = tk.Button(root, text="Play Music", command=startMusic, font=("Comic Sans MS", 12), fg="red", bg="green")
play_button.pack(side=tk.LEFT, padx=10, pady=10)

stop_button = tk.Button(root, text="Stop Music", command=stopMusic, font=("Comic Sans MS", 12), fg="red", bg="green")
stop_button.pack(side=tk.LEFT, padx=10, pady=10)

# Run the Tkinter main loop
root.mainloop()