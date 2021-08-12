import tkinter

repetition = 0


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer = None


# TIMER RESET
def reset_timer():
    window.after_cancel(timer)
    global repetition
    repetition = 0
    title.config(text="Timer")
    canvas.itemconfig(clock, text="00:00")
    check_marks.config(text="")


# TIMER MECHANISM
def start_timer():
    global repetition
    repetition += 1
    work_min_sec = WORK_MIN * 60
    short_break_min_sec = SHORT_BREAK_MIN * 60
    long_break_min_sec = LONG_BREAK_MIN * 60
    if repetition % 2 == 1:
        title.config(text="Timer")
        count_down(work_min_sec)
    elif repetition % 8 == 0:
        title.config(text='Break')
        count_down(long_break_min_sec)
    else:
        title.config(text='Break')
        count_down(short_break_min_sec)


# COUNTDOWN MECHAMISM
def count_down(count):
    global repetition
    seconds = count % 60
    minutes = int((count - seconds) / 60)
    if seconds < 10:
        seconds = f"0{seconds}"
    if minutes < 10:
        minutes = f"0{minutes}"
    canvas.itemconfig(clock, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        for i in range(repetition//2):
            mark += "✔\n"
            check_marks.config(text=mark)


# UI SETUP

window = tkinter.Tk()
window.title("Timer")
window.config(padx=100, pady=100, bg=YELLOW)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_pic = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_pic)
clock = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


title = tkinter.Label(text="Timer")
title.config(font=(FONT_NAME, 45, "bold"), bg=YELLOW, fg=GREEN, anchor='center')
title.grid(row=0, column=1)

check_marks = tkinter.Label(text="")
check_marks.config(font=(FONT_NAME, 15, "bold"), bg=YELLOW, fg=GREEN, anchor='center')
check_marks.grid(row=3, column=1)

start_button = tkinter.Button(text="Start", command=start_timer)
start_button.config(anchor="e", highlightthickness=0)
start_button.grid(row=2, column=0)

reset_button = tkinter.Button(text="Reset", command=reset_timer)
reset_button.config(anchor="w", highlightthickness=0)
reset_button.grid(row=2, column=2)

window.mainloop()
