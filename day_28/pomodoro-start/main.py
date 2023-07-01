from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    count_down(1 * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    # print(count)
    canvas.itemconfig(timer_text, text=f"0{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
# window.minsize(width=300, height=300)
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=280, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="./day_28/pomodoro-start/tomato.png")
canvas.create_image(120, 112, image=tomato_img)
timer_text = canvas.create_text(
    130, 130, text="00:00", fill="white", font=(FONT_NAME, 32, "bold")
)
canvas.grid(row=1, column=1)


# timer text
timer_label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)

# start button
start_btn = Button(text="Start", command=start_timer, highlightthickness=0)
start_btn.grid(row=2, column=0)

# reset button
reset_btn = Button(text="Reset", highlightthickness=0)
reset_btn.grid(row=2, column=2)

# check mark
checkmark = Label(text="✔️", fg=GREEN, bg=YELLOW)
checkmark.grid(row=3, column=1)

window.mainloop()
