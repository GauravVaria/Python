import tkinter as tk
from pygame import mixer #pip install pygame
from tkinter import filedialog
import tkinter.font as font
from PIL import ImageTk, Image #pip install pillow
splash_root = tk.Tk()

# Adjust size
splash_root.geometry("512x575")

# Set Label
logo = ImageTk.PhotoImage(Image.open('.\\Logo\\logo.jpg'))
logo_label = tk.Label(image=logo)
logo_label.pack()
splash_font = font.Font(family = 'Times New Roman', size = 30, weight = 'bold', slant = 'italic')
splash_label = tk.Label(splash_root,text="Know your music.", font = splash_font)
splash_label.pack()
def main():
    splash_root.destroy()
    mixer.init() # Initialize mixer
    window = tk.Tk()
    window.geometry('1190x595')
    window.resizable(False,False) # Window not resizable
    window.title('nPlayer'.center(370)) # Center Title

    defined_font = font.Font(family='Helvetica')

    songs_list=tk.Listbox(window,selectmode=tk.SINGLE,bg="black",fg="white",font=('arial',15),
                          height=21,width=109,selectbackground="gray",selectforeground="black")
    songs_list.grid(columnspan=9)

    my_menu=tk.Menu(window)
    window.config(menu=my_menu)
    add_song_menu=tk.Menu(my_menu)
    my_menu.add_cascade(label="Menu",menu=add_song_menu)

    def addsongs():
        #to open a file  
        temp_song=filedialog.askopenfilenames(initialdir="Project\Music",title="Choose a song",
                                              filetypes=(("mp3 Files","*.mp3"),))
        # ##loop through every item in the list to insert in the listbox
        for s in temp_song:
            s=s.replace("Project\Music","")
            songs_list.insert(tk.END,s)

    add_song_menu.add_command(label="Add songs",command=addsongs)

    def deletesong():
        curr_song=songs_list.curselection()
        songs_list.delete(curr_song[0])

    add_song_menu.add_command(label="Delete song",command=deletesong)

    def previous():
        #to get the selected song index
        previous_one=songs_list.curselection()
        #to get the previous song index
        previous_one=previous_one[0]-1
        #to get the previous song
        temp2=songs_list.get(previous_one)
        mixer.music.load(temp2)
        mixer.music.play()
        songs_list.selection_clear(0,tk.END)
        #activate new song
        songs_list.activate(previous_one)
        #set the next song
        songs_list.selection_set(previous_one)

    previous_button = tk.Button(window, text='Previous', command = previous, width = 25,
                                 height = 4, font=defined_font)
    previous_button.grid(column=0, row = 1)

    def pause():
        mixer.music.pause()

    pause_button = tk.Button(window, text='Pause', command = pause, width = 25,
                             height = 4, font=defined_font)
    pause_button.grid(column=1, row = 1)

    def play():
        song=songs_list.get(tk.ACTIVE)
        mixer.music.load(song)
        mixer.music.play()

    play_button = tk.Button(window, text='Play', command = play, width = 25,
                             height = 4, font=defined_font)
    play_button.grid(column=2, row = 1)

    def resume():
        mixer.music.unpause()
        songs_list.selection_clear(tk.ACTIVE)

    resume_button = tk.Button(window, text='Resume', command = resume, width = 25,
                               height = 4, font=defined_font)
    resume_button.grid(column=3, row = 1)

    def next():
        #to get the selected song index
        next_one=songs_list.curselection()
        #to get the next song index
        next_one=next_one[0]+1
        #to get the next song 
        temp=songs_list.get(next_one)
        mixer.music.load(temp)
        mixer.music.play()
        songs_list.selection_clear(0,tk.END)
        #activate newsong
        songs_list.activate(next_one)
         #set the next song
        songs_list.selection_set(next_one)

    next_button = tk.Button(window, text='Next', command = next, width = 25,
                             height = 4, font=defined_font)
    next_button.grid(column=4, row = 1)

# Set Interval
splash_root.after(3000,main)
 
# Execute tkinter
tk.mainloop()