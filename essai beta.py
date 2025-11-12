import turtle,random,os
from playsound import playsound
from time import sleep
import threading

#path to resources maker
dirname = os.path.dirname(os.path.abspath("__file__"))
redirect = os.path.join(dirname,'Resources\\')
os.chdir(redirect)
check="False"

def nothing():
    print("enter hit")
    turtle.bye()

#window
def pineapplepen():
    global pen,ch,run,block,blocka,blockb,s,speed_ch,speed_run
    wn=turtle.Screen()
    wn.setup(width = 1.0, height = 1.0)                         #for full screem
    canvas = wn.getcanvas()                                     #gets canvas
    root = canvas.winfo_toplevel()                              #gets title bar to root var
    root.overrideredirect(1)                                    #removes the minimize,close and other title bar components
    wn.title("The Chase: 2Players")
    wn.bgpic("main_bg.gif")
    wn.addshape("runner2.gif")
    wn.addshape("BOMB.gif")
    wn.addshape("ch_left.gif")
    wn.addshape("ch_right.gif")
    wn.addshape("runner2_right.gif")
    wn.addshape("plasma_left.gif")
    wn.addshape("ink.gif")
    wn.tracer(0)
    s=30
    speed_ch=0.5
    speed_run=0.7

#pen
    pen=turtle.Turtle()
    pen.speed(0)
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(-100, 0)

#chaser
    ch=turtle.Turtle()
    ch.speed(0)
    ch.shape("ch_right.gif")
    ch.penup()
    ch.shapesize(stretch_wid=2, stretch_len=2)
    ch.goto(-posx, 0)
    global q,ch_x,ch_y
    q=30
    ch_x=0.3
    ch_y=0


#runner
    run=turtle.Turtle()
    run.speed(0)
    run.shape("runner2.gif")
    run.penup()
    run.goto(posx, 0)
    global run_x,run_y
    run_x= -0.3
    run_y=0

#blocks
    block=turtle.Turtle()
    block.shape("BOMB.gif")
    block.speed(0)
    block.penup()
    block.goto(random.randint(-posx, posx), 290)
    p=0.2

    blocka=turtle.Turtle()
    blocka.shape("BOMB.gif")
    blocka.speed(0)
    blocka.penup()
    blocka.goto(random.randint(-posx, posx), -290)
    e=0.2

    blockb=turtle.Turtle()
    blockb.shape("BOMB.gif")
    blockb.speed(0)
    blockb.penup()
    blockb.goto(random.randint(-posx, posx), 290)
    r=0.2

    gun=turtle.Turtle()
    global shoot,ammo,gun_x,gun_y
    gun.shape("ink.gif")
    gun.speed(0)
    gun.penup()
    gun.goto(1600, 1600)
    shoot = False
    ammo =5
    gun_x=0
    gun_y=0
    w=20

#control chaser
    def ch_up():
        global ch_x,ch_y
        ch_x=0
        ch_y= speed_ch
    def ch_down():
        global ch_x,ch_y
        ch_x=0
        ch_y= -speed_ch
    def ch_right():
        ch.shape("ch_right.gif")
        global ch_x,ch_y
        ch_x=speed_ch
        ch_y= 0
    def ch_left():
        ch.shape("ch_left.gif")
        global ch_x,ch_y
        ch_x=-speed_ch
        ch_y= 0

#control runner
    def run_up():
        global run_x,run_y
        run_x=0
        run_y= speed_run
    def run_down():
        global run_x,run_y
        run_x=0
        run_y= -speed_run
    def run_right():
        run.shape("runner2_right.gif")
        global run_x,run_y
        run_x=speed_run
        run_y= 0
    def run_left():
        run.shape("runner2.gif")
        global run_x,run_y
        run_x=-speed_run 
        run_y= 0

    def shoot_gun():
        global gun_x, gun_y, shoot, ammo
        if not shoot and ammo > 0:
            gun.goto(ch.xcor(), ch.ycor())
            gun_x= ch_x*2
            gun_y= ch_y*2
            shoot = True
            ammo -= 1

#keyboard binding
    wn.listen()

    wn.onkeypress(ch_up, "w")
    wn.onkeypress(ch_down, "s")
    wn.onkeypress(ch_right, "d")
    wn.onkeypress(ch_left, "a")

    wn.onkeypress(run_up, "Up")
    wn.onkeypress(run_down, "Down")
    wn.onkeypress(run_right, "Right")
    wn.onkeypress(run_left, "Left")

    wn.onkeypress(nothing,"Return")
    wn.onkeypress(shoot_gun, "space")

    def explosion():
        playsound("explosion.mp3")
        
    def megumin_chant():
        playsound("megumin_chant.mp3")

    def game_over():
        playsound("game_over.mp3")

    def sound_setup():
        global thread, thread3, thread2
        thread = threading.Thread(target = explosion)
        thread2 = threading.Thread(target = megumin_chant)
        thread3 = threading.Thread(target = game_over)
        
    def chaser_win_1():
        pen.write("Runner is Caught!! The Chaser Wins", font=("Arial", 25))  

    def runner_win():
        pen.write("Chaser got hit. Runner wins!!", font=("Arial", 25))  

    def chaser_win_2():
        pen.write("The Runner got hit. The Chaser Wins", font=("Arial", 25))

    def time_over():
        pen.write("TIME OVER", font=("Arial", 25))
            
    def screen_text_setup():
        global thread4,thread5,thread6, thread7
        thread4 = threading.Thread(target = chaser_win_1)
        thread5 = threading.Thread(target = chaser_win_2)
        thread6 = threading.Thread(target = runner_win)
        thread7 = threading.Thread(target = time_over)

