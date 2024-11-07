from tkinter import Tk, Label
from PIL import Image, ImageTk, ImageSequence
import pygame
from pygame import mixer

# Initialize the mixer for playing music
mixer.init()

def play_music():
    music_path = r"C:\Users\kalas\Downloads\kanye.mp3"
    try:
        mixer.music.load(music_path)
        mixer.music.play()
    except Exception as e:
        print(f"Error loading music: {e}")

def play_gif(root):
    root.lift()  # Bring the window to the front
    root.attributes("-topmost", True)  # Keep the window on top

    global img
    try:
        img = Image.open("C:\\Users\\kalas\\Downloads\\bobmarley.gif")
        lbl = Label(root)  # Create a label in the root window
        lbl.place(x=0, y=0)  # Place the label at the top-left corner

        frames = [ImageTk.PhotoImage(img.resize((1366, 768))) for img in ImageSequence.Iterator(img)]

        total_time = 12000  # Total duration for the GIF (12 seconds)
        frame_duration = total_time // len(frames)  # Time for each frame

        def update_gif(frame_index):
            if frame_index < len(frames):
                lbl.config(image=frames[frame_index])  # Update the label with the current frame
                root.after(frame_duration, update_gif, frame_index + 1)  # Schedule the next frame
            else:
                root.destroy()  # Close the window when done

        update_gif(0)  # Start the GIF
    except Exception as e:
        print(f"Error playing GIF: {e}")

if __name__ == "__main__":
    # Create the root window
    root = Tk()
    root.geometry("1366x768")  # Set the window size
    root.title("Music and GIF Player")  # Set the window title
    play_music()  # Start playing the music
    play_gif(root)  # Pass the root window to play_gif
    root.mainloop()  # Start the Tkinter event loop

     
