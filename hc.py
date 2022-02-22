from atexit import register
from cgitb import text
from tkinter import *
from turtle import color
import random
hand = Tk()
hand.geometry("500x500")
t1=[]
t2=[]
runs=wickets=target=0
innings=1    

global one
global two
global three
global four
global five
global six

one=Button(hand,text="1",padx=15,pady=15,fg='red',command=lambda:score(1))
two=Button(hand,text="2",padx=15,pady=15,fg='red',command=lambda:score(2))
three=Button(hand,text="3",padx=15,pady=15,fg='red',command=lambda:score(3))
four=Button(hand,text="4",padx=15,pady=15,fg='blue',command=lambda:score(4))
five=Button(hand,text="5",padx=15,pady=15,fg='blue',command=lambda:score(5))
six=Button(hand,text="6",padx=15,pady=15,fg='blue',command=lambda:score(6))



        



def score(x):
    global runs 
    global wickets
    global target
    global innings
    ai=random.randint(1,6)
    if(x==ai):
        wickets+=1
    else:
        if(innings==2):
            target-=x
            runs+=x
        else:
            runs+=x
 

    Wick=Label(hand,text="Wickets: "+str(wickets))
    Runs=Label(hand,text="Runs: "+str(runs))
    Runs.grid(row=3,column=1,sticky="nsew")
    Wick.grid(row=4,column=1,sticky="nsew")
    AI=Label(hand,text="AI chose "+str(ai))
    AI.grid(row=2,column=1,sticky="nsew")
    if((wickets==10)and(innings==1)):
        target=runs+1
        innings+=1 
        In1=Label(hand,text=" needs "+str(runs)+" to win")
        t1.extend([runs,wickets])
        runs=wickets=0
        In1.grid(row=6,column=0,sticky="nsew")
    if((innings==2)and(target>=0)and(wickets>=0)):
        In2=Label(hand,text="Need "+str(target)+" from "+str(10-wickets))
        In2.grid(row=7,column=0,sticky="nsew")
    if((target<=0)or(wickets==10)):
        if(innings==2):
            one.config(state=DISABLED) 
            two.config(state=DISABLED)
            three.config(state=DISABLED)
            four.config(state=DISABLED)
            five.config(state=DISABLED)
            six.config(state=DISABLED)
    if((target<=0)and(innings==2)):
        t2.extend([runs,wickets])
        MS=Label(hand,text=str(t1[0])+'/'+str(t1[1])+'\n'+str(t2[0])+'/'+str(t2[1])+"Team B wins by "+str(10-t2[1])+" wickets")
        MS.grid(row=10,column=0,sticky="nsew")   
    elif((wickets==10)and(innings==2)):
        MS1=Label(hand,text=str(t1[0])+'/'+str(t1[1])+'\n'+str(t2[0])+'/'+str(t2[1])+"Team A wins by "+str(target)+" runs")
        MS1.grid(row=10,column=0,sticky="nsew")

one.grid(row=0,column=0,sticky="nsew")
two.grid(row=0,column=1,sticky="nsew")
three.grid(row=0,column=2,sticky="nsew")
four.grid(row=1,column=0,sticky="nsew")
five.grid(row=1,column=1,sticky="nsew")
six.grid(row=1,column=2,sticky="nsew")

Grid.rowconfigure(hand,[0,1,2,3,4,5,6,7,8,9,10],weight=1)
Grid.columnconfigure(hand,[0,1,2],weight=1)

one.config(font=("Cooper Black",10))
two.config(font=("Cooper Black",10))
three.config(font=("Cooper Black",10))
four.config(font=("Cooper Black",10))
five.config(font=("Cooper Black",10))
six.config(font=("Cooper Black",10))

def resize(e):
    size=e.width / 10
    one.config(font=("Cooper Black",int(size)))
    two.config(font=("Cooper Black",int(size)))
    three.config(font=("Cooper Black",int(size)))
    four.config(font=("Cooper Black",int(size)))
    five.config(font=("Cooper Black",int(size)))
    six.config(font=("Cooper Black",int(size)))



hand.bind('<Configure>',resize)

hand.mainloop()