#checks:
    while True:
        wn.update()     #update sthe screen

        if block.ycor() < -290:
            block.goto(random.randint(-posx, posx), 290)
            pen.setx(-100)
            pen.clear()
            pen.write(s, font=("Arial", 25))  
            s -= 1
            p = 0.5

        if blocka.ycor()>290:
            blocka.goto(random.randint(-posx,posx), -290)
            e=0.5

        if blockb.ycor()< -290:
            blockb.goto(random.randint(-posx, posx), 290)
            r=0.5

        if (run.xcor()> ch.xcor()-q and run.xcor() < ch.xcor()+q) and (run.ycor()> ch.ycor()-q and run.ycor() < ch.ycor()+q):
            pen.clear()
            sound_setup()
            screen_text_setup()
            pen.setx(-300)
            thread4.start()
            thread.start()
            thread3.start()
            thread.join()
            sleep(3)
            turtle.bye()

        if ((block.xcor() > ch.xcor() - q and block.xcor() < ch.xcor() + q) and (block.ycor() > ch.ycor() - q and block.ycor() < ch.ycor() + q)) or ((blockb.xcor() > ch.xcor() - q and blockb.xcor() < ch.xcor() + q) and (blockb.ycor() > ch.ycor() - q and blockb.ycor() < ch.ycor() + q)) or ((blocka.xcor() > ch.xcor() - q and blocka.xcor() < ch.xcor() + q) and (blocka.ycor() > ch.ycor() - q and blocka.ycor() < ch.ycor() + q)):
            wn.bgpic("explosion_megumin.gif")
            wn.update()
            playsound("megumin_chant.mp3")
            pen.clear()
            playsound("explosion.mp3")
            pen.setx(-300)
            pen.write("Chaser got hit. Runner wins!!", font=("Arial", 25))  
            playsound("game_over.mp3")
            sleep(3)
            turtle.bye()

        if (run.xcor() > gun.xcor() - w and run.xcor() < gun.xcor() + w) and (gun.ycor() - w < run.ycor() < gun.ycor() + w):
            pen.clear()
            playsound("explosion.mp3")
            pen.setx(-300)
            pen.write("The Runner got hit. The Chaser Wins", font=("Arial", 25))
            sleep(3)
            turtle.bye()

        if s==0:
            pen.clear()
            playsound("game_over.mp3")
            pen.setx(-300)
            pen.write("TIME OVER", font=("Arial", 25))  
            sleep(3)
            turtle.bye()

        block.sety(block.ycor() - p)
        blocka.sety(blocka.ycor()+ e)
        blockb.sety(blockb.ycor() - r)

        ch.setx(ch.xcor()+ch_x)
        ch.sety(ch.ycor()+ch_y)
        run.setx(run.xcor()+run_x)
        run.sety(run.ycor()+run_y)
        gun.setx(gun.xcor()+gun_x)
        gun.sety(gun.ycor()+gun_y)
#bouncer
        if ch.xcor()>posx or ch.xcor()< -posx:
            ch_x = -ch_x
        if ch.ycor()>350 or ch.ycor()< -350:
            ch_y = -ch_y

        if run.xcor()>posx or run.xcor()< -posx:
            run_x = -run_x
        if run.ycor()>350 or run.ycor()< -350:
            run_y = -run_y
        if (gun.ycor()>390 or gun.ycor()< -390) or (gun.xcor()>390 or gun.xcor()<-390):
            shoot = False
#it joins loading module with the main module like a bridge

#settings
def settings():
    pen.setx(-300)
    pen.clear()
    pen.write("this is yet to be implemented.\nGood job finding this one.\nHear this music instead", font=("Arial", 25))  
    playsound("backgroundsound.mp3")
    pen.clear()
    turtle.bye()
#loading screen
def ihaveapenihaveanapple():
    global wn,pen,posx,check
    check="True"
    wn=turtle.Screen()
    wn.setup(width = 1.0, height = 1.0)
    wn.title("The Chase: 2Players")
    wn.bgpic("begining_bg.png")
    wn.addshape("settings.gif")
    posx = wn.window_width()//2-50
    posy = wn.window_height()//2-30
    

    sett=turtle.Turtle()
    sett.shape("settings.gif")
    sett.penup()
    sett.goto(posx, posy)

    pen = turtle.Turtle()
    pen.hideturtle()
    def uhhhh():
        pen.clear()
        pineapplepen()

    def color_coder(text,i,j,size):
        pen.penup()
        pen.setx(i)
        pen.sety(j)
        global color
        color=["violet","indigo","blue","green","yellow","orange","red","cyan"] #list of colors respectively
        global ren
        for ren in range(len(color)):    #accessess the list of colors
            wn.listen()
            wn.onkey(uhhhh,"Return")
            wn.onkey(settings,"x")
            pen.color(color[ren])
            pen.write(text, font=("Arial", size))
            sleep(0.25)

    pen.clear()
    i= -400
    j=0
    text="THE CHASE: 2PLAYERS"  #this will be displayed
    size=50
    color_coder(text,i,j,size)
    j=-100
    i=-150
    size=25
    text="press enter to begin"  #this will be displayed
    color_coder(text,i,j,size)
    j=-200
    i=-150
    size=10
    text="you cannot leave when the game is proceeding.\nThis setting was implemented by itsuren but you can exit by entering enter.\nThe Game admin is Ninamhang."  #this will be displayed (\n means hitting enter or new line)
    color_coder(text,i,j,size)
    sleep(3)
    pen.clear()
    uhhhh()

ihaveapenihaveanapple() #this is required to initiate the program else the program wont run



