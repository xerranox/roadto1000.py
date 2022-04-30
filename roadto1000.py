#Librerias
from email.mime import application
import turtle
import time
import random
from tkinter import messagebox

#Variables
puntuacion = 0

#Ventana
ventana = turtle.Screen()
ventana.title("Road To 1000 By: xerranox")
ventana.bgcolor("Black")
ventana.setup(width=1080, height=720)

#Limite arriba
barrera = turtle.Turtle()
barrera.goto(-550, 300)
barrera.pensize(2)
barrera.pencolor("White")
barrera.speed(2)
barrera.goto(550, 300)
barrera.hideturtle()

#Limite abajo
barrera1 = turtle.Turtle()
barrera1.goto(550, -300)
barrera1.pensize(2)
barrera1.pencolor("White")
barrera1.speed(2)
barrera1.goto(-550, -300)
barrera1.hideturtle()

#Mini limite
barrera1 = turtle.Turtle()
barrera1.goto(-440, -360)
barrera1.pensize(2)
barrera1.pencolor("White")
barrera1.speed(2)
barrera1.goto(-440, -300)
barrera1.hideturtle()

#Texto
texto = turtle.Turtle()
texto.color("White")
texto.penup()
texto.hideturtle()
texto.goto(0, 315)
texto.write("--------------------------- ROAD TO 1000 ---------------------------", align="center", font=("Courier", 20, "normal"))

#Copyright
Copyright = turtle.Turtle()
Copyright.color("White")
Copyright.penup()
Copyright.hideturtle()
Copyright.goto(0, -340)
Copyright.write("                    By: xerranox", align="left", font=("Courier", 20, "normal"))

#Jugador
jugador = turtle.Turtle()
jugador.direccion = "quieto"
jugador.color("White")
jugador.penup()
jugador.shape("square")
jugador.goto(0, 0)

#Funciones
def arriba():
    jugador.direccion = "arriba"
def abajo():
    jugador.direccion = "abajo"
def derecha():
    jugador.direccion = "derecha"
def izquierda():
    jugador.direccion = "izquierda"

#Teclado
ventana.listen()
ventana.onkeypress(arriba, "w")
ventana.onkeypress(abajo, "s")
ventana.onkeypress(derecha, "d")
ventana.onkeypress(izquierda, "a")

#Movimiento
def movimiento():
    if jugador.direccion == 'arriba':
        y = jugador.ycor()
        jugador.sety(y+10)
    if jugador.direccion == 'abajo':
        y = jugador.ycor()
        jugador.sety(y-10)
    if jugador.direccion == 'derecha':
        x = jugador.xcor()
        jugador.setx(x+10)
    if jugador.direccion == 'izquierda':
        x = jugador.xcor()
        jugador.setx(x-10)

#Enemigo
enemigo = turtle.Turtle()
enemigo.color("White")
enemigo.shape("circle")
enemigo.penup()
enemigo.goto(100, -100)

#Marcador
punt = turtle.Turtle()
punt.speed(0)
punt.color("white")
punt.penup()
punt.hideturtle()
punt.goto(-450, -345)
punt.write("0", align="right", font=("Courier", 25, "normal"))

#Perder
def gameover():
    time.sleep(1)
    jugador.goto(0, 0)
    jugador.direccion = "quieto"
    punt.clear()
    punt.write("{}".format(puntuacion), align="right", font=("Courier", 25, "normal"))

#Juego
while True:
    ventana.update()

    #Movimiento
    movimiento()

    #Choque pared
    if jugador.xcor() > 550 or jugador.xcor() < -550 or jugador.ycor() > 280 or jugador.ycor() < -280:
        puntuacion = 0
        gameover()
    
    #Choque punto
    if jugador.distance(enemigo) < 20:
        x = random.randint(-16, 16)
        y = random.randint(-13, 13)
        puntuacion += 1
        enemigo.goto(x*20, y*20)
        punt.clear()
        punt.write("{}".format(puntuacion), align="right", font=("Courier", 25, "normal"))

    if puntuacion >= 1000:
        print(messagebox.askretrycancel(message="El juego se va ha cerrar automaticamente no te preocupes...", title="¡FELICIDADES!"))
        quit()