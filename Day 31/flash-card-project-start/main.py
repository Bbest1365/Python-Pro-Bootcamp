from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
def next_card():




window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
canvas.create_text(400, 150, text="French", font=("Arial",40, 'italic'))
with open('/data/french_words.csv','r') as data_file:

canvas.create_text(400, 263, text="word", font=('Ariel', 60,'bold'))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image,highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image,highlightthickness=0, command=next_card)
known_button.grid(row=1, column=1)
# my_image = PhotoImage(file="images/card_back.png")

# button = Button(image=my_image, highlightthickness=0)



window.mainloop()