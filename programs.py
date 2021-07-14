from tkinter import *
from tkinter import messagebox
import random
import time

dark=True
bgc="#525150"
wrdc="white"
spacec="#f0f0f0"
win=Tk()
win.title("pick-a-progr")
win.geometry("400x400")
win.configure(bg=bgc)
score=0
answers=0

def first_win():
    global txt,frame1,name,dark,bgc,wrdc,spacec,frame1_1
    frame1_1=Frame(win)
    frame1_1.pack(fill=Y)
    frame1_1.configure(bg=spacec)
    frame1= Frame(win)
    frame1.pack(fill=Y)
    frame1.configure(bg=bgc)

    titlelbl = Label(master=frame1_1, text="Pick-A-Progr",font=("Helvetica",25),bg=bgc,fg=wrdc)
    titlelbl.grid(column=0,row=1)
    lblhello=Label(master=frame1,text="Hello, what is your name?",font=("Helvetica",25),bg=bgc,fg=wrdc)
    lblhello.grid(column=0,row=3,pady=10)
    lblnm=Label(master=frame1,text="Hi, my name is",font=("Helvetica",25),bg=bgc,fg=wrdc)
    lblnm.grid(column=0,row=4)
    txt=Entry(master=frame1,width=20,font=("Helvetica",20,"bold"),justify=CENTER)
    txt.grid(column=0,row=5)
    btnxt = Button(master=frame1, font=("Helvetica", 25), text="Exit", width=11,bg=bgc,fg=wrdc, command=exit)
    btnxt.grid(column=0, row=6,pady=95)

    lbl_space1=Label(master=frame1_1,font=("Helvetica",10),bg=spacec,width=30)
    lbl_space1.grid(column=0,row=0)
    lbl_space2=Label(master=frame1_1,font=("Helvetica",10),bg=spacec,width=30)
    lbl_space2.grid(column=0,row=2)

    win.bind('<Return>', sec_win)
    name=""

def sec_win(*args):
    global txt,frame1,name,frame1_1,bgc,wrdc,spacec,score,answers
    if name=="":
        name=txt.get()
        frame1.destroy()
        frame1_1.destroy()
    if name=="":
        res=messagebox.showerror("Error", "You haven't entered a name!!!")
        first_win()
    else:
        global frame2,frame2_2
        win.geometry("400x450")
        opt_img=PhotoImage(file='img/options_gear.png')
        opt_img=opt_img.subsample(4)

        frame2=Frame(win)
        frame2.pack(fill=Y)
        frame2.configure(bg=spacec)
        frame2_2 = Frame(win)
        frame2_2.pack(fill=Y)
        frame2_2.configure(bg=bgc)

        titlelbl=Label(master=frame2,text="Pick-A-Progr",font=("Helvetica",25),bg=bgc,fg=wrdc)
        titlelbl.grid(column=0,row=1,columnspan=2)

        lblspace1=Label(master=frame2,font=("Helvetica",10),bg=spacec,width=30)
        lblspace1.grid(column=0,row=0,columnspan=2)
        lblspace1 = Label(master=frame2, font=("Helvetica", 10), bg=spacec, width=30)
        lblspace1.grid(column=0, row=2,columnspan=2)

        wellbl=Label(master=frame2_2,text="Welcome "+name+"!\nChoose a program!",font=("Helvetica",25),bg=bgc,fg=wrdc)
        wellbl.grid(column=0,row=3,columnspan=3)
        btngames=Button(master=frame2_2,font=("Helvetica",25),text="Games"
                        ,bg=bgc,fg=wrdc,width=11,command=games)
        btngames.grid(column=0,row=4,columnspan=3)
        btnqzes=Button(master=frame2_2,font=("Helvetica",25),text="Quizzes",width=11,bg=bgc,fg=wrdc,
                       command=unavailable)
        btnqzes.grid(column=0,row=5,columnspan=3,pady=15)

        btnxt = Button(master=frame2_2, font=("Helvetica",25), text="Exit", width=3,bg=bgc,fg=wrdc, command=exit)
        btnxt.grid(column=0,row=6)
        lblscore=Label(master=frame2_2,font=("Helvetica",25),fg=wrdc,bg=bgc,text=str(score)+"/"+str(answers))
        lblscore.grid(column=1,row=6)
        btnopt=Button(master=frame2_2,font=("Helvetica",25),bg=bgc,image=opt_img,command=options)
        btnopt.image=opt_img
        btnopt.grid(column=2,row=6)
