#python number guessing game with tkiner GUI
#needed modules
import random
from sys import builtin_module_names
from PIL import ImageTk
import time
from tkinter import *
from tkinter import font
from tkinter.font import BOLD, ITALIC



#this function starts the game
def yes_start_game(top):
    #toplevel creates a child widow to top
    new_window=Toplevel(top)
    new_window.configure(bg="#C1C6C0")

    #creating labels and entry's
    l1=Label(new_window,text="Guess a Number from 1 to 10",bg="#C1C6C0",font=("Comic Sans MS",20))
    l2=Label(new_window,text="*********************************************************",bg="#C1C6C0",font=("Comic Sans MS",20))

    #single row different columns
    l3=Label(new_window,text="No of Attemps:",bg="#C1C6C0",font=("Comic Sans MS",20))
    l4=Entry(new_window,textvariable=no_of_attemps,width=3,font=("Comic Sans MS",20),bg="#C1C6C0")
    l9=Label(new_window,text="Lowest Attempts:",bg="#C1C6C0",font=("Comic Sans MS",20))
    l5=Entry(new_window,textvariable=high_score,bg="#C1C6C0",font=("Comic Sans MS",20),width=3)

    l6=Label(new_window,text="*********************************************************",bg="#C1C6C0",font=("Comic Sans MS",20))
    l7=Label(new_window,textvariable=game_logs,bg="#C1C6C0",font=("Comic Sans MS",20))
    l8=Label(new_window,text="*********************************************************",bg="#C1C6C0",font=("Comic Sans MS",20))
    
    #same rows different columns
    l11=Label(new_window,text="Guess here:",bg="#C1C6C0",font=("Comic Sans MS",20))
    e=Entry(new_window,textvariable=enter_numbered,width=3,font=("Comic Sans MS",20),justify=CENTER,bg="#C1C6C0")
    
    #same rows
    #quit destroys 
    quit_btn=Button(new_window,command=new_window.destroy,text="Exit->",bg="#C1C6C0",font=("Comic Sans MS",16),width=10)
    #restart btn sets all the intvars,stringvars to initial state and attempts to 0
    rest_btn=Button(new_window,command=restart_action,text="Restart",font=("Comic Sans MS",16),width=10,bg="#C1C6C0")
    #try calls the try action which uses linear search approach for guessing numbers
    try_btn=Button(new_window,text="TRY",command=try_action,font=("Comic Sans MS",16),width=10,bg="#C1C6C0")

    #binding all labels,buttons entry using grid method this time
    l1.grid(row=0,column=0,columnspan=7)
    l2.grid(row=1,column=0,columnspan=7)
    
    l3.grid(row=2,column=0,columnspan=1)
    l4.grid(row=2,column=1,columnspan=1)
    l9.grid(row=2,column=3,columnspan=3)
    l5.grid(row=2,column=6,columnspan=2)
    
    l6.grid(row=3,column=0,columnspan=7)
    l7.grid(row=4,column=0,columnspan=7)
    l8.grid(row=7,column=0,columnspan=7)
    
    l11.grid(row=11,column=1)
    e.grid(row=11,column=2,pady=8,padx=20)
    
    try_btn.grid(row=12,column=2)
    quit_btn.grid(row=12,column=4)
    rest_btn.grid(row=12,column=6)

    #mainlooping all the widgets
    new_window.mainloop()
    

#restart function resetting everything 
def restart_action():
    attemps=0
    no_of_attemps.set(0)
    game_logs.set("")
    enter_numbered.set("")
    secret_number=random.randint(1,10)


#trying numbers
def try_action():

    #making these variables globals as these will be modified in the function acc to the scenario
    global attemps
    global secret_number
    global lowest_attempt

    #if user gives number in 1 to 10 the program preceeds otherwise attemps inc by 1 
    if(int(enter_numbered.get())<=10 and int(enter_numbered.get())>0):

        #linear search if num>secret_num
        if(int(enter_numbered.get())>secret_number):
            game_logs.set("You guessed high!Guess a lower Number")
            #resetting the entry to "" preparing for next guess
            enter_numbered.set("")
            attemps+=1
            #setting number of attemps
            no_of_attemps.set(attemps)
        elif(int(enter_numbered.get())<secret_number):
            game_logs.set("You guessed low!Guess a higher Number")
            attemps+=1
            no_of_attemps.set(attemps)
            enter_numbered.set("")
        else:
            #when the user guesses the number right
            game_logs.set("Congratulations!You won")
            if(attemps==0):
                attemps+=1
            #we keep track of lowest attemsp from file handling so we update if someoned clears the guess in less than the current
            if(attemps<lowest_attempt):
                lowest_attempt=attemps
                #we update the new high score on the file
                fi=open("high_score.txt","w")
                fi.write("{}".format(attemps))
                high_score.set(lowest_attempt)
                game_logs.set("Congratulations!You won\nNew High score!")
                no_of_attemps.set(attemps)
                attemps=0
    else:
        game_logs.set("Number should be between 1 and 10!")
        enter_numbered.set("")
        attemps+=1
        no_of_attemps.set(attemps)

if __name__=="__main__":
    #main page
    #create a tkinter window
    top=Tk()
    attemps=0
    #configure all the coming entry's and labels textvariable
    no_of_attemps=IntVar()
    enter_numbered=StringVar()
    game_logs=StringVar()
    game_logs.set("Game Logs!")

    #generate random number from random module
    secret_number=random.randint(1,10)

    #store highscore on a file as it may lost storing it in a variable
    fi=open("high_score.txt",'r')
    lowest_attempt=int(fi.read())
    high_score=IntVar()
    high_score.set(lowest_attempt)

    #configuring top window
    top.maxsize()
    top.wm_state("zoomed")
    top.geometry("500x500")
    top.title("Number Guessing Game")

    #building canvas which i will be using to draw an image on
    c=Canvas(top,background="#000000",height=500,width=500)
    c.pack(expand=YES,fill=BOTH)
    #making photoimage of our file
    img=PhotoImage(file="icon2.png")
    l1=Label(c,image=img)
    l1.pack(pady=30)
    #adding label explaining rules
    l=Label(c,anchor=W,justify=CENTER,width=90,text="\n In the game you will have to guess a Secret number.\nAt each step you will be given a hint whether the number you are guessing is greater or smaller then your guessed number.\nThe game ends when you guess the number right.GoodLuck!\nThe limit of the numbers is between 1 to 10\n",fg="#00F5FF",bg="#000000",font=("Comic Sans MS",20))
    l.pack()

    #configuring buttons for starting and quitting the game

    #yes_start_game starts the game taking the window which is toplevel
    op1=Button(c,text="Start Game->",command=lambda:yes_start_game(top),relief=GROOVE,bg="#000000",fg="#ffffff",borderwidth=2,activebackground="#7FFF6D",activeforeground="#000000",font=("Comic Sans MS",15))

    #quit option destroys the window
    op2=Button(c,text="Quit Game->",command=top.destroy,relief=GROOVE,bg="#000000",fg="#ffffff",borderwidth=2,activebackground="#7FFF6D",activeforeground="#000000",font=("Comic Sans MS",15))
    op1.pack(pady=10)
    op2.pack(padx=10)

    #mainlooping the top window
    top.mainloop()


