from tkinter import *
from functions import *

window = Tk()
window.title('Spotify Playlist Generator')
window.geometry("300x300+10+10")
window.configure(background="#CDF7FF")

# LABEL
label_select_genres = Label(window, text="Select your Genres", bg='#A0DEEA', fg='white', font=("Helvetica", 16))
label_select_genres.place(x=85, y=70)

# FRAME
frame = Frame(window)
frame.place(x=80, y=120)

# LISTBOX
genre_selection = Listbox(frame, height=6, selectmode='multiple')
for genre in list_of_genres:
    genre_selection.insert(END, genre)
genre_selection.pack(side=LEFT, fill="x")

# SCROLLBAR
scrollbar = Scrollbar(frame)
scrollbar.pack(side=RIGHT, fill=BOTH)
scrollbar.config(command=genre_selection.yview)

genre_selection.config(yscrollcommand=scrollbar.set)


def user_genres():
    genres = []
    for i in genre_selection.curselection():
        genres.append(genre_selection.get(i))
    return genres


def call_main():
    genres = user_genres()
    main(genres)


# BUTTON
create_playlist_button = Button(window, text="Create Playlist", fg='blue')
create_playlist_button.place(x=80, y=250)
create_playlist_button.bind('<Button-1>', lambda event: call_main())

if __name__ == "__main__":
    window.mainloop()





