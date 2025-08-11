# --- Import Libraries ---
from tkinter import *      # GUI creation
from tkinter import messagebox
import pandas as pd        # Reading CSV data
from random import choice  # Selecting random entries

# --- Global Constants & Variables ---
BACKGROUND_COLOR = "#B1DDC6"
q_language = q_word = a_language = a_word = None
flip_timer = None  # Stores reference to the card flip timer
random_row = None
wrong_words = []

# Session complete flag
session_over = False

# --- Load Word Data ---
data = None
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")
finally:
    data_list = data.to_dict(orient="records")      #Stored fetched data

def right_answer():
    global session_over
    if session_over:
        return

    data_list.remove(random_row)    # type: ignore
    check_end_session()
    # If not finished, go to next card
    next_card()

def wrong_answer():
    global session_over
    if session_over:
        return

    data_list.remove(random_row)    # type: ignore
    wrong_words.append(random_row)
    check_end_session()
    # If not finished, go to next card
    next_card()

def check_end_session():
    global session_over
    if len(data_list) == 0 and not session_over:
        session_over = True  # Mark that session is finished

        # Save remaining words to file
        df = pd.DataFrame(wrong_words)
        df.to_csv("data/words_to_learn.csv", index=False)

        # Show popup message
        messagebox.showinfo(
            title="Session Complete",
            message=(
                "Great job! 🎉\n"
                "You’ve completed today’s flashcards.\n\n"
                "We’ve saved the words you still need to practice in:\n"
                "'words_to_learn.csv'\n\n"
                "Open that file to review the ones you haven’t mastered yet.\n"
                "Keep practicing and you’ll get them all! 💪"
            )
        )
        # Close the app
        window.destroy()
        return True
    return False

# --- Function: Show a New Flashcard ---
def next_card():
    """Display a random word pair and start the flip timer."""
    global q_language, q_word, a_language, a_word, flip_timer

    if not data_list:
        check_end_session()
        return

    # Disable buttons until flip
    right_btn.config(state=DISABLED)
    wrong_btn.config(state=DISABLED)

    # Cancel any ongoing flip timer before starting a new one
    if flip_timer:
        window.after_cancel(flip_timer)

    # Pick a random word pair from the data
    global random_row
    random_row = choice(data_list)
    q_language, a_language = random_row.keys()
    q_word, a_word = random_row.values()

    # Update the card front with question language & word
    canvas.itemconfig(canvas_img, image=card_front)
    canvas.itemconfig(language_name, text=q_language, fill="black")
    canvas.itemconfig(word, text=q_word, fill="black")

    # Schedule the flip after 3 seconds
    flip_timer = window.after(3000, flip_card)

# --- Function: Flip the Flashcard ---
def flip_card():
    """Flip the card to show the answer."""
    canvas.itemconfig(canvas_img, image=card_back)
    canvas.itemconfig(language_name, text=a_language, fill="white")
    canvas.itemconfig(word, text=a_word, fill="white")

    # Enable buttons after flip
    right_btn.config(state=NORMAL)
    wrong_btn.config(state=NORMAL)

# --- GUI Setup ---
window = Tk()
window.title("Flash-Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# --- Load Images ---
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
wrong_img = PhotoImage(file="images/wrong.png")
right_img = PhotoImage(file="images/right.png")

# --- Canvas for Card Display ---
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas_img = canvas.create_image(400, 263)
language_name = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# --- Buttons ---
wrong_btn = Button(image=wrong_img, highlightthickness=0, command=wrong_answer)
wrong_btn.grid(row=1, column=0)

right_btn = Button(image=right_img, highlightthickness=0, command=right_answer)
right_btn.grid(row=1, column=1)

# --- Start App ---
next_card()  # Show first card immediately
window.mainloop()
