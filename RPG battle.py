from quitwohoho import keluarout, lanjutan

#########################################
#Player Name
p_name = input("Welcome to RPG Battle .please input your name.")
#Initial PLayer Stats
p_str = 5
p_hp= 10
p_maxhp=10
p_lv= 1
#Player EXP
p_exp= 0
p_explvup= 10
#________________________________________
#Enemy Proto
e_name = {"namaa":["Tante Vero", "Bagus sang Manusia Millenium", "Aldi sang penakluk dunia", "One Punch Minaldi", "Alfi the Legend", "Ashoka dewa"]}
import random
e_hp = 10
e_str= 0
e_expdrop= 10
#Enemy stat buat reset
e_hp2 = 10
e_str2= 2
e_expdrop2= 0
z = 0
x= str(0)
e_expmod= 0
e_hpmod= 0
e_strmod= 0

def main_menu():
    x=input("Welcome "+ p_name + " to the main menu.please input your choice 1.battle 2.show menu 3.quit")
    if x=="1" :
        print ("[ENEMY ENCOUNTER]")
        x, e_expmod, e_hpmod,e_strmod, w, b=battle_screen()
    elif x=="2" :
        show_data()
        main_menu()
    elif x=="3":
        siap = lanjutan("Bye!","Hope to see you again! :D")
        siap.mantap()
    else:
        print("please input valid number.")
        main_menu()
    return

def show_data():
    print("Name: "+ str(p_name))
    print("Lv: "+str(p_lv))
    print("HP: "+str(p_hp))
    print("STR: "+str(p_str))
    print("EXP: "+str(p_exp) + "/" + str(p_explvup))
    return

def startup():
    """

    :rtype: object
    """
    p_name
    main_menu()
    return

def battle_screen():
    global p_hp
    global p_str
    global p_maxhp
    global p_exp
    global p_lv
    b= random.choice(e_name["namaa"])
    w= random.randint(1,5)
    x=str(b)
    z= str(w)
    e_hpmod=int(e_hp) +int(z)
    e_strmod=int(e_str) +int(z)
    e_expmod=int(e_expdrop) + int(z)
    print ( x + " LV "+ z +" appeared!")
    print ("Show status")
    print("Name: "+ x)
    print("Lv: "+ z)
    print("HP: "+str(e_hpmod))
    print("STR: "+str(e_strmod))
    print("EXP Drop: "+str(e_expmod))
    print("____________________________")
    print("------[INITIATE BATTLE]------")
    while e_hpmod > 0 or p_hp > 0:
        input("please press enter to continue")
        e_hpmod -= p_str
        print(p_name+" have attacked!")
        input("please press enter to continue")
        p_hp -= e_strmod
        print(str(x)+" have attacked!")
        if e_hpmod <= 0:
            p_hp = p_maxhp
            p_exp += e_expmod
            if p_exp >= 10:
                print("congratulation you've leveled up!")
                print("your Level grow by 1")
                print("your HP grow by 1")
                print("your STR grow by 1")
                p_maxhp += 1
                p_str += 1
                p_exp = 0
                p_lv += 1
                p_hp = p_maxhp
                main_menu()
            else:
                print("Congratulation you win")
                main_menu()
        elif p_hp <= 0:
            print("You lose. better luck next time")
            p_hp = p_maxhp
            main_menu()
        else:
            print("Next Round")

    return x, e_expmod, e_hpmod, e_strmod, w,b
startup()
