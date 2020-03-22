
from turtle import *
 
pensize(2)
hideturtle()
 
#Det mangler kode der ... står i main-funksjonen under, og du skal skrive den koden som trengs her.
#Anbefaler å lese teksten inni print() for å få en anelse om hva som må gjøres.
def main():
    print("Jeg kan tegne en muffins, en blomst, eller en sjokolade."
        "\nDu kan bestemme hva jeg skal tegne,"
        "\nhvor mange striper, blad eller ruter det jeg skal tegne har,"
        "\nog fargene som skal brukes."
        "\nDette gjør du ved å oppgi en streng på følgende format:"
        '\n"hva,antall,farge1,farge2,farge3"'
        "\nhva er enten 'm' for muffins, 'b' for blomst, eller 's' for sjokolade,"
        "\nantall er et positivt heltall større enn null,"
        "\nog fargene du kan velge mellom er som følger:"
        "\nred, yellow, purple, brown, green, blue, pink, grey, orange"
        "\n")
    s = input("Hva velger du? ")   #Skriv inn kode slik at det bruker har skrevet inn tegnes med de oppgitte spesifikasjonene.
    sList = s.split(',')

    if sList[0] == 'm':
        cupcake(int(sList[1]), sList[2], sList[3], sList[4])
        
    elif sList[0] == 'b':
        flower(int(sList[1]), sList[2], sList[3], sList[4])
        
    elif sList[0] == 's':
        chocolate(int(sList[1]), sList[2], sList[3], sList[4])
    else:
        print('Du oppga feil verdier\n')
        main()

#---------------------------------------------------------------------------------------------------------------------------------------------
#KODEN UNDER TRENGER DU IKKE Å SE PÅ. OPPGAVEN OMHANDLER MAIN-FUNKSJONEN OVER 
       
def petal():
    for i in range(2):
        forward(50)
        left(30)
        forward(75)
        left(30)
        forward(50)
        left(120)
         
def flower(num,f1,f2,f3):
    pencolor(f1)
    bgcolor(f2)
    fillcolor(f3)
    begin_fill()
    for i in range(num):
        petal()
        left(360/num)
    end_fill()
 
def cupcake(num,f1,f2,f3):
    pencolor(f1)
    bgcolor(f2)
    fillcolor(f3)
    left(100)
    begin_fill()
    forward(30)
    backward(30)
    right(100)
    forward(100)
    left(80)
    forward(30)
    left(100)
    forward(110)
    end_fill()
    for j in range(num):
        backward(111/(num+1))
        if (j>num/2):
            v = 80
        elif j==num//2:
            v = 90
        else:
            v = 100
        left(v)
        forward(30)
        backward(30)
        right(v)
    backward(111/(num+1))
    fillcolor("moccasin")           #For å endre på fargen til selve muffinsen, kan du bytte ut 'moccasin' med en annen farge
    begin_fill()
    right(100)
    for i in range(200):
        forward(1)
        left(1)
    end_fill()
 
def rectangle():
    begin_fill()
    forward(15)
    left(90)
    forward(20)
    left(90)
    forward(15)
    left(90)
    forward(20)
    end_fill()
     
def chocolate(num,f1,f2,f3):
    pencolor(f1)
    bgcolor(f2)
    fillcolor(f3)
    rectangle()
    for i in range(1,num):
        if i%3 == 0:
            left(90)
            forward(30)
            right(90)
            forward(20)
            left(90)
            rectangle()
        else:
            left(90)
            backward(15)
            rectangle()
while True:
    main()
