global f

f=0

#t_movie function is used to select movie name

def t_movie():
    global f
    f=f+1
    print("Which movie you want to watch ? ")
    print("1 . KGF ")
    print("2 . Goat ")
    print("3 . Garudan ")
    print("4 . Maharaja ")
    movie = int(input("Enter Your Choice Movie : "))
    if movie == 4:
        center()
        theater()
        return 0
    if f==1:
        theater()

#This theater function used to select screen

def theater():
    print("Which screen do you want to watch movie:")
    print("1,SCREEN 1")
    print("2,SCREEN 2")
    print("3,SCREEN 3")
    a=int(input("Choose your screen:"))
    ticket=int(input("How many no.of tickets do you want?:"))
    timing(a)

#This timing function used to select timing for movie


def timing(a):
    time1={
        "1":"10.00 - 1.00" ,
        "2":"1.10 - 4.10" ,
        "3":"4.20-7.20" ,
        "4":"7.30-10.30",
        }
    time2={
        "1":"10.15-1.15",
        "2":"1.25-4.25",
        "3":"4.35-7.35",
        "4":"7.45-10.45"
        }
    time3={
        "1":"10.30-1.30",
        "2":"1.40-4.40",
        "3":"4.50-7.50",
        "4":"8.00-10.45"
        }
    if a==1:
        print("choose your time:")
        print(time1)
        t=input("select your time:")
        x=time1[t]
        print("Successful!, enjoy your movie" +x)
    elif a==2:
        print("choose your time:")
        print(time2)
        t=input("select your time:")
        x=time21[t]
        print("Successful!, enjoy your movie" +x)
    elif a==3:
        print("choose your time:")
        print(time3)
        t=input("select your time:")
        x=time3[t]
        print("Successful!, enjoy your movie" +x)
    return 0


        
def movie(theater):
    if theater == 1:
        t_movie()
    elif theater == 2:
        t_movie()
    elif theater == 3:
        t_movie()
    elif theater == 4:
        city()
    else:
        print("Wrong choice")

def center():
    print("Which theater do you see the movie?")
    print("1 . PVR")
    print("2 . MARIS")
    print("3 . INOX")
    print("4 . Back")
    a=int(input("Choice your option:"))
    movie(a)
    return 0
#This function is used to select the city
def city():
    print("HAI WELCOME TO MOVIE TICKET BOOKING:")
    print("WHERE YOU WANT TO WATCH MOVIE?")
    print("1,Chennai")
    print("2,Trichy")
    print("3,Virudhachalam")
    place=int(input("Choose your option:"))
    if place == 1:
        center()
    elif place == 2:
        center()
    elif place == 3:
        center()
    else:
        print("Wrong Choice")
    
        
city()       
    
        
