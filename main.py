from tkinter import *
import math
import time

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global timer
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="TIMER")
    reps = 0
    check_marks.config(text="")
    start_button.config(state=NORMAL)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def startTimer():
    global reps
    reps += 1
    start_button.config(state=DISABLED)
    if reps % 8 == 0:
        title_label.config(text="LONG BREAK", fg=RED)
        countdown(LONG_BREAK_MIN * 60)
    elif reps % 2 == 1:
        title_label.config(text="WORK", fg=GREEN)
        countdown(WORK_MIN * 60)
    elif reps % 2 == 0:
        title_label.config(text="BREAK", fg=PINK)
        countdown(SHORT_BREAK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"
    # elif count_sec == 0:

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        startTimer()
        marks = ""
        session_count = math.floor(reps / 2)
        for _ in range(session_count):
            marks += "✅"
        check_marks.config(text=marks)


#---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")

window.config(padx=100, pady=50, bg=YELLOW)
title_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50), bg=YELLOW)
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

# canvas.pack()
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=startTimer)

start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset)
reset_button.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)
window.mainloop()