def unavailable():
    res = messagebox.showerror("Error","Not available yet!!!")
def chgnm():
    global frame3,frame3_2
    frame3.destroy()
    frame3_2.destroy()
    first_win()
def options():
    global txt,frame2,frame2_2,bgc,wrdc,spacec,frame3,frame3_2,dark
    frame2_2.destroy()
    frame2.destroy()

    frame3 = Frame(win)
    frame3.pack(fill=Y)
    frame3.configure(bg=spacec)
    frame3_2 = Frame(win)
    frame3_2.pack(fill=Y)
    frame3_2.configure(bg=bgc)

    lbl_space1=Label(master=frame3,font=("Helvetica",10),bg=spacec,width=20)
    lbl_space1.grid(column=0,row=0)
    lbl_space2=Label(master=frame3,font=("Helvetica",10),bg=spacec,width=20)
    lbl_space2.grid(column=0,row=2)

    lbl_title=Label(master=frame3,font=("Helvetica",25),bg=bgc,fg=wrdc,text="Options")
    lbl_title.grid(column=0,row=1)

    btnchn = Button(master=frame3_2, font=("Helvetica", 25), text="Change Name", width=11, bg=bgc, fg=wrdc,command=chgnm)
    btnchn.grid(column=0, row=3,pady=10)
    btnthm=Button(master=frame3_2,font=("Helvetica", 25),text="Theme:LIGHT", width=11,bg=bgc,fg=wrdc,command=change_theme)
    btnthm.grid(column=0,row=4,pady=5)
    if dark==False:
        btnthm.configure(text="Theme:DARK")
    btnbck=Button(master=frame3_2,font=("Helvetica",25),text="Back", width=6,bg=bgc,fg=wrdc,command=back_tt)
    btnbck.grid(column=0,row=5,pady=120)

def back_tt():
    global frame3,frame3_2
    frame3_2.destroy()
    frame3.destroy()
    sec_win()

def change_theme():
    global dark,bgc,wrdc,spacec,frame3,frame3_2
    if dark==True:
        bgc="#e0e0e0"
        wrdc="black"
        spacec="#ecffe8"
        dark=False
    else:
        bgc="#525150"
        wrdc="white"
        spacec="#f0f0f0"
        dark=True
    win.configure(bg=bgc)
    frame3.destroy()
    frame3_2.destroy()
    options()

def games():
    global dark,bgc,wrdc,spacec,frame2,frame2_2,frame3,frame3_2
    frame2.destroy()
    frame2_2.destroy()

    win.geometry("400x400")

    frame3 = Frame(win)
    frame3.pack(fill=Y)
    frame3.configure(bg=spacec)
    frame3_2=Frame(win)
    frame3_2.pack(fill=Y)
    frame3_2.configure(bg=bgc)

    lbl_title=Label(master=frame3,font=("Helvetica",25),text="Games",bg=bgc,fg=wrdc)
    lbl_title.grid(column=0,row=1)
    lbl_space=Label(master=frame3,font=("Helvetica",10),bg=spacec,width=20)
    lbl_space.grid(column=0,row=0)
    lbl_space = Label(master=frame3,font=("Helvetica", 10),bg=spacec,width=20)
    lbl_space.grid(column=0,row=2)

    btn_color_game=Button(master=frame3_2,font=("Helvetica",25)
                           ,text="Color Game",bg=bgc,fg=wrdc,command=lambda:colour_game(400,400),width=14)
    btn_color_game.grid(column=0,row=0,pady=20)
    btn_guess_the_num=Button(master=frame3_2,font=("Helvetica",25)
                             ,text="Gues the number",bg=bgc,fg=wrdc,command=Guess_the_number)
    btn_guess_the_num.grid(column=0,row=1)
    btn_back=Button(master=frame3_2,font=("Helvetica",25)
                             ,text="Back",bg=bgc,fg=wrdc,command=back_tt,width=14)
    btn_back.grid(column=0,row=2,pady=20)
