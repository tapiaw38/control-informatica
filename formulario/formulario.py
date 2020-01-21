from tkinter import *
from tkinter import messagebox
import sqlite3
from datetime import datetime, date, time, timedelta
import calendar
import time



# --------------COFIGURACION DE VENTANA
def form():
    ventana = Toplevel()
    #ventana.iconbitmap("")
    ventana.geometry("620x640+370+50")
    ventana.config(bg="white")
    ventana.resizable(0, 0)

    # -----------------variables
    borrabusqueda = StringVar()
    tiempo = str(time.strftime("%d/%m/%y"))
    borra1 = StringVar()
    borra2 = StringVar()
    borra3 = StringVar()
    borra4 = StringVar()
    borra5 = StringVar()
    borra6 = StringVar()
    borra7 = StringVar()
    borra8 = StringVar()
    borra9 = StringVar()
    borra10 = StringVar()
    borra11 = StringVar()
    borra12 = StringVar()
    borra13 = StringVar()
    borra14 = StringVar()
    borra15 = StringVar()
    borra16 = StringVar()

# ---------------------funcion borrar
    def borrarcampos():
        borrabusqueda.set("")
        borra1.set(tiempo)
        borra2.set("")
        borra3.set("")
        borra4.set("")
        borra5.set("")
        borra6.set("")
        borra7.set("")
        borra8.set("")
        borra9.set("")
        borra10.set("")
        borra11.set("")
        borra12.set("")
        borra13.set("")
        borra14.set("")
        borra15.set("")
        borra16.set("")
        botonguarda.config(state=NORMAL, bg="white")

    def guardardatos():
        miConexion = sqlite3.connect("form.db")
        miCursor = miConexion.cursor()
        if borra1.get() == "":
            messagebox.showerror("ERROR", "Debes completar todos lo campos")
        elif borra2.get() == "":
            messagebox.showerror("ERROR", "Debes completar todos lo campos")
        elif borra3.get() == "":
            messagebox.showerror("ERROR", "Debes completar todos lo campos")
        elif borra4.get() == "":
            messagebox.showerror("ERROR", "Debes completar todos lo campos")
        elif borra5.get() == "":
            messagebox.showerror("ERROR", "Debes completar todos lo campos")
        elif borra6.get() == "":
            messagebox.showerror("ERROR", "Debes completar todos lo campos")
        elif borra7.get() == "":
            messagebox.showerror("ERROR", "Debes completar todos lo campos")
        elif borra8.get() == "":
            messagebox.showerror("ERROR", "Debes completar todos lo campos")
        elif borra10.get() == "":
            messagebox.showerror("ERROR", "Debes completar todos lo campos")
        elif borra11.get() == "":
            messagebox.showerror("ERROR", "Debes completar todos lo campos")
        elif borra12.get() == "":
            messagebox.showerror("ERROR", "Debes completar todos lo campos")
        elif borra13.get() == "":
            messagebox.showerror("ERROR", "Debes completar todos lo campos")
        elif borra14.get() == "":
            messagebox.showerror("ERROR", "Debes completar todos lo campos")
        elif borra15.get() == "":
            messagebox.showerror("ERROR", "Debes completar todos lo campos")
        elif borra16.get() == "":
            messagebox.showerror("ERROR", "Debes completar todos lo campos")
        else:
            miCursor.execute("INSERT INTO form VALUES(NULL, '" + borra1.get() +
                             "','" + borra2.get() +
                             "','" + borra3.get() +
                             "','" + borra4.get() +
                             "','" + borra5.get() +
                             "','" + borra6.get() +
                             "','" + borra7.get() +
                             "','" + borra8.get() +
                             "','" + borra9.get() +
                             "','" + borra10.get() +
                             "','" + borra11.get() +
                             "','" + borra12.get() +
                             "','" + borra13.get() +
                             "','" + borra14.get() +
                             "','" + borra15.get() +
                             "','" + borra16.get() +
                             "')")

            miConexion.commit()
            opcion = messagebox.askquestion("ATENCIÓN", " Registro Guardado\n¿Deseas ingresar un nuevo registro?")
            if opcion == "yes":
                ventana.destroy()
                form()
            else:
                ventana.destroy()
    #---------------------------------------ACTUALIZAR
    def actualizar():

            miConexion = sqlite3.connect("form.db")
            miCursor = miConexion.cursor()
            miCursor.execute("UPDATE form SET fecha='" + borra1.get() +
                             "', secretaria ='" + borra2.get() +
                             "', direccion='" + borra3.get() +
                             "', departamento='" + borra4.get() +
                             "', responsable='" + borra5.get() +
                             "', dni='" + borra6.get() +
                             "', procesador='" + borra7.get() +
                             "', memoria_tipo='" + borra8.get() +
                             "', memoria_cap='" + borra9.get() +
                             "', HDD='" + borra10.get() +
                             "', usuario='" + borra11.get() +
                             "', contrasena='" + borra12.get() +
                             "', mac='" + borra14.get() +
                             "', monitor='" + borra15.get() +
                             "', impresora='" + borra16.get() +
                             "' WHERE ip=" +"'"+borra13.get()+"'")
            miConexion.commit()
            opcion = messagebox.askquestion("ATENCIÓN", " Registro Modificado\n¿Deseas volver al registro de subsidios?")
            if opcion == "yes":
                ventana.destroy()
                form()
            else:
                ventana.destroy()

