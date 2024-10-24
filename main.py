# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK="&#x2705"
import time
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    canvas.itemconfig(timer_text,text="00:00")
    countdown(0)
# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def countdown(total_seconds):
    # while total_seconds:       
    if total_seconds>0:
        secs=total_seconds%60
        mins=total_seconds//60
        timer=f'{mins:02d}:{secs:02d}'
        print(timer)
    # time.sleep(1)    
    # total_seconds-=1
        canvas.itemconfig(timer_text,text=timer)
        tkwindow.after(1000,countdown,total_seconds-1)

def display_time():
    total_seconds=2*60
    countdown(total_seconds)

# ---------------------------- UI SETUP ------------------------------- #







from tkinter import *

tkwindow=Tk()
tkwindow.title("Pomodoro timer")
tkwindow.config(padx=100,pady=50)

title_label=Label(text="Timer",font=(FONT_NAME,'45','bold'),fg=GREEN)
title_label.grid(column=1,row=0)

canvas=Canvas(width=300,height=300)
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(140,140,image=tomato_img)
timer_text=canvas.create_text(145,170,text="00:00",font=('Helvetica','30','bold'),fill="white")
canvas.grid(column=1,row=1)


start_button=Button(text="Start",bg=YELLOW,command=display_time)
reset_button=Button(text="Reset",bg=PINK,command=reset_timer)

start_button.grid(column=0,row=2)
reset_button.grid(column=2,row=2)


check_mark=Label(text="✅",fg=GREEN)
check_mark.grid(column=1,row=3)

tkwindow.mainloop()