def colour_game(x,y):
    global win, cg_score, clgframe1,frame3,frame3_2,bgc,wrdc,spacec,score,answers
    win.title("Colour Game")
    global colours
    frame3.destroy()
    frame3_2.destroy()
    def set():
        global time, text, cg_score, clgframe2, c,clgframe1
        time = 30
        clgframe2=Frame(win)
        clgframe2.pack(fill=Y)
        clgframe2.configure(bg=spacec)
        clgframe1 = Frame(win)
        clgframe1.pack(fill=Y)
        clgframe1.configure(bg=bgc)
        text=""
        cg_score=0
        c=0

    colours = ['Red', 'Blue', 'Green', 'Brown', 'Black', 'Cyan', 'Pink', 'Purple', 'Crimson', 'White']

    def MainGame(event):
        global c,cg_score,wrdc
        scorelbl.configure(text="Your score  " + str(cg_score)+"/"+str(c),fg=wrdc)
        if time == 30:
            nextsec()
        next_clr()

    def nextsec():
        global time, word
        if time > 0:
            time-=1
            timelbl.config(text="Time=" + str(time) + "sec.")
            timelbl.after(1000,nextsec)

    def next_clr():
        global time, text, cg_score, colours, txt, word, clgframe1,c,score,answers,wrdc
        if time != 0:
            if txt.get().lower() == colours[1].lower():
                cg_score += 1
            txt.delete(0, END)
            random.shuffle(colours)
            word.config(fg=str(colours[1]), text=str(colours[0]))
            scorelbl.configure(text="Your score  " + str(cg_score)+"/"+str(c))
            c+=1
        else:
            word.config(fg=wrdc, text="Your score is " + str(cg_score)+"/"+str(c), font=("Helvetica", 30))
            txt.delete(0, END)
            txt.configure(state="disabled")
            score+=cg_score
            answers+=c

    def firstwin():
        global scorelbl, timelbl, txt, word,bgc,wrdc,spacec,clgframe1,clgframe2
        title = Label(master=clgframe2, text="Type in the colour of the \nword and not the text!"
                      ,font=("Helvetica",25),fg=wrdc,bg=bgc)
        title.grid(column=0, row=1)
        scorelbl=Label(master=clgframe1,text="Press enter to start",font=("Helvetica",20),bg=bgc,fg=wrdc)
        scorelbl.grid(column=0, row=1, columnspan=2)
        timelbl = Label(master=clgframe1, text="Time=" + str(time) + "sec.", font=("Helvetica", 20),bg=bgc,fg=wrdc)
        timelbl.grid(column=0, row=2, columnspan=2)
        word = Label(master=clgframe1, text="", font=("Helvetica", 60),bg=bgc)
        word.grid(column=0, row=3, columnspan=2)
        txt = Entry(master=clgframe1, text=text, width=20, justify=CENTER,font=("Helvetica", 20),bg=bgc,fg=wrdc)
        txt.grid(column=0, row=4, columnspan=2)
        win.bind('<Return>', MainGame)
        reset = Button(master=clgframe1, text="Reset",font=("Helvetica", 15), height=2, width=10, command=restart,bg=bgc,fg=wrdc)
        reset.grid(column=0, row=5)
        bckbtn=Button(master=clgframe1,text="Back",font=("Helvetica",15),height=2,width=10,command=back,bg=bgc,fg=wrdc)
        bckbtn.grid(column=1,row=5)

        lblspace1=Label(master=clgframe2,text="",font=("Helvetica",10),bg=spacec,width=50)
        lblspace1.grid(column=0,row=0)
        lblspace2=Label(master=clgframe2,text="",font=("Helvetica",10),bg=spacec,width=50)
        lblspace2.grid(column=0,row=2)
    def restart():
        global time, clgframe1,clgframe2
        time = 0
        clgframe1.destroy()
        clgframe2.destroy()
        set()
        firstwin()
    def back():
        clgframe1.destroy()
        clgframe2.destroy()
        games()
    set()
    firstwin()