#---------------------------------------------------------------------------------------------
    def buscaIP():
        try:
            miConexion = sqlite3.connect("form.db")
            miCursor = miConexion.cursor()
            miCursor.execute("SELECT * FROM form WHERE ip=" +"'"+ borrabusqueda.get()+"'")
            elUsuario = miCursor.fetchall()
            for form in elUsuario:
                borra1.set(form[1])
                borra2.set(form[2])
                borra3.set(form[3])
                borra4.set(form[4])
                borra5.set(form[5])
                borra6.set(form[6])
                borra7.set(form[7])
                borra8.set(form[8])
                borra9.set(form[9])
                borra10.set(form[10])
                borra11.set(form[11])
                borra12.set(form[12])
                borra13.set(form[13])
                borra14.set(form[14])
                borra15.set(form[15])
                borra16.set(form[16])
            miConexion.commit()
            botonguarda.config(state=DISABLED, bg="red")
        except:
            messagebox.showwarning("LYON", "Ingresa una busqueda valida")

 #------------------TITULO
    titulo_subsidio=Label(ventana, text="Relevamiento de oficina", bg="white",font=("Bodoni MT Condensed",25)).place(x=195,y=0)

 #------------------BUSQUEDA
    busqueda = Label(ventana, text="Busqueda por IP",font=("OCR A Extended",11))
    busqueda.place(x=30, y=50, width=200)
    busqueda=Entry(ventana, justify="center",font=("OCR A Extended",13),textvariable=borrabusqueda)
    busqueda.place(x=230,y=50, width=200)
    botonbusqueda= Button(ventana, text="BUSCAR", bg='white',height=1, command=buscaIP).place(x=440,y=50)
 #-----------------FORMULARIO
 #-----------------COLUMNA 1
    etiqueta = Label(ventana, text="Fecha",font=15)
    etiqueta.place(x=30, y=100, width=220)
    entrada=Entry(ventana, justify="center",font=15,textvariable=borra1)
    entrada.place(x=30,y=130, width=220)
    #------------------------------------------
    etiqueta2 = Label(ventana, text="Secretaria",font=(15))
    etiqueta2.place(x=30, y=160, width=220)
    entrada2 = Entry(ventana,justify="center",font=(13),textvariable=borra2)
    entrada2.place(x=30, y=190, width=220)
    #-------------------------------------------
    etiqueta3 = Label(ventana, text="Dirección",font=(15))
    etiqueta3.place(x=30, y=220, width=220)
    entrada3 = Entry(ventana,justify="center",font=(13),textvariable=borra3)
    entrada3.place(x=30, y=250, width=220)
    #--------------------------------------------
    etiqueta4 = Label(ventana, text="Departamento",font=(15))
    etiqueta4.place(x=30, y=280, width=220)
    entrada4= Entry(ventana,justify="center",font=(13),textvariable=borra4)
    entrada4.place(x=30, y=310, width=220)
    #--------------------------------------------
    etiqueta5 = Label(ventana, text="Responsable",font=(15))
    etiqueta5.place(x=30, y=340, width=220)
    entrada5= Entry(ventana,justify="center",font=(13),textvariable=borra5)
    entrada5.place(x=30, y=370, width=220)
    #--------------------------------------------
    etiqueta6 = Label(ventana, text="DNI",font=(15))
    etiqueta6.place(x=30, y=400, width=220)
    entrada6 = Entry(ventana,justify="center",font=(15),textvariable=borra6)
    entrada6.place(x=30, y=430, width=220)
    #--------------------------------------------
    etiqueta7 = Label(ventana, text="Procesador",font=(15))
    etiqueta7.place(x=30, y=460, width=220)
    entrada7 = Entry(ventana,justify="center",font=(15),textvariable=borra7)
    entrada7.place(x=30, y=490, width=220)
    #--------------------------------------------
    etiqueta8 = Label(ventana, text="Memoria Tipo",font=(15))
    etiqueta8.place(x=30, y=520, width=220)
    entrada8 = Entry(ventana,justify="center",font=(15),textvariable=borra8)
    entrada8.place(x=30, y=550, width=220)
    #--------------------------------------------

 #----------------COLUMNA 2


    etiqueta9 = Label(ventana, text="Memoria Capacidad",font=(15))
    etiqueta9.place(x=360, y=100, width=220)
    entrada9 = Entry(ventana,justify="center",font=(15),textvariable=borra9)
    entrada9.place(x=360, y=130, width=220)
    #--------------------------------------------
    etiqueta10 = Label(ventana, text="HDD Capacidad",font=(15))
    etiqueta10.place(x=360, y=160, width=220)
    entrada10 = Entry(ventana,justify="center",font=(15),textvariable=borra10)
    entrada10.place(x=360, y=190, width=220)
    #--------------------------------------------
    etiqueta11 = Label(ventana, text="Usuario",font=(15))
    etiqueta11.place(x=360, y=220, width=220)
    entrada11 = Entry(ventana,justify="center",font=(15),textvariable=borra11)
    entrada11.place(x=360, y=250, width=220)
    #--------------------------------------------
    etiqueta12 = Label(ventana, text="Contraseña",font=(15))
    etiqueta12.place(x=360, y=280, width=220)
    entrada12 = Entry(ventana,justify="center",font=(15),textvariable=borra12)
    entrada12.place(x=360, y=310, width=220)
    #--------------------------------------------
    etiqueta13 = Label(ventana, text="Dirección IP",font=(15))
    etiqueta13.place(x=360, y=340, width=220)
    entrada13 = Entry(ventana,justify="center",font=(15),textvariable=borra13)
    entrada13.place(x=360, y=370, width=220)
    #--------------------------------------------
    etiqueta14 = Label(ventana, text="Dirección MAC",font=(15))
    etiqueta14.place(x=360, y=400, width=220)
    entrada14 = Entry(ventana,justify="center",font=(15),textvariable=borra14)
    entrada14.place(x=360, y=430, width=220)
    #--------------------------------------------
    etiqueta15 = Label(ventana, text="Monitor Marca/Tipo/Pulgadas",font=(10))
    etiqueta15.place(x=360, y=460, width=220)
    entrada15= Entry(ventana,justify="center",font=(13),textvariable=borra15)
    entrada15.place(x=360, y=490, width=220)
    #--------------------------------------------
    etiqueta16 = Label(ventana, text="Impresora Marca/Tipo",font=(12))
    etiqueta16.place(x=360, y=520, width=220)
    entrada16= Entry(ventana,justify="center",font=(13),textvariable=borra16)
    entrada16.place(x=360, y=550, width=220)
    #--------------------------------------------
    #----------BOTONES
    botonborra= Button(ventana, text="BORRAR", bg='white',font=10 , width=11, height=1, command=borrarcampos).place(x=150,y=590)
    botonguarda= Button(ventana, text="GUARDAR", bg='white',font=10 , width=11, height=1, command=guardardatos)
    botonguarda.place(x=260,y=590)
    botonactualiza= Button(ventana, text="ACTUALIZA", bg='white',font=10 , width=11, height=1, command=actualizar).place(x=370,y=590)

#------------------------------------------------------------------------------



    ventana.mainloop()
