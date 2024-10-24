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
repeat=0
time_loop=None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global repeat
    canvas.itemconfig(timer_text,text="00:00")
    Label.config(title_label,text="TIMER",fg=GREEN)
    tkwindow.after_cancel(time_loop)
    repeat=0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
        
def display_starttime():
    global repeat
    repeat+=1
    # worktime_secs=WORK_MIN*60
    # short_breaksecs=SHORT_BREAK_MIN*60
    # long_breaksecs=LONG_BREAK_MIN*60    
    worktime_secs=10
    short_breaksecs=4
    long_breaksecs=8
  
    if  repeat%2!=0 and repeat<=7:
        print(f"work:{worktime_secs}") 
        Label.config(title_label,text="WORK",fg=GREEN)  
        countdown(worktime_secs)
        print(repeat)      
        
       
    if repeat%2==0 and repeat<7:
        print(repeat)
        Label.config(title_label,text="S_BREAK",fg=RED)  
        countdown(short_breaksecs)
        print(f"sb:{short_breaksecs}") 
        check_mark=Label(text="✅",fg=GREEN)
        check_mark.grid(column=repeat-1,row=3)
         
    if repeat==8:    
        print(f"longbrkrep={repeat}")
        print(f"llb:{long_breaksecs}")  
        # Label(text="S_BREAK",font=(FONT_NAME,'45','bold'),fg=PINK)
        Label.config(title_label,text="L_BREAK",fg=PINK)
        countdown(long_breaksecs)       
        
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def countdown(total_seconds):  
    global time_loop   
  
    if total_seconds>0:
        secs=total_seconds%60
        mins=total_seconds//60
        timer=f'{mins:02d}:{secs:02d}'
        # print(timer)
        canvas.itemconfig(timer_text,text=timer)
        time_loop=tkwindow.after(1000,countdown,total_seconds-1)
    if total_seconds==0:
        display_starttime()
           

        
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


start_button=Button(text="Start",bg=YELLOW,command=display_starttime)
reset_button=Button(text="Reset",bg=PINK,command=reset_timer)

start_button.grid(column=0,row=2)
reset_button.grid(column=2,row=2)


check_mark=Label(text="",fg=GREEN)
check_mark.grid(column=1,row=3)

tkwindow.mainloop()