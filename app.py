from tkinter import *
from tkinter import messagebox
import sqlite3
from formulario.formulario import form
import os
import time
#-------------------------------------
#FUNCION PING

def ping():
    miConexion = sqlite3.connect("form.db")
    miCursor = miConexion.cursor()
    miCursor.execute("SELECT * FROM form")
    elUsuario = miCursor.fetchall()
    for form in elUsuario:
        response = os.system("ping " + form[13])

        if response == 0:

            print ("Hay conexion"+form[13])
            lista.config(state="normal")
            lista.insert(1.0,"\nConectando..."+"\nConexión \nestablecida con:\n"+form[13]+"\n")
            lista.config(state="disable")
            if form[13] == "192.168.1.100":
                botonliquid.config(image=pc1)#usain
            elif form[13] == "192.168.1.126":
                botonliquid2.config(image=pc1)#walter
            elif form[13] == "192.168.1.71":
                botonliquid3.config(image=pc1)#martin
            else:
                pass

        else:
            print ("No hay conexion"+form[13])
            lista.config(state="normal", fg="red")
            lista.insert(1.0,"Conectando..."+"\nError de coneccion con "+form[13])
            lista.config(state="disable")
            if form[13] == "192.168.1.100":
                botonliquid.config(image=pc2)
            elif form[13] == "192.168.1.126":
                botonliquid2.config(image=pc2)
            elif form[13] == "192.168.1.71":
                botonliquid3.config(image=pc2)#martin
            else:
                pass
#---------------------------------------


#---------------funciones para ventanas


def haberes():
    ventana = Toplevel()
    #ventana.iconbitmap("")
    ventana.geometry("300x60+1035+580")
    ventana.config(bg="white")
    ventana.resizable(0, 0)
    lista = Text(ventana, width=30, height=5)
    lista.place(x=1, y=1)
    lista.config(state="disable")
    miConexion = sqlite3.connect("form.db")
    miCursor = miConexion.cursor()
    miCursor.execute("SELECT * FROM form WHERE ip="+"'192.168.1.126'")
    elUsuario = miCursor.fetchall()
    for form in elUsuario:
        lista.config(state="normal")
        lista.insert(1.0, "IP: " + form[13] + "\n"
                        + "MAC: " + form[14] +"\n"
                        +"Encargado: " + form[5])
        lista.config(state="disable")
    miConexion.commit()

def haberes2():
    ventana = Toplevel()
    #ventana.iconbitmap("")
    ventana.geometry("300x60+1035+580")
    ventana.config(bg="white")
    ventana.resizable(0, 0)
    lista = Text(ventana, width=30, height=5)
    lista.place(x=1, y=1)
    lista.config(state="disable")
    miConexion = sqlite3.connect("form.db")
    miCursor = miConexion.cursor()
    miCursor.execute("SELECT * FROM form WHERE ip="+"'192.168.1.100'")
    elUsuario = miCursor.fetchall()
    for form in elUsuario:
        lista.config(state="normal")
        lista.insert(1.0, "IP: " + form[13] + "\n"
                        + "MAC: " + form[14] +"\n"
                        +"Encargado: " + form[5])
        lista.config(state="disable")
    miConexion.commit()

def haberes3():
    ventana = Toplevel()
    #ventana.iconbitmap("")
    ventana.geometry("300x60+1035+580")
    ventana.config(bg="white")
    ventana.resizable(0, 0)
    lista = Text(ventana, width=30, height=5)
    lista.place(x=1, y=1)
    lista.config(state="disable")
    miConexion = sqlite3.connect("form.db")
    miCursor = miConexion.cursor()
    miCursor.execute("SELECT * FROM form WHERE ip="+"'192.168.1.72'")
    elUsuario = miCursor.fetchall()
    for form in elUsuario:
        lista.config(state="normal")
        lista.insert(1.0, "IP: " + form[13] + "\n"
                        + "MAC: " + form[14] +"\n"
                        +"Encargado: " + form[5])
        lista.config(state="disable")
    miConexion.commit()


