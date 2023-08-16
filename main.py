from tkinter import *
import random
import pandas

data = pandas.read_csv("data/jap_engl.csv", sep="\t")
BACKGROUND_COLOR = "#B1DDC6"
data_dict = data.to_dict(orient="records") # {row.Polski: row.Deutch for(index, row) in data.iterrows()}

current_choice = {}


# ---------------------------- RANDOM WORD ------------------------------- #


def wybieram():
    canvas.itemconfig(card_background, image=card_front_pic)
    global current_choice, flip_timer
    window.after_cancel(flip_timer)
    current_choice = random.choice(data_dict)

    canvas.itemconfig(text_front, text=current_choice["Japanese"], fill="black")
    canvas.itemconfig(text_front_title, text="Japanese", fill="black")
    flip_timer = window.after(5000, flip_card)
    return current_choice


def flip_card():

    canvas.itemconfig(card_background, image=card_back_pic)
    canvas.itemconfig(text_front, text=current_choice["English"], fill="white", font=("Arial", 30))
    canvas.itemconfig(text_front_title, text="English", fill="white")

# ---------------------------- BUTTONS ------------------------------- #



# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Japs flashcards for Bączek")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(4000, flip_card)
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

card_front_pic = PhotoImage(file="images/card_front.png")
card_back_pic = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_pic)
text_front_title = canvas.create_text(380, 150, text="", fill="black", font=("Arial", 40, "italic"))
text_front = canvas.create_text(380, 260, text="", fill="black", font=("Arial", 40, "bold"))
canvas.grid(column=0, columnspan=2, row=0)


button_right_pic = PhotoImage(file="images/right.png")
button_right = Button(image=button_right_pic, highlightthickness=0, bg=BACKGROUND_COLOR, command=wybieram)
button_right.grid(column=1, row=1)

button_wrong_pic = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=button_wrong_pic, highlightthickness=0, bg=BACKGROUND_COLOR, command=wybieram)
button_wrong.grid(column=0, row=1)

wybieram()
window.mainloop()