def Guess_the_number():
    global frame3,frame3_2,bgc,wrdc,spacec,score,answers
    win.title("Gues the number")
    win.geometry("650x620")
    frame3.destroy()
    frame3_2.destroy()


    def start():
        global num, btn_rsrt, txtguess, lbl_up, lbl_dwn, lbl_crect, lbl_instr, row_dn_f, row_up_f, chk_f, lbl_rdm_num_seq,c
        c=0
        btn_rsrt.configure(text="Restart")
        txtguess.delete(0, END)
        for i in range(0, 15):
            a = random.randint(0, 100)
            lbl_rdm_num_seq.configure(text=a)
            lbl_rdm_num_seq.update()
            time.sleep(0.1)

        lbl_rdm_num_seq.configure(text="?")
        num = random.randint(0, 100)
        win.bind('<Return>', check)
        txtguess.delete(1, END)
        txtguess.configure(state='normal')

        lbl_crect.configure(image=chk_f)
        lbl_crect.image = chk_f
        lbl_dwn.configure(image=row_dn_f)
        lbl_dwn.image = row_dn_f
        lbl_up.configure(image=row_up_f)
        lbl_up.image = row_dn_f
        lbl_instr.configure(text="I have thought of a number from 0 to 100.\n"
                                 "Enter your guess at the box bleow.\n"
                                 "Then, press enter to proceed", font=("Helvetica", 20))

    def check(*args):
        global num, txtguess, lbl_up, lbl_dwn, lbl_crect, row_dn_f, row_up_f, c ,lbl_rdm_num_seq,wrdc,score,answers


        row_up_n = PhotoImage(file='img/arrow_up_on.png')
        row_up_n = row_up_n.subsample(3)
        row_dn_n = PhotoImage(file='img/arrow_down_on.png')
        row_dn_n = row_dn_n.subsample(3)
        chk_n = PhotoImage(file='img/check_on.png')
        chk_n = chk_n.subsample(4)

        if int(txtguess.get()) == num:
            c+=1
            lbl_crect.configure(image=chk_n)
            lbl_crect.image = chk_n
            lbl_dwn.configure(image=row_dn_f)
            lbl_dwn.image = row_dn_f
            lbl_up.configure(image=row_up_f)
            lbl_up.image = row_up_f
            txtguess.configure(state="disabled")
            lbl_rdm_num_seq.configure(fg=wrdc,text=str(c)+" tries")
            score+=1
            answers+=c

        elif int(txtguess.get()) > num:
            c+=1
            lbl_dwn.configure(image=row_dn_n)
            lbl_dwn.image = row_dn_n
            lbl_up.configure(image=row_up_f)
            lbl_up.image = row_up_f
            lbl_dwn.after(700, reset_colour)
            txtguess.delete(0, END)


        elif int(txtguess.get()) < num:
            c+=1
            lbl_up.configure(image=row_up_n)
            lbl_up.image = row_up_n
            lbl_dwn.configure(image=row_dn_f)
            lbl_dwn.image = row_dn_f
            lbl_dwn.after(700, reset_colour)
            txtguess.delete(0, END)
        win.bind('<Return>', check)

    def reset_colour():
        global lbl_up, lbl_dwn, row_dn_f, row_up_f
        lbl_up.configure(image=row_up_f)
        lbl_up.image = row_up_f
        lbl_dwn.configure(image=row_dn_f)
        lbl_dwn.image = row_dn_f

    def firstwin():
        global txtguess,lbl_up,lbl_dwn,lbl_crect,btn_rsrt,lbl_instr,row_dn_f,row_up_f,chk_f\
            ,lbl_rdm_num_seq,bgc,wrdc,spacec,framelbl,frameguess,framebtn

        row_dn_f = PhotoImage(file="img/arrow_down_off.png")
        row_dn_f = row_dn_f.subsample(3)
        row_up_f = PhotoImage(file="img/arrow_up_off.png")
        row_up_f = row_up_f.subsample(3)
        chk_f = PhotoImage(file="img/check_off.png")
        chk_f = chk_f.subsample(4)

        framelbl = Frame(win,bg=spacec)
        framelbl.pack(fill=Y)
        frameguess = Frame(win, bg=bgc)
        frameguess.pack(fill=Y)
        framebtn = Frame(win, bg=bgc)
        framebtn.pack(fill=Y)

        lbl_space = Label(master=framelbl, text="", bg=spacec, font=("Helvetica", 20), width=20)
        lbl_space.grid(column=0, row=1)
        lbl_space2 = Label(master=framelbl, text="", bg=spacec, font=("Helvetica", 20), width=20)
        lbl_space2.grid(column=1, row=1)
        lbl_space3 = Label(master=framelbl, text="", bg=spacec, font=("Helvetica", 20), width=20)
        lbl_space3.grid(column=0, row=3)
        lbl_space4 = Label(master=framelbl, text="", bg=spacec, font=("Helvetica", 20), width=20)
        lbl_space4.grid(column=1, row=3)
        lbl_instr = Label(master=framelbl, text="Press Start to begin", font=("Helvetica", 50), fg=wrdc,bg=bgc)
        lbl_instr.grid(column=0, row=2, columnspan=2)

        lbl_up = Label(master=frameguess, image=row_up_f, bg=bgc)
        lbl_up.image = row_up_f
        lbl_up.grid(column=0, row=0, columnspan=3)
        lbl_dwn = Label(master=frameguess, image=row_dn_f, bg=bgc)
        lbl_dwn.image = row_dn_f
        lbl_dwn.grid(column=0, row=2, columnspan=3)
        lbl_rdm_num_seq = Label(master=frameguess, font=('Helvetica', 15), bg=bgc, fg="#ff6110", text="",
                                width=18)
        lbl_rdm_num_seq.grid(column=0, row=1)
        txtguess = Entry(master=frameguess, width=15, font=("Helvetica", 15), bd=5, bg=bgc, fg=wrdc,
                         justify=CENTER, text="", state="disabled")
        txtguess.grid(column=1, row=1)
        lbl_crect = Label(master=frameguess, image=chk_f, bg=bgc)
        lbl_crect.image = chk_f
        lbl_crect.grid(column=2, row=1, padx=30)

        btn_exit = Button(master=framebtn, text="Exit", font=("Helvetica", 15), bg=bgc, fg=wrdc, width=15,
                          height=2, command=exit)
        btn_exit.grid(column=2, row=0, padx=20)
        btn_bck=Button(master=framebtn,text="Back",font=("Helvetica",15),bg=bgc,fg=wrdc,width=15,
                          height=2,command=back)
        btn_bck.grid(column=1,row=0,padx=20)
        btn_rsrt = Button(master=framebtn, text="Start", font=("Helvetica", 15), bg=bgc, fg=wrdc, width=15,
                          height=2, command=start)
        btn_rsrt.grid(column=0, row=0, padx=20)
    def back():
        framelbl.destroy()
        frameguess.destroy()
        framebtn.destroy()
        games()
    firstwin()

first_win()
win.mainloop()