#------------ configuracion de la raiz de la ventana---------------------------------
raiz = Tk()
raiz.title("DEPARTAMENTO DE INFORMATICA")
#raiz.resizable(0, 0)
#raiz.iconbitmap("final.ico")
raiz.state("zoomed")#mazimizar ventana
raiz.config(bg="white")
raiz.config(cursor="hand2")

#------------------------introducimos una imagen y titulo----------------------------
miImagen = PhotoImage(file="img/plantas.png")
label7 = Label(raiz, image=miImagen, bg="white").place(x=180, y=0)

# ---------------------------------funciones-----------------------------------------
def licencia():
    messagebox.showinfo("LYON", "Version 1.0.1 \n2018 all rights reserved.")


def salir():
    valor = messagebox.askquestion("Salir", "¿Deseas salir de la aplicacion?")
    if valor == "yes":
        raiz.destroy()
#---------------VENTANA PASAJES-----------------------------------------
#def abrirpasajes():
    #pasaje()
#---------------ABRIR DUBSIDIOS----------------------------------------
def abrirformulario():
    form()


# configura el menu y submenu
barramenu = Menu(raiz)
raiz.config(menu=barramenu)
archivo = Menu(barramenu, tearoff=0,font=20)
archivo.add_command(label="Salir", command=salir)

formulario = Menu(barramenu, tearoff=0, font=20)
formulario.add_command(label="Formulario", command=abrirformulario)
#formulario.add_separator()#separador de menu


becados = Menu(barramenu, tearoff=0,  font=20)
becados.add_command(label="Buscar")

empleo = Menu(barramenu, tearoff=0, font=20)
empleo.add_command(label="")


ayuda = Menu(barramenu, tearoff=0, font=20)
ayuda.add_command(label="Acerca de...", command=licencia)
#-------------------------ingresar en menu-------------------------------
barramenu.add_cascade(label="ARCHIVO", menu=archivo)

barramenu.add_cascade(label="RELEVAMIENTO", menu=formulario)

barramenu.add_cascade(label="SERVICIO TECNICO", menu=becados)

barramenu.add_cascade(label="AYUDA", menu=ayuda)


#--------------------------IMAGENES DE PC-------------------------------
pc1 = PhotoImage(file="img/pc.gif")
pc2 = PhotoImage(file="img/pc2.gif")
#la vivienda-----------------------------------------------------------
botonvivienda = Button(raiz, image=pc1)
botonvivienda.place(x=340, y=340)
#----------------------------------
#------------------liquidacion de haberes-------------------------------
botonliquid = Button(raiz, image=pc1, command=haberes2)
botonliquid.place(x=1005, y=540)
#
botonliquid2 = Button(raiz, image=pc1, command=haberes)
botonliquid2.place(x=985, y=575)
#
botonliquid3 = Button(raiz, image=pc1, command=haberes3)
botonliquid3.place(x=1005, y=610)

#----------------------SUMINISTROS--------------------------------------
botonsumi=Button(raiz, image=pc1)
botonsumi.place(x=1040, y=628)
#
botonsumi1=Button(raiz, image=pc1)
botonsumi1.place(x=1040, y=602)
#
botonsumi2=Button(raiz, image=pc1)
botonsumi2.place(x=1040, y=575)
#
botonsumi2=Button(raiz, image=pc1)
botonsumi2.place(x=1065, y=575)
#-----------------------------------------------------------------



#--------------------------BOTONES GRANDE PARA HACER PING
pc3 = PhotoImage(file="img/red.png")
botonvivienda = Button(raiz, image=pc3, command=ping)
botonvivienda.place(x=10, y=30)
#-----------------------------------------
lista = Text(raiz, width=19, height=18, bg="black", fg="white")
lista.place(x=10, y=90)
scrollvert = Scrollbar(raiz, command=lista.yview)
scrollvert.place(x=165, y=90, height=237)
lista.config(yscrollcommand=scrollvert.set, state="disable", font=("OCR A Extended",10))



raiz.mainloop()
