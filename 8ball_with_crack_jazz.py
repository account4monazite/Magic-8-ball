from random import choice
import pyttsx3 as pot
import tkinter as kt
from os import getcwd
# print(getcwd())

advice=[("It is certain",'green'),("Reply hazy, try again",'yellow'),("Don’t count on it",'red'),("It is decidedly so",'green'),("Ask again later",'yellow'),("My reply is no",'red'),("Without a doubt",'green'),
        ("Better not tell you now",'yellow'),("My sources say no",'yellow'),("Yes definitely",'green'),("Cannot predict now",'yellow'),("Outlook not so good",'red')
        ,("You may rely on it",'green'),("Concentrate and ask again",'yellow'),("Very doubtful",'yellow'),("As I see it, yes",'green'),
("Most likely",'green'),("Outlook good",'green'),("Yes",'green'),("Signs point to yes",'green')		]

shaking=False

def shakey(callback):
    global shaking
    shaking=True
    def move(off, c):
        if c > 0:
            x_change = off if c % 2 == 0 else -off
            img_label.place(x=original_x + x_change, y=original_y)
            window.after(50, move, off, c - 1)
        else:
            img_label.place(x=original_x, y=original_y)  # Reset position
            callback()  # Call the callback function
            shaking=False
    move(10, 20)  # Shake for 20 cycles

def get_answer():
    if shaking:
        return
    q=u_input.get()
    if q.strip():
      def show_answer():
        answer,color=choice(advice)
        result.config(text=answer,fg=color)
        intro.say(answer)
        intro.runAndWait()
      shakey(show_answer)
    else:
        result.config(text='Please ask a question!')
        intro.say('Please ask a question!')
        intro.runAndWait()

def play_intro():
    intro.say("Welcome to the Magic 8 Ball! Ask away your doubts!")
    intro.runAndWait()

def center_img():
    if shaking:
        return original_x,original_y
    window.update_idletasks()
    width_w=window.winfo_width()
    height_w=window.winfo_height()
    width_i=img.width()
    height_i=img.height()
    x_center=(width_w-width_i)//2
    y_center=(height_w-height_i)//2
    img_label.place(x=x_center,y=y_center+100)
    return x_center,y_center+100

def on_resize(event):
    global original_x, original_y
    original_x, original_y = center_img()



intro=pot.init()

window=kt.Tk()
window.title('Magic 8 ball:Know the Future')
window.geometry('600x600')
label=kt.Label(master=window,text='8 ball',font=('Comic Sans MS', 24))
label.pack(pady=10)



img=kt.PhotoImage(file='c:/Users/shriy/OneDrive/Desktop/New folder/ok.gif')
img_label=kt.Label(window,image=img)
# label.place(x=250,y=250)
original_x,original_y=center_img()
img_label.place(x=original_x,y=original_y+100)


u_input=kt.Entry(window,font='ComicSans 16',width=40)
u_input.pack(pady=10)

submit=kt.Button(window,text='Ask the 8 ball',font=('Comic Sans MS',14, 'bold'),command=get_answer)
submit.pack(pady=10)
result=kt.Label(window,text='',font=('Comic Sans MS',16),justify='center')
result.pack(pady=20)
window.after(1000,play_intro)
window.bind("<Configure>", on_resize)
window.mainloop()

# x=input("Type here: ")
# answer=choice(advice)
# intro.say(answer)
# intro.runAndWait()
