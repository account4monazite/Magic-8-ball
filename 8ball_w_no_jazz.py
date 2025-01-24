from random import choice
import pyttsx3 as pot
import tkinter as kt
from os import getcwd
# print(getcwd())

advice=["It is certain","Reply hazy, try again","Don’t count on it","It is decidedly so","Ask again later","My reply is no","Without a doubt","Better not tell you now","My sources say no",
"Yes definitely","Cannot predict now",	"Outlook not so good","You may rely on it",	"Concentrate and ask again"	"Very doubtful","As I see it, yes",
"Most likely","Outlook good","Yes","Signs point to yes"		]

def get_answer():
    q=u_input.get()
    if q.strip():
        answer=choice(advice)
        result.config(text=answer)
        intro.say(answer)
        intro.runAndWait()
    else:
        result.config(text='Please ask a question!')
        intro.say('Please ask a question!')
        intro.runAndWait()

def play_intro():
    intro.say("Welcome to the Magic 8 Ball! Ask away your doubts!")
    intro.runAndWait()

intro=pot.init()

window=kt.Tk()
window.title('Magic 8 ball:Know the Future')
window.geometry('600x600')
label=kt.Label(master=window,text='8 ball',font=('Comic Sans MS', 24))
label.pack(pady=10)

img=kt.PhotoImage(file='c:/Users/shriy/OneDrive/Desktop/New folder/ok.gif')
img_label=kt.Label(window,image=img)
img_label.pack(pady=10)

u_input=kt.Entry(window,font='ComicSans 16',width=40)
u_input.pack(pady=10)

submit=kt.Button(window,text='Ask the 8 ball',font=('Comic Sans MS',14, 'bold'),command=get_answer)
submit.pack(pady=10)
result=kt.Label(window,text='',font=('Comic Sans MS',16),justify='center')
result.pack(pady=20)
window.after(1000,play_intro)
window.mainloop()

# x=input("Type here: ")
# answer=choice(advice)
# intro.say(answer)
# intro.runAndWait()
