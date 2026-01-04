from sqlite3 import *
from tkinter import *
import tkinter as tk
from tkinter import messagebox
base=connect('LAURA_BASE')
cursor=base.cursor()
def eliminartodoMENOSUNO():
    try:
        frame.destroy()
    except:
        pass
def eliminartodo():
    global VER,CONTADOR
    VER=0
    CONTADOR=0
    try:
        frame.destroy()
    except:
        pass
def volverainicio():
    global raiz
    raiz.destroy()
    inicio()
def cerrar0():
    global base,raiz1
    base.close()
    raiz1.destroy()
#####################################################################################################################################################################
#####################################################################################################################################################################
# CODE IN SPANISH
def spanish():
    global raiz,VARIABLE,frame,Y,v,VER,CONTADOR,Y,VARIABLE1
    VARIABLE = 0
    VARIABLE1 = 0
    Y=0
    v=0
    #################################################################################################################################################################
    #################################################################################################################################################################
    # INGRESAR DATOS DE PRODUCTO
    def confirmar1111():
        global VARIABLE,unidad,precio
        try:
            unidad=cuadro1.get()
            precio=float(cuadro2.get())
            if unidad.isalpha() == True:
                cursor.execute('SELECT * FROM MATERIA_PRIMA')
                MP=cursor.fetchall()
                v=0
                try:
                    while True:
                        if MP[v][1] == materiaprima.upper():
                            # LA MATERIA PRIMA EXISTE
                            VARIABLE=3
                            menu1111()
                            break
                        else:
                            v+=1
                        if v == len(MP):
                            cursor.execute('INSERT INTO MATERIA_PRIMA VALUES(NULL,?,?,?,?,?)',(materiaprima.upper(),unidad.upper(),precio,'C',0),)
                            base.commit()
                            cursor.execute('SELECT * FROM MATERIA_PRIMA')
                            MP=cursor.fetchall()
                            v=0
                            try:
                                while True:
                                    if MP[v][1] == materiaprima.upper():
                                        # LA MATERIA PRIMA EXISTE
                                        cursor.execute('INSERT INTO RECETA VALUES(NULL,?,?,?,?)',(producto.upper(),materiaprima.upper(),cantidad,MP[v][4]),)
                                        base.commit()
                                        if tipo.upper() == 'F':
                                            variable=0
                                            cursor.execute('SELECT * FROM PRODUCTO')
                                            PRO=cursor.fetchall()
                                            try:
                                                while True:
                                                    if PRO[variable][1] == producto.upper():
                                                        break
                                                    else:
                                                        variable+=1
                                                    if variable == len(PRO):
                                                        cursor.execute('INSERT INTO PRODUCTO VALUES(NULL,?,?)',(producto.upper(),preciocarta),)
                                                        base.commit()
                                                        break
                                            except IndexError:
                                                cursor.execute('INSERT INTO PRODUCTO VALUES(NULL,?,?)',(producto.upper(),preciocarta),)
                                                base.commit()
                                            VARIABLE=2
                                            menu111()
                                            break
                                        else:
                                            variable=0
                                            cursor.execute('SELECT * FROM MATERIA_PRIMA')
                                            MP=cursor.fetchall()
                                            try:
                                                while True:
                                                    if MP[variable][1] == producto.upper():
                                                        cursor.execute('UPDATE MATERIA_PRIMA set preciomateriaprima = (?) WHERE codigomateriaprima = (?)',(MP[variable][3]+((MP[v][3]*cantidad)/MP[variable][5]),MP[variable][0]),)
                                                        base.commit()
                                                        break
                                                    else:
                                                        variable+=1
                                                    if variable == len(MP):
                                                        cursor.execute('INSERT INTO MATERIA_PRIMA VALUES(NULL,?,?,?,?,?)',(producto.upper(),unidad.upper(),(MP[v][3]*cantidad)/cant,'E',cant),)
                                                        base.commit()
                                                        break
                                            except IndexError:
                                                cursor.execute('INSERT INTO MATERIA_PRIMA VALUES(NULL,?,?,?,?,?)',(producto.upper(),unidad.upper(),(MP[v][3]*cantidad)/cant,'E',cant),)
                                                base.commit()
                                            VARIABLE=2
                                            menu111()
                                        break
                                    else:
                                        v+=1
                                    if v == len(MP):
                                        # LA MATERIA PRIMA NO EXISTE
                                        VARIABLE=4
                                        menu1111()
                                        break
                            except IndexError:
                                VARIABLE=4
                                menu1111()
                            break
                except IndexError:
                    cursor.execute('INSERT INTO MATERIA_PRIMA VALUES(NULL,?,?,?,?,?)',(materiaprima.upper(),unidad.upper(),precio,'C',0),)
                    base.commit()
                    cursor.execute('INSERT INTO RECETA VALUES(NULL,?,?,?,?)',(producto.upper(),materiaprima.upper(),cantidad,'C'),)
                    base.commit()
                    variable=0
                    if tipo.upper() == 'F':
                        cursor.execute('SELECT * FROM PRODUCTO')
                        PRO=cursor.fetchall()
                        try:
                            while True:
                                if PRO[variable][1] == producto.upper():
                                    break
                                else:
                                    variable+=1
                                if variable == len(PRO):
                                    cursor.execute('INSERT INTO PRODUCTO VALUES(NULL,?,?)',(producto.upper(),preciocarta),)
                                    base.commit()
                                    break
                        except IndexError:
                            cursor.execute('INSERT INTO PRODUCTO VALUES(NULL,?,?)',(producto.upper(),preciocarta),)
                            base.commit()
                        VARIABLE=2
                        menu111()
                    else:
                        cursor.execute('SELECT * FROM MATERIA_PRIMA')
                        MP=cursor.fetchall()
                        try:
                            while True:
                                if MP[variable][1] == producto.upper():
                                    break
                                else:
                                    variable+=1
                                if variable == len(MP):
                                    cursor.execute('INSERT INTO MATERIA_PRIMA VALUES(NULL,?,?,NULL,?,?)',(producto.upper(),unidad.upper(),'E',cant),)
                                    base.commit()
                                    break
                        except IndexError:
                            cursor.execute('INSERT INTO MATERIA_PRIMA VALUES(NULL,?,?,NULL,?,?)',(producto.upper(),unidad.upper(),'E',cant),)
                            base.commit()
                        VARIABLE=2
                        menu111()
            else:
                VARIABLE=1
                menu1111()
        except ValueError:
            VARIABLE=1
            menu1111()
    def menu1111():
        eliminartodo()
        global frame,cuadro1,cuadro2,VARIABLE
        frame=Frame(raiz,width='700',height='430',bg='#273746')
        frame.pack()
        cuadro11=StringVar()
        cuadro10=StringVar()
        
        texto=Label(frame,text='INGRESO DE MATERIAS PRIMAS',font=('Radio Canada Big',16),bg='#273746',fg='snow')
        texto.place(relx=0.5,y=60,anchor=tk.CENTER,relwidth=1,relheight=0.10)
        if VARIABLE == 1:
            messagebox.showerror("ERROR", "INGRESO DE DATOS INCORRECTO")
            VARIABLE=0
        else:
            if VARIABLE == 3:
                messagebox.showerror("ERROR", "LA MATERIA PRIMA YA FUE INGRESADA")
                VARIABLE=0
            else:
                if VARIABLE == 4:
                    messagebox.showerror("ERROR", "DEBE AGREGAR ESA MATERIA PRIMA (O PUEDE VOLVER)")
                    VARIABLE=0
        texto=Label(frame,text='INGRESE EL NOMBRE DE LA MATERIA PRIMA:',font=('Radio Canada Big',12),bg='#273746',fg='snow')
        texto.place(x=10,y=130,relwidth=0.75,relheight=0.06)
        texto=Label(frame,text=materiaprima.upper(),font=('Radio Canada Big',12),bg='#273746',fg='snow')
        texto.place(x=500,y=130,relwidth=0.20,relheight=0.06)
        texto=Label(frame,text='INGRESE LA UNIDAD DE MEDIDA:',font=('Radio Canada Big',12),bg='#273746',fg='snow')
        texto.place(x=10,y=170,relwidth=0.75,relheight=0.06)
        cuadro1=Entry(frame,textvariable=cuadro11)
        cuadro1.place(x=500,y=170,relheight=0.06)
        texto=Label(frame,text='INGRESE EL PRECIO POR UNIDAD: ',font=('Radio Canada Big',12),bg='#273746',fg='snow')
        texto.place(x=10,y=210,relwidth=0.75,relheight=0.06)
        cuadro2=Entry(frame,textvariable=cuadro10)
        cuadro2.place(x=500,y=210,relheight=0.06)
        Button2=Button(frame,text='CONFIRMAR',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:confirmar1111())
        Button2.place(x=540,y=360,relwidth=0.17,relheight=0.05)
        Button2=Button(frame,text='VOLVER',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:menu111())
        Button2.place(x=40,y=360,relwidth=0.17,relheight=0.05)
    def confirmar111():
        global VARIABLE,materiaprima,cantidad
        try:
            materiaprima=cuadro0.get()
            if materiaprima == '':
                VARIABLE=1
                menu111()
            else:
                cantidad=float(cuadro1.get())
                cursor.execute('SELECT * FROM MATERIA_PRIMA')
                MP=cursor.fetchall()
                cursor.execute('SELECT * FROM RECETA')
                REC=cursor.fetchall()
                v=0
                try:
                    while True:
                        if MP[v][1] == materiaprima.upper():
                            # LA MATERIA PRIMA EXISTE
                            w=0
                            try:
                                while True:
                                    if materiaprima.upper() == REC[w][2] and producto.upper() == REC[w][1]:
                                        VARIABLE=4
                                        menu111()
                                        break
                                    else:
                                        w+=1
                                    if w == len(REC):
                                        cursor.execute('INSERT INTO RECETA VALUES(NULL,?,?,?,?)',(producto.upper(),materiaprima.upper(),cantidad,MP[v][4]),)
                                        base.commit()
                                        if tipo.upper() == 'F':
                                            variable=0
                                            cursor.execute('SELECT * FROM PRODUCTO')
                                            PRO=cursor.fetchall()
                                            try:
                                                while True:
                                                    if PRO[variable][1] == producto.upper():
                                                        break
                                                    else:
                                                        variable+=1
                                                    if variable == len(PRO):
                                                        cursor.execute('INSERT INTO PRODUCTO VALUES(NULL,?,?)',(producto.upper(),preciocarta),)
                                                        base.commit()
                                                        break
                                            except IndexError:
                                                cursor.execute('INSERT INTO PRODUCTO VALUES(NULL,?,?)',(producto.upper(),preciocarta),)
                                                base.commit()
                                            VARIABLE=2
                                            menu111()
                                        else:
                                            variable=0
                                            cursor.execute('SELECT * FROM MATERIA_PRIMA')
                                            MP=cursor.fetchall()
                                            try:
                                                while True:
                                                    if MP[variable][1] == producto.upper():
                                                        cursor.execute('UPDATE MATERIA_PRIMA set preciomateriaprima = (?) WHERE codigomateriaprima = (?)',(MP[variable][3]+((MP[v][3]*cantidad)/MP[variable][5]),MP[variable][0]),)
                                                        base.commit()
                                                        break
                                                    else:
                                                        variable+=1
                                                    if variable == len(MP):
                                                        cursor.execute('INSERT INTO MATERIA_PRIMA VALUES(NULL,?,?,?,?,?)',(producto.upper(),unidad.upper(),(MP[v][3]*cantidad)/cant,'E',cant),)
                                                        base.commit()
                                                        break
                                            except IndexError:
                                                cursor.execute('INSERT INTO MATERIA_PRIMA VALUES(NULL,?,?,NULL,?,?)',(producto.upper(),unidad.upper(),(MP[v][3]*cantidad)/cant,'E',cant),)
                                                base.commit()
                                            VARIABLE=2
                                            menu111()
                                        break
                            except IndexError:
                                cursor.execute('INSERT INTO RECETA VALUES(NULL,?,?,?,?)',(producto.upper(),materiaprima.upper(),cantidad,MP[v][4]),)
                                base.commit()
                                if tipo.upper() == 'F':
                                    variable=0
                                    cursor.execute('SELECT * FROM PRODUCTO')
                                    PRO=cursor.fetchall()
                                    try:
                                        while True:
                                            if PRO[variable][1] == producto.upper():
                                                break
                                            else:
                                                variable+=1
                                            if variable == len(PRO):
                                                cursor.execute('INSERT INTO PRODUCTO VALUES(NULL,?,?)',(producto.upper(),preciocarta),)
                                                base.commit()
                                                break
                                    except IndexError:
                                        cursor.execute('INSERT INTO PRODUCTO VALUES(NULL,?,?)',(producto.upper(),preciocarta),)
                                        base.commit()
                                    VARIABLE=2
                                    menu111()
                                else:
                                    variable=0
                                    cursor.execute('SELECT * FROM MATERIA_PRIMA')
                                    MP=cursor.fetchall()
                                    try:
                                        while True:
                                            if MP[variable][1] == producto.upper():
                                                cursor.execute('UPDATE MATERIA_PRIMA set preciomateriaprima = (?) WHERE codigomateriaprima = (?)',(MP[variable][3]+((MP[v][3]*cantidad)/MP[variable][5]),MP[variable][0]),)
                                                base.commit()
                                                break
                                            else:
                                                variable+=1
                                            if variable == len(MP):
                                                cursor.execute('INSERT INTO MATERIA_PRIMA VALUES(NULL,?,?,?,?,?)',(producto.upper(),unidad.upper(),(MP[v][3]*cantidad)/cant,'E',cant),)
                                                base.commit()
                                                break
                                    except IndexError:
                                        cursor.execute('INSERT INTO MATERIA_PRIMA VALUES(NULL,?,?,?,?,?)',(producto.upper(),unidad.upper(),(MP[v][3]*cantidad)/cant,'E',cant),)
                                        base.commit()
                                    VARIABLE=2
                                    menu111()
                            break
                        else:
                            v+=1
                        if v == len(MP):
                            # LA MATERIA PRIMA NO EXISTE
                            VARIABLE=4
                            menu1111()
                            break
                except IndexError:
                    VARIABLE=4
                    menu1111()
        except ValueError:
            VARIABLE=1
            menu111()
    def menu111():
        eliminartodo()
        global frame,cuadro0,cuadro1,VARIABLE,VARIABLE1
        frame=Frame(raiz,width='700',height='430',bg='#273746')
        frame.pack()
        cuadro01=StringVar()
        cuadro11=StringVar()

        texto=Label(frame,text='INGRESO DE PRODUCTOS',font=('Radio Canada Big',16),bg='#273746',fg='snow')
        texto.place(relx=0.5,y=60,anchor=tk.CENTER,relwidth=1,relheight=0.10)
        if VARIABLE == 1:
            messagebox.showerror("ERROR", "INGRESO DE DATOS INCORRECTO")
            VARIABLE=0
        else:
            if VARIABLE == 2:
                messagebox.showinfo("FELICIDADES", "DATOS AGREGADOS CORRECTAMENTE")
                VARIABLE=0
            else:
                if VARIABLE == 4:
                    messagebox.showerror("ERROR", "LA MATERIA PRIMA YA FUE INGRESADA")
                    VARIABLE=0
        texto=Label(frame,text='NOMBRE DEL PRODUCTO:',font=('Radio Canada Big',12),bg='#273746',fg='snow')
        texto.place(x=10,y=130,relwidth=0.75,relheight=0.06)
        texto=Label(frame,text=producto.upper(),font=('Radio Canada Big',12),bg='#273746',fg='snow')
        texto.place(x=500,y=130,relwidth=0.20,relheight=0.06)
        texto=Label(frame,text='TIPO DE PRODUCTO:',font=('Radio Canada Big',12),bg='#273746',fg='snow')
        texto.place(x=10,y=170,relwidth=0.75,relheight=0.06)
        if VARIABLE1 == 3:
            if tipo.upper() == 'F':
                texto=Label(frame,text='PRODUCTO FINAL',font=('Radio Canada Big',12),bg='#273746',fg='snow')
                texto.place(x=500,y=170,relwidth=0.20,relheight=0.06)
                texto=Label(frame,text='PRECIO DE CARTA:',font=('Radio Canada Big',12),bg='#273746',fg='snow')
                texto.place(x=10,y=210,relwidth=0.75,relheight=0.06)
                texto=Label(frame,text='${:.2f}'.format(PRO[v][2]),font=('Radio Canada Big',12),bg='#273746',fg='snow')
                texto.place(x=500,y=210,relwidth=0.20,relheight=0.06)
            else:
                texto=Label(frame,text='PRODUCTO BASE',font=('Radio Canada Big',12),bg='#273746',fg='snow')
                texto.place(x=500,y=170,relwidth=0.20,relheight=0.06)
                texto=Label(frame,text='CANTIDAD:',font=('Radio Canada Big',12),bg='#273746',fg='snow')
                texto.place(x=10,y=210,relwidth=0.75,relheight=0.06)
                texto=Label(frame,text=(MP[v][5],MP[v][2]),font=('Radio Canada Big',12),bg='#273746',fg='snow')
                texto.place(x=500,y=210,relwidth=0.20,relheight=0.06)
        else:
            if tipo.upper() == 'F':
                texto=Label(frame,text='PRODUCTO FINAL',font=('Radio Canada Big',12),bg='#273746',fg='snow')
                texto.place(x=500,y=170,relwidth=0.20,relheight=0.06)
                texto=Label(frame,text='PRECIO DE CARTA:',font=('Radio Canada Big',12),bg='#273746',fg='snow')
                texto.place(x=10,y=210,relwidth=0.75,relheight=0.06)
                texto=Label(frame,text='${:.2f}'.format(preciocarta),font=('Radio Canada Big',12),bg='#273746',fg='snow')
                texto.place(x=500,y=210,relwidth=0.20,relheight=0.06)
            else:
                texto=Label(frame,text='PRODUCTO BASE',font=('Radio Canada Big',12),bg='#273746',fg='snow')
                texto.place(x=500,y=170,relwidth=0.20,relheight=0.06)
                texto=Label(frame,text='CANTIDAD:',font=('Radio Canada Big',12),bg='#273746',fg='snow')
                texto.place(x=10,y=210,relwidth=0.75,relheight=0.06)
                texto=Label(frame,text=(cant,unidad.upper()),font=('Radio Canada Big',12),bg='#273746',fg='snow')
                texto.place(x=500,y=210,relwidth=0.20,relheight=0.06)

        texto=Label(frame,text='INGRESE EL NOMBRE DE LA MATERIA PRIMA:',font=('Radio Canada Big',12),bg='#273746',fg='snow')
        texto.place(x=10,y=250,relwidth=0.75,relheight=0.06)
        cuadro0=Entry(frame,textvariable=cuadro01)
        cuadro0.place(x=500,y=250,relheight=0.06)
        texto=Label(frame,text='INGRESE LA CANTIDAD:',font=('Radio Canada Big',12),bg='#273746',fg='snow')
        texto.place(x=10,y=290,relwidth=0.75,relheight=0.06)
        cuadro1=Entry(frame,textvariable=cuadro11)
        cuadro1.place(x=500,y=290,relheight=0.06)
        Button2=Button(frame,text='CONFIRMAR',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:confirmar111())
        Button2.place(x=540,y=360,relwidth=0.17,relheight=0.05)
        Button2=Button(frame,text='VOLVER',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:menu1())
        Button2.place(x=40,y=360,relwidth=0.17,relheight=0.05)
    def confirmar11():
        global VARIABLE,preciocarta,unidad,cant
        if tipo.upper() == 'F':
            try:
                preciocarta=float(cuadro0.get())
                menu111()
            except ValueError:
                VARIABLE=1
                menu11()
        else:
            try:
                unidad=cuadro0.get()
                cant=float(cuadro1.get())
                if unidad.isalpha() == True:
                    menu111()
                else:
                    VARIABLE=1
                    menu11()
            except ValueError:
                VARIABLE=1
                menu11()
    def menu11():
        eliminartodo()
        global frame,cuadro0,cuadro1,VARIABLE
        frame=Frame(raiz,width='700',height='430',bg='#273746')
        frame.pack()
        cuadro01=StringVar()
        cuadro10=StringVar()

        texto=Label(frame,text='INGRESO DE PRODUCTOS',font=('Radio Canada Big',16),bg='#273746',fg='snow')
        texto.place(relx=0.5,y=60,anchor=tk.CENTER,relwidth=1,relheight=0.10)
        if VARIABLE == 1:
            messagebox.showerror("ERROR", "INGRESO DE DATOS INCORRECTO")
            VARIABLE=0
        else:
            if VARIABLE == 2:
                messagebox.showinfo("FELICIDADES", "DATOS AGREGADOS CORRECTAMENTE")
                VARIABLE=0
        texto=Label(frame,text='NOMBRE DEL PRODUCTO:',font=('Radio Canada Big',12),bg='#273746',fg='snow')
        texto.place(x=10,y=130,relwidth=0.75,relheight=0.06)
        texto=Label(frame,text=producto.upper(),font=('Radio Canada Big',12),bg='#273746',fg='snow')
        texto.place(x=500,y=130,relwidth=0.20,relheight=0.06)
        texto=Label(frame,text='TIPO DE PRODUCTO:',font=('Radio Canada Big',12),bg='#273746',fg='snow')
        texto.place(x=10,y=170,relwidth=0.75,relheight=0.06)

        if tipo.upper() == 'F':
            texto=Label(frame,text='PRODUCTO FINAL',font=('Radio Canada Big',12),bg='#273746',fg='snow')
            texto.place(x=500,y=170,relwidth=0.20,relheight=0.06)
            texto=Label(frame,text='INGRESE EL PRECIO DE CARTA:',font=('Radio Canada Big',12),bg='#273746',fg='snow')
            texto.place(x=10,y=210,relwidth=0.75,relheight=0.06)
            cuadro0=Entry(frame,textvariable=cuadro01)
            cuadro0.place(x=500,y=210,relheight=0.06)
        else:
            texto=Label(frame,text='PRODUCTO BASE',font=('Radio Canada Big',12),bg='#273746',fg='snow')
            texto.place(x=500,y=170,relwidth=0.20,relheight=0.06)
            texto=Label(frame,text='INGRESE LA UNIDAD DE MEDIDA:',font=('Radio Canada Big',12),bg='#273746',fg='snow')
            texto.place(x=10,y=210,relwidth=0.75,relheight=0.06)
            cuadro0=Entry(frame,textvariable=cuadro01)
            cuadro0.place(x=500,y=210,relheight=0.06)
            texto=Label(frame,text='INGRESE LA CANTIDAD A REALIZAR:',font=('Radio Canada Big',12),bg='#273746',fg='snow')
            texto.place(x=10,y=250,relwidth=0.75,relheight=0.06)
            cuadro1=Entry(frame,textvariable=cuadro10)
            cuadro1.place(x=500,y=250,relheight=0.06)
        Button2=Button(frame,text='CONFIRMAR',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:confirmar11())
        Button2.place(x=540,y=360,relwidth=0.17,relheight=0.05)
        Button2=Button(frame,text='VOLVER',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:menu1())
        Button2.place(x=40,y=360,relwidth=0.17,relheight=0.05)
    def confirmar1():
        global VARIABLE,producto,tipo,PRO,v,MP,VARIABLE1
        try:
            producto=cuadro0.get()
            if producto == '':
                VARIABLE=1
                menu1()
            else:
                tipo=cuadro1.get()
                if tipo.upper() == 'F':
                    # PRODUCTO FINAL
                    cursor.execute('SELECT * FROM PRODUCTO')
                    PRO=cursor.fetchall()
                    v=0
                    try:
                        while True:
                            if PRO[v][1] == producto.upper():
                                # EL PRODUCTO FINAL EXISTE
                                VARIABLE=0
                                VARIABLE1=3
                                menu111()
                                break
                            else:
                                v+=1
                            if v == len(PRO):
                                # EL PRODUCTO FINAL NO EXISTE
                                VARIABLE=0
                                VARIABLE1=0
                                menu11()
                                break
                    except IndexError:
                        VARIABLE=0
                        menu11()
                else:
                    if tipo.upper() == 'B':
                        # PRODUCTO BASE
                        cursor.execute('SELECT * FROM MATERIA_PRIMA')
                        MP=cursor.fetchall()
                        v=0
                        try:
                            while True:
                                if MP[v][1] == producto.upper():
                                    # EL PRODUCTO BASE EXISTE
                                    VARIABLE=0
                                    VARIABLE1=3
                                    menu111()
                                    break
                                else:
                                    v+=1
                                if v == len(MP):
                                    # EL PRODUCTO BASE NO EXISTE
                                    VARIABLE=0
                                    VARIABLE1=0
                                    menu11()
                                    break
                        except IndexError:
                            VARIABLE=0
                            menu11()
                    else:
                        VARIABLE=1
                        menu1()
        except ValueError:
            VARIABLE=1
            menu1()
    def menu1():
        eliminartodo()
        global frame,cuadro0,cuadro1,VARIABLE
        frame=Frame(raiz,width='700',height='430',bg='#273746')
        frame.pack()
        cuadro01=StringVar()
        cuadro11=StringVar()

        texto=Label(frame,text='INGRESO DE PRODUCTOS',font=('Radio Canada Big',16),bg='#273746',fg='snow')
        texto.place(relx=0.5,y=60,anchor=tk.CENTER,relwidth=1,relheight=0.10)
        if VARIABLE == 1:
            messagebox.showerror("ERROR", "INGRESO DE DATOS INCORRECTO")
            VARIABLE=0
        else:
            if VARIABLE == 2:
                messagebox.showinfo("FELICIDADES", "DATOS AGREGADOS CORRECTAMENTE")
                VARIABLE=0
        texto=Label(frame,text='INGRESE EL NOMBRE DEL PRODUCTO:',font=('Radio Canada Big',12),bg='#273746',fg='snow')
        texto.place(x=10,y=130,relwidth=0.75,relheight=0.06)
        cuadro0=Entry(frame,textvariable=cuadro01)
        cuadro0.place(x=500,y=130,relheight=0.06)
        texto=Label(frame,text='INGRESE B (PRODUCTO BASE) O F (PRODUCTO FINAL):',font=('Radio Canada Big',12),bg='#273746',fg='snow')
        texto.place(x=10,y=170,relwidth=0.75,relheight=0.06)
        cuadro1=Entry(frame,textvariable=cuadro11)
        cuadro1.place(x=500,y=170,relheight=0.06)
        Button2=Button(frame,text='CONFIRMAR',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:confirmar1())
        Button2.place(x=540,y=360,relwidth=0.17,relheight=0.05)
    # INGRESAR DATOS DE MATERIA PRIMA
    def confirmar12():
        global VARIABLE,materiaprima,unidad,precio
        try:
            materiaprima=cuadro0.get()
            unidad=cuadro1.get()
            precio=float(cuadro2.get())
            if unidad.isalpha() == True:
                cursor.execute('SELECT * FROM MATERIA_PRIMA')
                MP=cursor.fetchall()
                v=0
                try:
                    while True:
                        if MP[v][1] == materiaprima.upper():
                            # LA MATERIA PRIMA EXISTE
                            VARIABLE=3
                            menu12()
                            break
                        else:
                            v+=1
                        if v == len(MP):
                            cursor.execute('INSERT INTO MATERIA_PRIMA VALUES(NULL,?,?,?,?,?)',(materiaprima.upper(),unidad.upper(),precio,'C',0),)
                            base.commit()
                            VARIABLE=2
                            menu12()
                            break
                except IndexError:
                    cursor.execute('INSERT INTO MATERIA_PRIMA VALUES(NULL,?,?,?,?,?)',(materiaprima.upper(),unidad.upper(),precio,'C',0),)
                    base.commit()
                    VARIABLE=2
                    menu12()
            else:
                VARIABLE=1
                menu12()
        except ValueError:
            VARIABLE=1
            menu12()
    def menu12():
        eliminartodo()
        global frame,cuadro0,cuadro1,cuadro2,VARIABLE
        frame=Frame(raiz,width='700',height='430',bg='#273746')
        frame.pack()

        cuadro01=StringVar()
        cuadro11=StringVar()
        cuadro10=StringVar()

        texto=Label(frame,text='INGRESO DE MATERIAS PRIMAS',font=('Radio Canada Big',16),bg='#273746',fg='snow')
        texto.place(relx=0.5,y=60,anchor=tk.CENTER,relwidth=1,relheight=0.10)
        texto=Label(frame,text='INGRESE EL NOMBRE DE LA MATERIA PRIMA:',font=('Radio Canada Big',12),bg='#273746',fg='snow')
        texto.place(x=10,y=130,relwidth=0.75,relheight=0.06)
        cuadro0=Entry(frame,textvariable=cuadro01)
        cuadro0.place(x=500,y=130,relheight=0.06)
        texto=Label(frame,text='INGRESE LA UNIDAD DE MEDIDA:',font=('Radio Canada Big',12),bg='#273746',fg='snow')
        texto.place(x=10,y=170,relwidth=0.75,relheight=0.06)
        cuadro1=Entry(frame,textvariable=cuadro11)
        cuadro1.place(x=500,y=170,relheight=0.06)
        texto=Label(frame,text='INGRESE EL PRECIO POR UNIDAD: ',font=('Radio Canada Big',12),bg='#273746',fg='snow')
        texto.place(x=10,y=210,relwidth=0.75,relheight=0.06)
        cuadro2=Entry(frame,textvariable=cuadro10)
        cuadro2.place(x=500,y=210,relheight=0.06)
        Button2=Button(frame,text='CONFIRMAR',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:confirmar12())
        Button2.place(x=540,y=360,relwidth=0.17,relheight=0.05)
        if VARIABLE == 1:
            messagebox.showerror("ERROR", "INGRESO DE DATOS INCORRECTO")
            VARIABLE=0
        else:
            if VARIABLE == 2:
                messagebox.showinfo("FELICIDADES", "DATOS AGREGADOS CORRECTAMENTE")
                VARIABLE=0
            else:
                if VARIABLE == 3:
                    messagebox.showerror("ERROR", "LA MATERIA PRIMA YA FUE INGRESADA")
                    VARIABLE=0
    #################################################################################################################################################################
    #################################################################################################################################################################
    # VER DATOS DE PRODUCTO
    def menu21A():
        eliminartodo()
        menu21()
    def siguiente():
        global CONTADOR
        CONTADOR+=1
        menu21()
    def atras():
        global VER,CONTADOR,f,guarda
        if guarda == 1:
            VER=0
            CONTADOR=0
            guarda=0
            menu21()
        else:
            if CONTADOR > 0:
                if f == 80:
                    VER-=5
                if f == 120:
                    VER-=6
                if f == 160:
                    VER-=7
                if f == 200:
                    VER-=8
                CONTADOR-=1
            else:
                VER=0
            menu21()
    def menu21():
        eliminartodoMENOSUNO()
        global frame,VER,f,guarda,PRO
        frame=Frame(raiz,width='700',height='430',bg='#273746')
        frame.pack()
        guarda=0
        texto=Label(frame,text='CONSULTA DE PRODUCTOS',font=('Radio Canada Big',16),bg='#273746',fg='snow')
        texto.place(relx=0.5,y=60,anchor=tk.CENTER,relwidth=1,relheight=0.10)
                
        cursor.execute('SELECT * FROM RECETA')
        REC=cursor.fetchall()
        cursor.execute('SELECT * FROM MATERIA_PRIMA')
        MP=cursor.fetchall()
        cursor.execute('SELECT * FROM PRODUCTO')
        PRO=cursor.fetchall()
        try:
            f=40
            while True:
                x=0
                v=0
                while True:
                    # BUSCA EL PRODUCTO EN LA TABLA DE RECETAS
                    if PRO[VER][1] == REC[x][1]:
                        z=0
                        while True:
                            # BUSCA LA MATERIA PRIMA DEL PRODUCTO
                            if REC[x][2] == MP[z][1]:
                                v+=(MP[z][3]*REC[x][3])
                                break
                            else:
                                z+=1
                            if z == len(MP):
                                break
                        x+=1
                    else:
                        x+=1
                    if x == len(REC):
                        break
                texto=Label(frame,text=VER+1,font=('Radio Canada Big',10),bg='#273746',fg='snow')
                texto.place(x=10,y=130+f,relwidth=0.15,relheight=0.06)
                texto=Label(frame,text=PRO[VER][1],font=('Radio Canada Big',10),bg='#273746',fg='snow')
                texto.place(x=120,y=130+f,relwidth=0.15,relheight=0.06)
                texto=Label(frame,text='${:.2f}'.format(PRO[VER][2]),font=('Radio Canada Big',10),bg='#273746',fg='snow')
                texto.place(x=230,y=130+f,relwidth=0.15,relheight=0.06)
                texto=Label(frame,text='${:.2f}'.format(v),font=('Radio Canada Big',10),bg='#273746',fg='snow')
                texto.place(x=340,y=130+f,relwidth=0.15,relheight=0.06)
                if (PRO[VER][2]-v) > 0:
                    texto=Label(frame,text='SE GANAN',font=('Radio Canada Big',12),bg='#273746',fg='snow')
                    texto.place(x=450,y=130+f,relwidth=0.15,relheight=0.06)
                    texto=Label(frame,text='${:.2f}'.format(PRO[VER][2]-v),font=('Radio Canada Big',10),bg='#273746',fg='snow')
                    texto.place(x=560,y=130+f,relwidth=0.15,relheight=0.06)
                else:
                    texto=Label(frame,text='SE PIERDEN',font=('Radio Canada Big',12),bg='#273746',fg='snow')
                    texto.place(x=450,y=130+f,relwidth=0.15,relheight=0.06)
                    texto=Label(frame,text='${:.2f}'.format(v-PRO[VER][2]),font=('Radio Canada Big',10),bg='#273746',fg='snow')
                    texto.place(x=560,y=130+f,relwidth=0.15,relheight=0.06)
                VER+=1
                f+=40
                if VER % 4 == 0:
                    break
        except IndexError:
            if VER == 0:
                messagebox.showwarning("ERROR", "NO HAY PRODUCTOS")
                frame.destroy()
            if f == 40:
                guarda=1
                if CONTADOR > 0:
                    messagebox.showwarning("ERROR", "NO HAY MAS PRODUCTOS")
                    atras()
        if VER>0:
            texto=Label(frame,text='CODIGO',font=('Radio Canada Big',12),bg='#273746',fg='snow')
            texto.place(x=10,y=130,relwidth=0.15,relheight=0.06)
            texto=Label(frame,text='NOMBRE',font=('Radio Canada Big',12),bg='#273746',fg='snow')
            texto.place(x=120,y=130,relwidth=0.15,relheight=0.06)
            texto=Label(frame,text='PRECIO',font=('Radio Canada Big',12),bg='#273746',fg='snow')
            texto.place(x=230,y=130,relwidth=0.15,relheight=0.06)
            texto=Label(frame,text='COSTO',font=('Radio Canada Big',12),bg='#273746',fg='snow')
            texto.place(x=340,y=130,relwidth=0.15,relheight=0.06)
        try:
            if PRO[VER][0]==4:
                pass
            Button2=Button(frame,text='SIGUIENTE',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:siguiente())
            Button2.place(x=180,y=360,relwidth=0.17,relheight=0.05)
        except IndexError:
            pass
        if CONTADOR>0:
            Button2=Button(frame,text='ATRAS',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:atras())
            Button2.place(x=40,y=360,relwidth=0.17,relheight=0.05)
    # VER DATOS DE MATERIA PRIMA
    def menu22A():
        eliminartodo()
        menu22()
    def siguiente1():
        global CONTADOR
        CONTADOR+=1
        menu22()
    def atras1():
        global VER,CONTADOR,f,guarda
        if guarda == 1:
            VER=0
            CONTADOR=0
            guarda=0
            menu22()
        else:
            if CONTADOR > 0:
                if f == 80:
                    VER-=5
                if f == 120:
                    VER-=6
                if f == 160:
                    VER-=7
                if f == 200:
                    VER-=8
                CONTADOR-=1
            else:
                VER=0
            menu22()
    def menu22():
        eliminartodoMENOSUNO()
        global frame,VER,f,guarda,MP
        frame=Frame(raiz,width='700',height='430',bg='#273746')
        frame.pack()
        guarda=0
        texto=Label(frame,text='CONSULTA DE MATERIAS PRIMAS',font=('Radio Canada Big',16),bg='#273746',fg='snow')
        texto.place(relx=0.5,y=60,anchor=tk.CENTER,relwidth=1,relheight=0.10)
        
        cursor.execute('SELECT * FROM MATERIA_PRIMA')
        MP=cursor.fetchall()
        try:
            f=40
            while True:
                texto=Label(frame,text=MP[VER][1],font=('Radio Canada Big',10),bg='#273746',fg='snow')
                texto.place(x=140,y=130+f,relwidth=0.2,relheight=0.06)
                texto=Label(frame,text=VER+1,font=('Radio Canada Big',10),bg='#273746',fg='snow')
                texto.place(x=10,y=130+f,relwidth=0.2,relheight=0.06)
                texto=Label(frame,text=MP[VER][2],font=('Radio Canada Big',10),bg='#273746',fg='snow')
                texto.place(x=280,y=130+f,relwidth=0.2,relheight=0.06)
                texto=Label(frame,text='${:.2f}'.format(MP[VER][3]),font=('Radio Canada Big',10),bg='#273746',fg='snow')
                texto.place(x=420,y=130+f,relwidth=0.2,relheight=0.06)
                if MP[VER][4] == 'C':
                    texto=Label(frame,text='COMPRADA',font=('Radio Canada Big',10),bg='#273746',fg='snow')
                    texto.place(x=550,y=130+f,relwidth=0.2,relheight=0.06)
                else:
                    texto=Label(frame,text='ELABORADA',font=('Radio Canada Big',10),bg='#273746',fg='snow')
                    texto.place(x=550,y=130+f,relwidth=0.2,relheight=0.06)
                VER+=1
                f+=40
                if VER % 4 == 0:
                    break
        except IndexError:
            if VER == 0:
                messagebox.showwarning("ERROR", "NO HAY MATERIAS PRIMAS")
                frame.destroy()
            if f == 40:
                guarda=1
                if CONTADOR > 0:
                    messagebox.showwarning("ERROR", "NO HAY MAS MATERIAS PRIMAS")
                    atras1()
        if VER>0:
            texto=Label(frame,text='CODIGO',font=('Radio Canada Big',12),bg='#273746',fg='snow')
            texto.place(x=10,y=130,relwidth=0.2,relheight=0.06)
            texto=Label(frame,text='NOMBRE',font=('Radio Canada Big',12),bg='#273746',fg='snow')
            texto.place(x=140,y=130,relwidth=0.2,relheight=0.06)
            texto=Label(frame,text='UNIDAD',font=('Radio Canada Big',12),bg='#273746',fg='snow')
            texto.place(x=280,y=130,relwidth=0.2,relheight=0.06)
            texto=Label(frame,text='PRECIO',font=('Radio Canada Big',12),bg='#273746',fg='snow')
            texto.place(x=420,y=130,relwidth=0.2,relheight=0.06)
            texto=Label(frame,text='TIPO',font=('Radio Canada Big',12),bg='#273746',fg='snow')
            texto.place(x=550,y=130,relwidth=0.2,relheight=0.06)
        try:
            if MP[VER][0]==4:
                pass
            Button2=Button(frame,text='SIGUIENTE',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:siguiente1())
            Button2.place(x=180,y=360,relwidth=0.17,relheight=0.05)
        except IndexError:
            pass
        if CONTADOR>0:
            Button2=Button(frame,text='ATRAS',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:atras1())
            Button2.place(x=40,y=360,relwidth=0.17,relheight=0.05)
    #################################################################################################################################################################
    #################################################################################################################################################################
    # MODIFICAR DATOS DE PRODUCTO
    def menu31A():
        eliminartodo()
        menu31()
    def siguienteMP():
        global CONTADOR
        CONTADOR+=1
        menu31()
    def atrasMP():
        global VER,CONTADOR,f,guarda,x
        if guarda == 1:
            CONTADOR=0
            VER=0
            guarda=0
            menu31()
        else:
            if CONTADOR > 0:
                if x == 0:
                    if f == 80:
                        VER-=7
                    if f == 120:
                        VER-=8
                    if f == 160:
                        VER-=9
                if x == 350:
                    if f == 40:
                        VER-=9
                    if f == 80:
                        VER-=10
                    if f == 120:
                        VER-=11
                    if f == 160:
                        VER-=12
                CONTADOR-=1
            else:
                VER=0
            menu31()
    def confirmar311111():
        global VARIABLE,cantidad,REC,PRO,Y
        try:
            cantidad=float(cuadro0.get())
            cursor.execute('UPDATE RECETA SET cantidadmateriaprima = (?) WHERE nombrereceta = (?) AND nombremateriaprimareceta = (?)',(cantidad,PRO[v][1],REC[Y][2]))
            base.commit()
            VARIABLE=2
            menu311()
        except ValueError:
            VARIABLE=1
            Mcantidades()
    def menu3111():
        eliminartodo()
        global frame,cuadro0,VARIABLE,REC,PRO,Y
        frame=Frame(raiz,width='700',height='430',bg='#273746')
        frame.pack()

        cuadro01=StringVar()

        texto=Label(frame,text='MODIFICAR PRODUCTOS',font=('Radio Canada Big',16),bg='#273746',fg='snow')
        texto.place(relx=0.5,y=60,anchor=tk.CENTER,relwidth=1,relheight=0.10)
        texto=Label(frame,text='INGRESE LA CANTIDAD NUEVA:',font=('Radio Canada Big',12),bg='#273746',fg='snow')
        texto.place(x=10,y=130,relwidth=0.75,relheight=0.06)
        cuadro0=Entry(frame,textvariable=cuadro01)
        cuadro0.place(x=500,y=130,relheight=0.06)
        Button2=Button(frame,text='CONFIRMAR',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:confirmar311111())
        Button2.place(x=540,y=360,relwidth=0.17,relheight=0.05)
        Button2=Button(frame,text='VOLVER',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:menu311())
        Button2.place(x=40,y=360,relwidth=0.17,relheight=0.05)
        if VARIABLE == 1:
            messagebox.showerror("ERROR", "INGRESO DE DATOS INCORRECTO")
            VARIABLE=0
    def confirmar31111():
        global VARIABLE,opcion,REC,PRO,Y
        cursor.execute('SELECT * FROM RECETA')
        REC=cursor.fetchall()
        cursor.execute('SELECT * FROM PRODUCTO')
        PRO=cursor.fetchall()
        Y=0
        v=0
        bandera=0
        try:
            opcion=cuadro0.get()
            if opcion == '':
                VARIABLE=1
                Mcantidades()
            else:
                while True:
                    if PRO[v][0] == codigo:
                        while True:
                            if REC[Y][1] == PRO[v][1]:
                                if opcion.upper() == REC[Y][2]:
                                    VARIABLE=0
                                    bandera = 1
                                    menu3111()
                                    break
                                else:
                                    Y+=1
                                    break
                            else:
                                Y+=1
                        if bandera == 1:
                            break
                    else:
                        v+=1
        except ValueError:
            VARIABLE=1
            Mcantidades()
    def Mcantidades():
        eliminartodo()
        global frame,cuadro0,VARIABLE,Y
        frame=Frame(raiz,width='700',height='430',bg='#273746')
        frame.pack()

        cursor.execute('SELECT * FROM PRODUCTO')
        PRO=cursor.fetchall()
        cursor.execute('SELECT * FROM RECETA')
        REC=cursor.fetchall()
        Button2=Button(frame,text='SIGUIENTE',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:Mcantidades())
        Button2.place(x=180,y=360,relwidth=0.17,relheight=0.05)
        try:
            while True:
                if REC[Y][1] == PRO[v][1]:
                    texto=Label(frame,text=REC[Y][2],font=('Radio Canada Big',10),bg='#273746',fg='snow')
                    texto.place(x=120,y=170,relwidth=0.25,relheight=0.06)
                    texto=Label(frame,text='CANTIDAD',font=('Radio Canada Big',10),bg='#273746',fg='snow')
                    texto.place(x=120,y=210,relwidth=0.25,relheight=0.06)
                    texto=Label(frame,text=REC[Y][3],font=('Radio Canada Big',10),bg='#273746',fg='snow')
                    texto.place(x=120,y=250,relwidth=0.25,relheight=0.06)
                    Y+=1
                    if Y>=1:
                        break
                else:
                    Y+=1
        except  IndexError:
            messagebox.showwarning("ERROR", "NO HAY MAS MATERIAS PRIMAS")
            Y=0
            Mcantidades()

        cuadro01=StringVar()

        texto=Label(frame,text='MODIFICAR PRODUCTOS',font=('Radio Canada Big',16),bg='#273746',fg='snow')
        texto.place(relx=0.5,y=60,anchor=tk.CENTER,relwidth=1,relheight=0.10)
        texto=Label(frame,text='INGRESE EL NOMBRE DE LA MATERIA PRIMA:',font=('Radio Canada Big',12),bg='#273746',fg='snow')
        texto.place(x=10,y=130,relwidth=0.75,relheight=0.06)
        cuadro0=Entry(frame,textvariable=cuadro01)
        cuadro0.place(x=500,y=130,relheight=0.06)
        Button2=Button(frame,text='CONFIRMAR',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:confirmar31111())
        Button2.place(x=540,y=360,relwidth=0.17,relheight=0.05)
        Button2=Button(frame,text='VOLVER',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:menu311())
        Button2.place(x=40,y=360,relwidth=0.17,relheight=0.05)
        if VARIABLE == 1:
            messagebox.showerror("ERROR", "INGRESO DE DATOS INCORRECTO")
            VARIABLE=0
    def confirmar3111():
        global VARIABLE
        try:
            precio=float(cuadro0.get())
            cursor.execute('UPDATE PRODUCTO SET precioproducto = (?) WHERE codigoproducto = (?)',(precio,codigo))
            base.commit()
            VARIABLE=2
            menu311()
        except ValueError:
            VARIABLE=1
            Mpreciodecarta()  
    def Mpreciodecarta():
        eliminartodo()
        global frame,cuadro0,VARIABLE
        frame=Frame(raiz,width='700',height='430',bg='#273746')
        frame.pack()

        cuadro01=StringVar()

        texto=Label(frame,text='MODIFICAR PRODUCTOS',font=('Radio Canada Big',16),bg='#273746',fg='snow')
        texto.place(relx=0.5,y=60,anchor=tk.CENTER,relwidth=1,relheight=0.10)
        texto=Label(frame,text='INGRESE EL PRECIO DE CARTA NUEVO:',font=('Radio Canada Big',12),bg='#273746',fg='snow')
        texto.place(x=10,y=130,relwidth=0.75,relheight=0.06)
        cuadro0=Entry(frame,textvariable=cuadro01)
        cuadro0.place(x=500,y=130,relheight=0.06)
        Button2=Button(frame,text='CONFIRMAR',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:confirmar3111())
        Button2.place(x=540,y=360,relwidth=0.17,relheight=0.05)
        Button2=Button(frame,text='VOLVER',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:menu311())
        Button2.place(x=40,y=360,relwidth=0.17,relheight=0.05)
        if VARIABLE == 1:
            messagebox.showerror("ERROR", "INGRESO DE DATOS INCORRECTO")
            VARIABLE=0
    def confirmar311():
        global VARIABLE,PRO,v
        try:
            producto=cuadro0.get()
            if producto == '':
                VARIABLE=1
                Mnombre()
            else:
                cursor.execute('UPDATE RECETA SET nombrereceta = (?) WHERE nombrereceta = (?)',(producto.upper(),PRO[v][1]))
                base.commit()
                cursor.execute('UPDATE PRODUCTO SET nombreproducto = (?) WHERE codigoproducto = (?)',(producto.upper(),codigo))
                base.commit()
                VARIABLE=2
                menu311()
        except ValueError:
            VARIABLE=1
            Mnombre() 
    def Mnombre():
        eliminartodo()
        global frame,cuadro0,VARIABLE
        frame=Frame(raiz,width='700',height='430',bg='#273746')
        frame.pack()

        cuadro01=StringVar()

        texto=Label(frame,text='MODIFICAR PRODUCTOS',font=('Radio Canada Big',16),bg='#273746',fg='snow')
        texto.place(relx=0.5,y=60,anchor=tk.CENTER,relwidth=1,relheight=0.10)
        texto=Label(frame,text='INGRESE EL NOMBRE NUEVO:',font=('Radio Canada Big',12),bg='#273746',fg='snow')
        texto.place(x=10,y=130,relwidth=0.75,relheight=0.06)
        cuadro0=Entry(frame,textvariable=cuadro01)
        cuadro0.place(x=500,y=130,relheight=0.06)
        Button2=Button(frame,text='CONFIRMAR',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:confirmar311())
        Button2.place(x=540,y=360,relwidth=0.17,relheight=0.05)
        Button2=Button(frame,text='VOLVER',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:menu311())
        Button2.place(x=40,y=360,relwidth=0.17,relheight=0.05)
        if VARIABLE == 1:
            messagebox.showerror("ERROR", "INGRESO DE DATOS INCORRECTO")
            VARIABLE=0
    def menu311():
        eliminartodo()
        global frame,cuadro0,VARIABLE,Y
        frame=Frame(raiz,width='700',height='430',bg='#273746')
        frame.pack()
        Y=0
        if VARIABLE == 2:
            messagebox.showinfo("FELICIDADES", "DATOS MODIFICADOS CORRECTAMENTE")
            VARIABLE=0
        cursor.execute('SELECT * FROM PRODUCTO')
        PRO=cursor.fetchall()
        texto=Label(frame,text='MODIFICAR PRODUCTOS',font=('Radio Canada Big',16),bg='#273746',fg='snow')
        texto.place(relx=0.5,y=60,anchor=tk.CENTER,relwidth=1,relheight=0.10)
        texto=Label(frame,text='PRODUCTO NUMERO:',font=('Radio Canada Big',12),bg='#273746',fg='snow')
        texto.place(x=10,y=130,relwidth=0.75,relheight=0.06)
        texto=Label(frame,text=codMP,font=('Radio Canada Big',10),bg='#273746',fg='snow')
        texto.place(x=500,y=130,relwidth=0.25,relheight=0.06)
        Button2=Button(frame,text='MODIFICAR NOMBRE',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:Mnombre())
        Button2.place(x=120,y=170,relwidth=0.5,relheight=0.05)
        texto=Label(frame,text=PRO[v][1],font=('Radio Canada Big',10),bg='#273746',fg='snow')
        texto.place(x=500,y=170,relwidth=0.25,relheight=0.06)
        Button2=Button(frame,text='MODIFICAR PRECIO DE CARTA',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:Mpreciodecarta())
        Button2.place(x=120,y=210,relwidth=0.5,relheight=0.05)
        texto=Label(frame,text=PRO[v][2],font=('Radio Canada Big',10),bg='#273746',fg='snow')
        texto.place(x=500,y=210,relwidth=0.25,relheight=0.06)
        Button2=Button(frame,text='MODIFICAR CANTIDADES DE MATERIA PRIMA',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:Mcantidades())
        Button2.place(x=120,y=250,relwidth=0.5,relheight=0.05)
        Button2=Button(frame,text='VOLVER',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:menu31A())
        Button2.place(x=40,y=360,relwidth=0.17,relheight=0.05)
    def confirmar31():
        global codigo,VARIABLE,PRO,v,CONTADOR,VER,guarda,codMP
        try:
            codMP=int(cuadro0.get())
            #try:
            v=0
            cursor.execute('SELECT * FROM PRODUCTO')
            PRO=cursor.fetchall()
            codigo=PRO[codMP-1][0]
            VARIABLE=0
            while True:
                if codigo == PRO[v][0]:
                    VARIABLE=0
                    menu311()
                    break
                else:
                    v+=1
                if v == len(PRO):
                    VARIABLE=1
                    menu31()
                    break
            #except IndexError:
            #        VARIABLE=1
            #        menu31()
        except ValueError:
            VARIABLE=1
            menu31()
    def menu31():
        eliminartodo()
        global frame,cuadro0,VARIABLE,VER,f,guarda,x,PRO
        frame=Frame(raiz,width='700',height='430',bg='#273746')
        frame.pack()
        guarda=0

        cuadro01=StringVar()

        texto=Label(frame,text='MODIFICAR PRODUCTOS',font=('Radio Canada Big',16),bg='#273746',fg='snow')
        texto.place(relx=0.5,y=60,anchor=tk.CENTER,relwidth=1,relheight=0.10)
        
        if VARIABLE == 1:
            messagebox.showerror("ERROR", "INGRESO DE DATOS INCORRECTO")
            VARIABLE=0
            guarda=1
            atrasMP()
        else:
            if VARIABLE == 2:
                messagebox.showinfo("FELICIDADES", "DATOS MODIFICADOS CORRECTAMENTE")
                VARIABLE=0
                guarda=1
                atrasMP()
            else:
                cursor.execute('SELECT * FROM RECETA')
                REC=cursor.fetchall()
                cursor.execute('SELECT * FROM MATERIA_PRIMA')
                MP=cursor.fetchall()
                cursor.execute('SELECT * FROM PRODUCTO')
                PRO=cursor.fetchall()
                try:
                    x=0
                    f=40
                    while True:
                        x=0
                        v=0
                        while True:
                            # BUSCA EL PRODUCTO EN LA TABLA DE RECETAS
                            if PRO[VER][1] == REC[x][1]:
                                z=0
                                while True:
                                    # BUSCA LA MATERIA PRIMA DEL PRODUCTO
                                    if REC[x][2] == MP[z][1]:
                                        # ES COMPRADA
                                        if MP[z][4] == 'C':
                                            v+=(MP[z][3]*REC[x][3])
                                            break
                                        else:
                                            w=0
                                            # ES ELABORADA ASI QUE BUSCA LA MATERIA PRIMA EN LA TABLA DE RECETAS
                                            while True:
                                                if MP[z][1] == REC[w][1]:
                                                    u=0
                                                    t=0
                                                    while True:
                                                        # BUSCA LA MATERIA PRIMA DE LA MPE
                                                        if REC[w][2] == MP[u][1]:
                                                            while True:
                                                                if MP[u][1]==REC[t][2]:
                                                                    break
                                                                else:
                                                                    t+=1
                                                                if t == len(REC):
                                                                    break
                                                            v+=(REC[x][3]*(MP[u][3]*REC[w][3])/REC[t][3])
                                                            break
                                                        else:
                                                            u+=1
                                                        if u == len(MP):
                                                            break
                                                    w+=1
                                                else:
                                                    w+=1
                                                if w == len(REC):
                                                    break
                                        break
                                    else:
                                        z+=1
                                    if z == len(MP):
                                        break
                                x+=1
                            else:
                                x+=1
                            if x == len(REC):
                                break
                        texto=Label(frame,text=VER+1,font=('Radio Canada Big',10),bg='#273746',fg='snow')
                        texto.place(x=10+x,y=170+f,relwidth=0.15,relheight=0.06)
                        texto=Label(frame,text=PRO[VER][1],font=('Radio Canada Big',10),bg='#273746',fg='snow')
                        texto.place(x=120+x,y=170+f,relwidth=0.15,relheight=0.06)
                        VER+=1
                        f+=40
                        if VER % 6 == 0:
                            break
                        if VER % 3 == 0:
                            f=40
                            x=350
                            continue
                except IndexError:
                    if VER == 0:
                            messagebox.showwarning("ERROR", "NO HAY PRODUCTOS")
                            frame.destroy()
                    if f == 40 and x == 0:
                        guarda=1
                        if CONTADOR > 0:
                            messagebox.showwarning("ERROR", "NO HAY MAS PRODUCTOS")
                            atrasMP()
        if VER>0:
            texto=Label(frame,text='INGRESE EL CODIGO DEL PRODUCTO:',font=('Radio Canada Big',12),bg='#273746',fg='snow')
            texto.place(x=10,y=130,relwidth=0.75,relheight=0.06)
            cuadro0=Entry(frame,textvariable=cuadro01)
            cuadro0.place(x=500,y=130,relheight=0.06)
            Button2=Button(frame,text='CONFIRMAR',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:confirmar31())
            Button2.place(x=540,y=360,relwidth=0.17,relheight=0.05)
        try:
            if PRO[VER][0]==4:
                pass
            Button2=Button(frame,text='SIGUIENTE',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:siguienteMP())
            Button2.place(x=180,y=360,relwidth=0.17,relheight=0.05)
        except IndexError:
            pass
        if CONTADOR>0:
            Button2=Button(frame,text='ATRAS',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:atrasMP())
            Button2.place(x=40,y=360,relwidth=0.17,relheight=0.05)
    # MODIFICAR DATOS DE MATERIA PRIMA
    def menu32A():
        eliminartodo()
        menu32()
    def siguienteMMP():
        global CONTADOR
        CONTADOR+=1
        menu32()
    def atrasMMP():
        global VER,CONTADOR,f,guarda,x
        if guarda == 1:
            CONTADOR=0
            VER=0
            guarda=0
            menu32()
        else:
            if CONTADOR > 0:
                if x == 0:
                    if f == 80:
                        VER-=7
                    if f == 120:
                        VER-=8
                    if f == 160:
                        VER-=9
                if x == 350:
                    if f == 40:
                        VER-=9
                    if f == 80:
                        VER-=10
                    if f == 120:
                        VER-=11
                    if f == 160:
                        VER-=12
                CONTADOR-=1
            else:
                VER=0
            menu32()
    def confirmarMP1():
        global VARIABLE,cantidad,REC,MP,Y
        try:
            cantidad=float(cuadro0.get())
            cursor.execute('UPDATE RECETA SET cantidadmateriaprima = (?) WHERE nombrereceta = (?) AND nombremateriaprimareceta = (?)',(cantidad,MP[v][1],REC[Y][2]))
            base.commit()
            VARIABLE=2
            menu322()
        except ValueError:
            VARIABLE=1
            MPcantidades()
    def menuMP():
        eliminartodo()
        global frame,cuadro0,VARIABLE,REC,PRO,Y
        frame=Frame(raiz,width='700',height='430',bg='#273746')
        frame.pack()

        cuadro01=StringVar()

        texto=Label(frame,text='MODIFICAR MATERIAS PRIMAS',font=('Radio Canada Big',16),bg='#273746',fg='snow')
        texto.place(relx=0.5,y=60,anchor=tk.CENTER,relwidth=1,relheight=0.10)
        texto=Label(frame,text='INGRESE LA CANTIDAD NUEVA:',font=('Radio Canada Big',12),bg='#273746',fg='snow')
        texto.place(x=10,y=130,relwidth=0.75,relheight=0.06)
        cuadro0=Entry(frame,textvariable=cuadro01)
        cuadro0.place(x=500,y=130,relheight=0.06)
        Button2=Button(frame,text='CONFIRMAR',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:confirmarMP1())
        Button2.place(x=540,y=360,relwidth=0.17,relheight=0.05)
        Button2=Button(frame,text='VOLVER',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:menu322())
        Button2.place(x=40,y=360,relwidth=0.17,relheight=0.05)
        if VARIABLE == 1:
            messagebox.showerror("ERROR", "INGRESO DE DATOS INCORRECTO")
            VARIABLE=0
    def confirmarMP():
        global VARIABLE,opcion,REC,MP,Y
        cursor.execute('SELECT * FROM RECETA')
        REC=cursor.fetchall()
        cursor.execute('SELECT * FROM MATERIA_PRIMA')
        MP=cursor.fetchall()
        Y=0
        v=0
        bandera=0
        try:
            opcion=cuadro0.get()
            if opcion == '':
                VARIABLE=1
                MPcantidades()
            else:
                while True:
                    if MP[v][0] == codigo:
                        while True:
                            if REC[Y][1] == MP[v][1]:
                                if opcion.upper() == REC[Y][2]:
                                    VARIABLE=0
                                    bandera = 1
                                    menuMP()
                                    break
                                else:
                                    Y+=1
                                    break
                            else:
                                Y+=1
                        if bandera == 1:
                            break
                    else:
                        v+=1
        except ValueError:
            VARIABLE=1
            MPcantidades()
    def MPcantidades():
        eliminartodo()
        global frame,cuadro0,VARIABLE,Y
        frame=Frame(raiz,width='700',height='430',bg='#273746')
        frame.pack()

        cursor.execute('SELECT * FROM MATERIA_PRIMA')
        MP=cursor.fetchall()
        cursor.execute('SELECT * FROM RECETA')
        REC=cursor.fetchall()
        Button2=Button(frame,text='SIGUIENTE',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:MPcantidades())
        Button2.place(x=180,y=360,relwidth=0.17,relheight=0.05)
        try:
            while True:
                if REC[Y][1] == MP[v][1]:
                    texto=Label(frame,text=REC[Y][2],font=('Radio Canada Big',10),bg='#273746',fg='snow')
                    texto.place(x=120,y=170,relwidth=0.25,relheight=0.06)
                    texto=Label(frame,text='CANTIDAD',font=('Radio Canada Big',10),bg='#273746',fg='snow')
                    texto.place(x=120,y=210,relwidth=0.25,relheight=0.06)
                    texto=Label(frame,text=REC[Y][3],font=('Radio Canada Big',10),bg='#273746',fg='snow')
                    texto.place(x=120,y=250,relwidth=0.25,relheight=0.06)
                    Y+=1
                    if Y>=1:
                        break
                else:
                    Y+=1
        except  IndexError:
            messagebox.showwarning("ERROR", "NO HAY MAS MATERIAS PRIMAS")
            Y=0
            MPcantidades()

        cuadro01=StringVar()

        texto=Label(frame,text='MODIFICAR MATERIAS PRIMAS',font=('Radio Canada Big',16),bg='#273746',fg='snow')
        texto.place(relx=0.5,y=60,anchor=tk.CENTER,relwidth=1,relheight=0.10)
        texto=Label(frame,text='INGRESE EL NOMBRE DE LA MATERIA PRIMA:',font=('Radio Canada Big',12),bg='#273746',fg='snow')
        texto.place(x=10,y=130,relwidth=0.75,relheight=0.06)
        cuadro0=Entry(frame,textvariable=cuadro01)
        cuadro0.place(x=500,y=130,relheight=0.06)
        Button2=Button(frame,text='CONFIRMAR',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:confirmarMP())
        Button2.place(x=540,y=360,relwidth=0.17,relheight=0.05)
        Button2=Button(frame,text='VOLVER',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:menu322())
        Button2.place(x=40,y=360,relwidth=0.17,relheight=0.05)
        if VARIABLE == 1:
            messagebox.showerror("ERROR", "INGRESO DE DATOS INCORRECTO")
            VARIABLE=0
    def confirmar3222222():
        global VARIABLE,cant
        try:
            cant=float(cuadro0.get())
            cursor.execute('UPDATE MATERIA_PRIMA SET cantidadmateriaprima = (?) WHERE codigomateriaprima = (?)',(cant,codigo))
            base.commit()
            VARIABLE=2
            menu322()
        except ValueError:
            VARIABLE=1
            MPcantidad()
    def MPcantidad():
        eliminartodo()
        global frame,cuadro0,VARIABLE
        frame=Frame(raiz,width='700',height='430',bg='#273746')
        frame.pack()
        cuadro01=StringVar()

        texto=Label(frame,text='MODIFICAR MATERIAS PRIMAS',font=('Radio Canada Big',16),bg='#273746',fg='snow')
        texto.place(relx=0.5,y=60,anchor=tk.CENTER,relwidth=1,relheight=0.10)
        texto=Label(frame,text='INGRESE LA CANTIDAD NUEVA:',font=('Radio Canada Big',12),bg='#273746',fg='snow')
        texto.place(x=10,y=130,relwidth=0.75,relheight=0.06)
        cuadro0=Entry(frame,textvariable=cuadro01)
        cuadro0.place(x=500,y=130,relheight=0.06)
        Button2=Button(frame,text='CONFIRMAR',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:confirmar3222222())
        Button2.place(x=540,y=360,relwidth=0.17,relheight=0.05)
        Button2=Button(frame,text='VOLVER',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:menu322())
        Button2.place(x=40,y=360,relwidth=0.17,relheight=0.05)
        if VARIABLE == 1:
            messagebox.showerror("ERROR", "INGRESO DE DATOS INCORRECTO")
            VARIABLE=0
    def confirmar322222():
        global VARIABLE,precio
        try:
            precio=float(cuadro0.get())
            cursor.execute('SELECT * FROM MATERIA_PRIMA')
            MP=cursor.fetchall()
            cursor.execute('SELECT * FROM RECETA')
            REC=cursor.fetchall()
            v=0
            while True:
                if codigo == MP[v][0]:
                    w=0
                    while True:
                        if MP[v][1] == REC[w][2]:
                            p=0
                            while True:
                                if REC[w][1] == MP[p][1]:
                                    cursor.execute('UPDATE MATERIA_PRIMA SET preciomateriaprima = (?) WHERE codigomateriaprima = (?)',(MP[p][3]-(MP[v][3]*REC[w][3]/MP[p][5]),MP[p][0]))
                                    base.commit()
                                    break
                                else:
                                    p+=1
                                if p == len(MP):
                                    break
                            w+=1
                        else:
                            w+=1
                        if w == len(REC):
                            break
                    break
                else:
                    v+=1
                if v == len(MP):
                    break
            cursor.execute('UPDATE MATERIA_PRIMA SET preciomateriaprima = (?) WHERE codigomateriaprima = (?)',(precio,codigo))
            base.commit()
            cursor.execute('SELECT * FROM MATERIA_PRIMA')
            MP=cursor.fetchall()
            cursor.execute('SELECT * FROM RECETA')
            REC=cursor.fetchall()
            v=0
            while True:
                if codigo == MP[v][0]:
                    w=0
                    while True:
                        if MP[v][1] == REC[w][2]:
                            p=0
                            while True:
                                if REC[w][1] == MP[p][1]:
                                    cursor.execute('UPDATE MATERIA_PRIMA SET preciomateriaprima = (?) WHERE codigomateriaprima = (?)',(MP[p][3]+(MP[v][3]*REC[w][3]/MP[p][5]),MP[p][0]))
                                    base.commit()
                                    break
                                else:
                                    p+=1
                                if p == len(MP):
                                    break
                            w+=1
                        else:
                            w+=1
                        if w == len(REC):
                            break
                    break
                else:
                    v+=1
                if v == len(MP):
                    break
            VARIABLE=2
            menu322()
        except ValueError:
            VARIABLE=1
            MPprecio()
    def MPprecio():
        eliminartodo()
        global frame,cuadro0,VARIABLE
        frame=Frame(raiz,width='700',height='430',bg='#273746')
        frame.pack()

        cuadro01=StringVar()

        texto=Label(frame,text='MODIFICAR MATERIAS PRIMAS',font=('Radio Canada Big',16),bg='#273746',fg='snow')
        texto.place(relx=0.5,y=60,anchor=tk.CENTER,relwidth=1,relheight=0.10)
        texto=Label(frame,text='INGRESE EL PRECIO NUEVO:',font=('Radio Canada Big',12),bg='#273746',fg='snow')
        texto.place(x=10,y=130,relwidth=0.75,relheight=0.06)
        cuadro0=Entry(frame,textvariable=cuadro01)
        cuadro0.place(x=500,y=130,relheight=0.06)
        Button2=Button(frame,text='CONFIRMAR',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:confirmar322222())
        Button2.place(x=540,y=360,relwidth=0.17,relheight=0.05)
        Button2=Button(frame,text='VOLVER',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:menu322())
        Button2.place(x=40,y=360,relwidth=0.17,relheight=0.05)
        if VARIABLE == 1:
            messagebox.showerror("ERROR", "INGRESO DE DATOS INCORRECTO")
            VARIABLE=0
    def confirmar3222():
        global VARIABLE,unidad
        try:
            unidad=cuadro0.get()
            if unidad.isalpha() == True:
                cursor.execute('UPDATE MATERIA_PRIMA SET unidadmateriaprima = (?) WHERE codigomateriaprima = (?)',(unidad.upper(),codigo))
                base.commit()
                VARIABLE=2
                menu322()
            else:
                VARIABLE=1
                MPunidaddemedida()
        except ValueError:
            VARIABLE=1
            MPunidaddemedida()  
    def MPunidaddemedida():
        eliminartodo()
        global frame,cuadro0,VARIABLE
        frame=Frame(raiz,width='700',height='430',bg='#273746')
        frame.pack()

        cuadro01=StringVar()

        texto=Label(frame,text='MODIFICAR MATERIAS PRIMAS',font=('Radio Canada Big',16),bg='#273746',fg='snow')
        texto.place(relx=0.5,y=60,anchor=tk.CENTER,relwidth=1,relheight=0.10)
        texto=Label(frame,text='INGRESE LA UNIDAD DE MEDIDA NUEVA:',font=('Radio Canada Big',12),bg='#273746',fg='snow')
        texto.place(x=10,y=130,relwidth=0.75,relheight=0.06)
        cuadro0=Entry(frame,textvariable=cuadro01)
        cuadro0.place(x=500,y=130,relheight=0.06)
        Button2=Button(frame,text='CONFIRMAR',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:confirmar3222())
        Button2.place(x=540,y=360,relwidth=0.17,relheight=0.05)
        Button2=Button(frame,text='VOLVER',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:menu322())
        Button2.place(x=40,y=360,relwidth=0.17,relheight=0.05)
        if VARIABLE == 1:
            messagebox.showerror("ERROR", "INGRESO DE DATOS INCORRECTO")
            VARIABLE=0
    def confirmar322():
        global VARIABLE,materiaprima
        try:
            materiaprima=cuadro0.get()
            if materiaprima == '':
                VARIABLE=1
                MPnombre()
            else:
                cursor.execute('UPDATE RECETA SET nombrereceta = (?) WHERE nombrereceta = (?)',(materiaprima.upper(),MP[v][1]))
                base.commit()
                cursor.execute('UPDATE RECETA SET nombremateriaprimareceta = (?) WHERE nombremateriaprimareceta = (?)',(materiaprima.upper(),MP[v][1]))
                base.commit()
                cursor.execute('UPDATE MATERIA_PRIMA SET nombremateriaprima = (?) WHERE codigomateriaprima = (?)',(materiaprima.upper(),codigo))
                base.commit()
                VARIABLE=2
                menu322()
        except ValueError:
            VARIABLE=1
            MPnombre()  
    def MPnombre():
        eliminartodo()
        global frame,cuadro0,VARIABLE
        frame=Frame(raiz,width='700',height='430',bg='#273746')
        frame.pack()

        cuadro01=StringVar()

        texto=Label(frame,text='MODIFICAR MATERIAS PRIMAS',font=('Radio Canada Big',16),bg='#273746',fg='snow')
        texto.place(relx=0.5,y=60,anchor=tk.CENTER,relwidth=1,relheight=0.10)
        texto=Label(frame,text='INGRESE EL NOMBRE NUEVO:',font=('Radio Canada Big',12),bg='#273746',fg='snow')
        texto.place(x=10,y=130,relwidth=0.75,relheight=0.06)
        cuadro0=Entry(frame,textvariable=cuadro01)
        cuadro0.place(x=500,y=130,relheight=0.06)
        Button2=Button(frame,text='CONFIRMAR',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:confirmar322())
        Button2.place(x=540,y=360,relwidth=0.17,relheight=0.05)
        Button2=Button(frame,text='VOLVER',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:menu322())
        Button2.place(x=40,y=360,relwidth=0.17,relheight=0.05)
        if VARIABLE == 1:
            messagebox.showerror("ERROR", "INGRESO DE DATOS INCORRECTO")
            VARIABLE=0
    def menu322():
        eliminartodo()
        global frame,cuadro0,VARIABLE,Y
        Y=0
        frame=Frame(raiz,width='700',height='430',bg='#273746')
        frame.pack()
        cursor.execute('SELECT * FROM MATERIA_PRIMA')
        MP=cursor.fetchall()
        texto=Label(frame,text='MODIFICAR MATERIAS PRIMAS',font=('Radio Canada Big',16),bg='#273746',fg='snow')
        texto.place(relx=0.5,y=60,anchor=tk.CENTER,relwidth=1,relheight=0.10)
        texto=Label(frame,text='MATERIA PRIMA NUMERO:',font=('Radio Canada Big',12),bg='#273746',fg='snow')
        texto.place(x=10,y=130,relwidth=0.75,relheight=0.06)
        texto=Label(frame,text=codMMP,font=('Radio Canada Big',10),bg='#273746',fg='snow')
        texto.place(x=500,y=130,relwidth=0.25,relheight=0.06)
        Button2=Button(frame,text='MODIFICAR NOMBRE',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:MPnombre())
        Button2.place(x=120,y=170,relwidth=0.5,relheight=0.05)
        texto=Label(frame,text=MP[v][1],font=('Radio Canada Big',10),bg='#273746',fg='snow')
        texto.place(x=500,y=170,relwidth=0.25,relheight=0.06)
        Button2=Button(frame,text='MODIFICAR UNIDAD DE MEDIDA',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:MPunidaddemedida())
        Button2.place(x=120,y=210,relwidth=0.5,relheight=0.05)
        texto=Label(frame,text=MP[v][2],font=('Radio Canada Big',10),bg='#273746',fg='snow')
        texto.place(x=500,y=210,relwidth=0.25,relheight=0.06)
        if MP[v][4]=='C':
            Button2=Button(frame,text='MODIFICAR PRECIO',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:MPprecio())
            Button2.place(x=120,y=250,relwidth=0.5,relheight=0.05)
            texto=Label(frame,text='${:.2f}'.format(MP[v][3]),font=('Radio Canada Big',10),bg='#273746',fg='snow')
            texto.place(x=500,y=250,relwidth=0.25,relheight=0.06)
        else:
            Button2=Button(frame,text='MODIFICAR CANTIDAD',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:MPcantidad())
            Button2.place(x=120,y=250,relwidth=0.5,relheight=0.05)
            texto=Label(frame,text=MP[v][5],font=('Radio Canada Big',10),bg='#273746',fg='snow')
            texto.place(x=500,y=250,relwidth=0.25,relheight=0.06)
            Button2=Button(frame,text='MODIFICAR CANTIDADES DE MATERIA PRIMA',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:MPcantidades())
            Button2.place(x=120,y=290,relwidth=0.5,relheight=0.05)
        Button2=Button(frame,text='VOLVER',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:menu32A())
        Button2.place(x=40,y=360,relwidth=0.17,relheight=0.05)
        if VARIABLE == 2:
            messagebox.showinfo("FELICIDADES", "DATOS AGREGADOS CORRECTAMENTE")
            VARIABLE=0
    def confirmar32():
        global codigo,VARIABLE,MP,v,CONTADOR,VER,guarda,codMMP
        try:
            codMMP=int(cuadro0.get())
            try:
                v=0
                cursor.execute('SELECT * FROM MATERIA_PRIMA')
                MP=cursor.fetchall()
                codigo=MP[codMMP-1][0]
                VARIABLE=0
                while True:
                    if codigo == MP[v][0]:
                        VARIABLE=0
                        menu322()
                        break
                    else:
                        v+=1
                    if v == len(MP):
                        VARIABLE=1
                        menu32()
                        break
            except IndexError:
                    VARIABLE=1
                    menu32()
        except ValueError:
            VARIABLE=1
            menu32()
    def menu32():
        eliminartodoMENOSUNO()
        global frame,cuadro0,VARIABLE,VER,f,guarda,x,MP
        frame=Frame(raiz,width='700',height='430',bg='#273746')
        frame.pack()
        guarda=0

        cuadro01=StringVar()

        texto=Label(frame,text='MODIFICAR MATERIAS PRIMAS',font=('Radio Canada Big',16),bg='#273746',fg='snow')
        texto.place(relx=0.5,y=60,anchor=tk.CENTER,relwidth=1,relheight=0.10)
        
        if VARIABLE == 1:
            messagebox.showerror("ERROR", "INGRESO DE DATOS INCORRECTO")
            VARIABLE=0
            guarda=1
            atrasMMP()
        else:
            if VARIABLE == 2:
                messagebox.showinfo("FELICIDADES", "DATOS MODIFICADOS CORRECTAMENTE")
                VARIABLE=0
                guarda=1
                atrasMMP()
            else:
                cursor.execute('SELECT * FROM MATERIA_PRIMA')
                MP=cursor.fetchall()
                cursor.execute('SELECT * FROM RECETA')
                REC=cursor.fetchall()
                try:
                    x=0
                    f=40
                    while True:
                        t=0
                        if MP[VER][4] == 'E':
                            w=0
                            # ES ELABORADA ASI QUE BUSCA LA MATERIA PRIMA EN LA TABLA DE RECETAS
                            while True:
                                if MP[VER][1] == REC[w][1]:
                                    u=0
                                    while True:
                                        z=0
                                        # BUSCA LA MATERIA PRIMA DE LA MPE
                                        if REC[w][2] == MP[u][1]:
                                            while True:
                                                if MP[u][1]==REC[z][2]:
                                                    break
                                                else:
                                                    z+=1
                                                if z == len(REC):
                                                    break
                                            t+=(1*(MP[u][3]*REC[w][3])/REC[z][3])
                                            break
                                        else:
                                            u+=1
                                        if u == len(MP):
                                            break
                                    w+=1
                                else:
                                    w+=1
                                if w == len(REC):
                                    break
                        texto=Label(frame,text=VER+1,font=('Radio Canada Big',10),bg='#273746',fg='snow')
                        texto.place(x=10+x,y=170+f,relwidth=0.2,relheight=0.06)
                        texto=Label(frame,text=MP[VER][1],font=('Radio Canada Big',10),bg='#273746',fg='snow')
                        texto.place(x=140+x,y=170+f,relwidth=0.2,relheight=0.06)
                        VER+=1
                        f+=40
                        if VER % 6 == 0:
                            break
                        if VER % 3 == 0:
                            f=40
                            x=350
                            continue
                except IndexError:
                    if VER == 0:
                        messagebox.showwarning("ERROR", "NO HAY MATERIAS PRIMAS")
                        frame.destroy()
                    if f == 40 and x == 0:
                        guarda=1
                        if CONTADOR > 0:
                            messagebox.showwarning("ERROR", "NO HAY MAS MATERIAS PRIMAS")
                            atrasMMP()
        if VER>0:
            texto=Label(frame,text='INGRESE EL CODIGO DE LA MATERIA PRIMA:',font=('Radio Canada Big',12),bg='#273746',fg='snow')
            texto.place(x=10,y=130,relwidth=0.75,relheight=0.06)
            cuadro0=Entry(frame,textvariable=cuadro01)
            cuadro0.place(x=500,y=130,relheight=0.06)
            Button2=Button(frame,text='CONFIRMAR',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:confirmar32())
            Button2.place(x=540,y=360,relwidth=0.17,relheight=0.05)
        try:
            if MP[VER][0]==4:
                pass
            Button2=Button(frame,text='SIGUIENTE',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:siguienteMMP())
            Button2.place(x=180,y=360,relwidth=0.17,relheight=0.05)
        except IndexError:
            pass
        if CONTADOR>0:
            Button2=Button(frame,text='ATRAS',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:atrasMMP())
            Button2.place(x=40,y=360,relwidth=0.17,relheight=0.05)
    #################################################################################################################################################################
    #################################################################################################################################################################
    # ELIMINAR DATOS DE PRODUCTO
    def menu41A():
        eliminartodo()
        menu41()
    def siguienteEP():
        global CONTADOR
        CONTADOR+=1
        menu41()
    def atrasEP():
        global VER,CONTADOR,f,guarda,x
        if guarda == 1:
            CONTADOR=0
            VER=0
            guarda=0
            menu41()
        else:
            if CONTADOR > 0:
                if x == 0:
                    if f == 80:
                        VER-=7
                    if f == 120:
                        VER-=8
                    if f == 160:
                        VER-=9
                if x == 350:
                    if f == 40:
                        VER-=9
                    if f == 80:
                        VER-=10
                    if f == 120:
                        VER-=11
                    if f == 160:
                        VER-=12
                CONTADOR-=1
            else:
                VER=0
            menu41()
    def confirmar41():
        global codigo,VARIABLE,PRO,v,CONTADOR,VER,guarda
        try:
            cod=int(cuadro0.get())
            try:
                v=0
                cursor.execute('SELECT * FROM PRODUCTO')
                PRO=cursor.fetchall()
                codigo=PRO[cod-1][0]
                VARIABLE=0
                while True:
                    if codigo == PRO[v][0]:
                        VARIABLE=2
                        cursor.execute('DELETE FROM RECETA WHERE nombrereceta == (?)',(PRO[v][1],))
                        base.commit()
                        cursor.execute('DELETE FROM PRODUCTO WHERE codigoproducto == (?)',(PRO[v][0],))
                        base.commit()
                        guarda=1
                        atrasEP()
                        break
                    else:
                        v+=1
                    if v == len(PRO):
                        VARIABLE=1
                        menu41()
                        break
            except IndexError:
                    VARIABLE=1
                    menu41()
        except ValueError:
            VARIABLE=1
            menu41()
    def menu41():
        eliminartodoMENOSUNO()
        global frame,cuadro0,VARIABLE,VER,f,guarda,x,PRO
        frame=Frame(raiz,width='700',height='430',bg='#273746')
        frame.pack()
        guarda=0

        cuadro01=StringVar()

        texto=Label(frame,text='ELIMINAR PRODUCTOS',font=('Radio Canada Big',16),bg='#273746',fg='snow')
        texto.place(relx=0.5,y=60,anchor=tk.CENTER,relwidth=1,relheight=0.10)
               
        if VARIABLE == 1:
            messagebox.showerror("ERROR", "INGRESO DE DATOS INCORRECTO")
            VARIABLE=0
            guarda=1
            atrasEP()
        else:
            if VARIABLE == 2:
                messagebox.showinfo("FELICIDADES", "DATOS ELIMINADOS CORRECTAMENTE")
                VARIABLE=0
                guarda=1
                atrasEP()
            else:
                cursor.execute('SELECT * FROM RECETA')
                REC=cursor.fetchall()
                cursor.execute('SELECT * FROM MATERIA_PRIMA')
                MP=cursor.fetchall()
                cursor.execute('SELECT * FROM PRODUCTO')
                PRO=cursor.fetchall()
                try:
                    x=0
                    f=40
                    while True:
                        x=0
                        v=0
                        while True:
                            # BUSCA EL PRODUCTO EN LA TABLA DE RECETAS
                            if PRO[VER][1] == REC[x][1]:
                                z=0
                                while True:
                                    # BUSCA LA MATERIA PRIMA DEL PRODUCTO
                                    if REC[x][2] == MP[z][1]:
                                        # ES COMPRADA
                                        if MP[z][4] == 'C':
                                            v+=(MP[z][3]*REC[x][3])
                                            break
                                        else:
                                            w=0
                                            # ES ELABORADA ASI QUE BUSCA LA MATERIA PRIMA EN LA TABLA DE RECETAS
                                            while True:
                                                if MP[z][1] == REC[w][1]:
                                                    u=0
                                                    t=0
                                                    while True:
                                                        # BUSCA LA MATERIA PRIMA DE LA MPE
                                                        if REC[w][2] == MP[u][1]:
                                                            while True:
                                                                if MP[u][1]==REC[t][2]:
                                                                    break
                                                                else:
                                                                    t+=1
                                                                if t == len(REC):
                                                                    break
                                                            v+=(REC[x][3]*(MP[u][3]*REC[w][3])/REC[t][3])
                                                            break
                                                        else:
                                                            u+=1
                                                        if u == len(MP):
                                                            break
                                                    w+=1
                                                else:
                                                    w+=1
                                                if w == len(REC):
                                                    break
                                        break
                                    else:
                                        z+=1
                                    if z == len(MP):
                                        break
                                x+=1
                            else:
                                x+=1
                            if x == len(REC):
                                break
                        texto=Label(frame,text=VER+1,font=('Radio Canada Big',10),bg='#273746',fg='snow')
                        texto.place(x=10+x,y=170+f,relwidth=0.15,relheight=0.06)
                        texto=Label(frame,text=PRO[VER][1],font=('Radio Canada Big',10),bg='#273746',fg='snow')
                        texto.place(x=120+x,y=170+f,relwidth=0.15,relheight=0.06)
                        VER+=1
                        f+=40
                        if VER % 6 == 0:
                            break
                        if VER % 3 == 0:
                            f=40
                            x=350
                            continue
                except IndexError:
                    if VER == 0:
                            messagebox.showwarning("ERROR", "NO HAY PRODUCTOS")
                            frame.destroy()
                    if f == 40 and x == 0:
                        guarda=1
                        if CONTADOR > 0:
                            messagebox.showwarning("ERROR", "NO HAY MAS PRODUCTOS")
                            atrasEP()
        if VER>0:
            texto=Label(frame,text='INGRESE EL CODIGO DEL PRODUCTO:',font=('Radio Canada Big',12),bg='#273746',fg='snow')
            texto.place(x=10,y=130,relwidth=0.75,relheight=0.06)
            cuadro0=Entry(frame,textvariable=cuadro01)
            cuadro0.place(x=500,y=130,relheight=0.06)
            Button2=Button(frame,text='CONFIRMAR',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:confirmar41())
            Button2.place(x=540,y=360,relwidth=0.17,relheight=0.05)
        try:
            if PRO[VER][0]==4:
                pass
            Button2=Button(frame,text='SIGUIENTE',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:siguienteEP())
            Button2.place(x=180,y=360,relwidth=0.17,relheight=0.05)
        except IndexError:
            pass
        if CONTADOR>0:
            Button2=Button(frame,text='ATRAS',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:atrasEP())
            Button2.place(x=40,y=360,relwidth=0.17,relheight=0.05)
    # ELIMINAR DATOS DE MATERIA PRIMA
    def menu42A():
        eliminartodo()
        menu42()
    def siguienteEMP():
        global CONTADOR
        CONTADOR+=1
        menu42()
    def atrasEMP():
        global VER,CONTADOR,f,guarda,x
        if guarda == 1:
            CONTADOR=0
            VER=0
            guarda=0
            menu42()
        else:
            if CONTADOR > 0:
                if x == 0:
                    if f == 80:
                        VER-=7
                    if f == 120:
                        VER-=8
                    if f == 160:
                        VER-=9
                if x == 350:
                    if f == 40:
                        VER-=9
                    if f == 80:
                        VER-=10
                    if f == 120:
                        VER-=11
                    if f == 160:
                        VER-=12
                CONTADOR-=1
            else:
                VER=0
            menu42()
    def confirmar42():
        global codigo,VARIABLE,MP,v,CONTADOR,VER,guarda
        try:
            cod=int(cuadro0.get())
            try:
                cursor.execute('SELECT * FROM MATERIA_PRIMA')
                MP=cursor.fetchall()
                cursor.execute('SELECT * FROM RECETA')
                REC=cursor.fetchall()
                codigo=MP[cod-1][0]
                v=0
                u=0
                VARIABLE=0
                while True:
                    if codigo == MP[v][0]:
                        try:
                            while True:
                                if MP[v][1] == REC[u][2]:
                                    VARIABLE=3
                                    menu42()
                                    break
                                else:
                                    u+=1
                                if u == len(REC):
                                    VARIABLE=2
                                    cursor.execute('DELETE FROM RECETA WHERE nombrereceta == (?)',(MP[v][1],))
                                    base.commit()
                                    cursor.execute('DELETE FROM MATERIA_PRIMA WHERE codigomateriaprima == (?)',(MP[v][0],))
                                    base.commit()
                                    guarda=1
                                    atrasEMP()
                                    break
                        except IndexError:
                            cursor.execute('DELETE FROM MATERIA_PRIMA WHERE codigomateriaprima == (?)',(MP[v][0],))
                            base.commit()
                            guarda=1
                            VARIABLE=2
                            atrasEMP()
                        break
                    else:
                        v+=1
                    if v == len(MP):
                        VARIABLE=1
                        menu42()
                        break
            except IndexError:
                VARIABLE=1
                menu42()
        except ValueError:
            VARIABLE=1
            menu42()
    def menu42():
        eliminartodoMENOSUNO()
        global frame,cuadro0,VARIABLE,VER,f,guarda,x,MP
        frame=Frame(raiz,width='700',height='430',bg='#273746')
        frame.pack()
        guarda=0

        cuadro01=StringVar()

        texto=Label(frame,text='ELIMINAR MATERIAS PRIMAS',font=('Radio Canada Big',16),bg='#273746',fg='snow')
        texto.place(relx=0.5,y=60,anchor=tk.CENTER,relwidth=1,relheight=0.10)

        if VARIABLE == 1:
            messagebox.showerror("ERROR", "INGRESO DE DATOS INCORRECTO")
            VARIABLE=0
            guarda=1
            atrasEMP()
        else:
            if VARIABLE == 2:
                messagebox.showinfo("FELICIDADES", "DATOS ELIMINADOS CORRECTAMENTE")
                VARIABLE=0
                guarda=1
                atrasEMP()
            else:   
                if VARIABLE == 3:
                    messagebox.showwarning("ERROR", "NO SE PUEDEN ELIMINAR LOS DATOS")
                    VARIABLE=0
                    guarda=1
                    atrasEMP()
                else:
                    cursor.execute('SELECT * FROM MATERIA_PRIMA')
                    MP=cursor.fetchall()
                    cursor.execute('SELECT * FROM RECETA')
                    REC=cursor.fetchall()
                    try:
                        x=0
                        f=40
                        while True:
                            t=0
                            if MP[VER][4] == 'E':
                                w=0
                                # ES ELABORADA ASI QUE BUSCA LA MATERIA PRIMA EN LA TABLA DE RECETAS
                                while True:
                                    if MP[VER][1] == REC[w][1]:
                                        u=0
                                        while True:
                                            z=0
                                            # BUSCA LA MATERIA PRIMA DE LA MPE
                                            if REC[w][2] == MP[u][1]:
                                                while True:
                                                    if MP[u][1]==REC[z][2]:
                                                        break
                                                    else:
                                                        z+=1
                                                    if z == len(REC):
                                                        break
                                                t+=(1*(MP[u][3]*REC[w][3])/REC[z][3])
                                                break
                                            else:
                                                u+=1
                                            if u == len(MP):
                                                break
                                        w+=1
                                    else:
                                        w+=1
                                    if w == len(REC):
                                        break
                            texto=Label(frame,text=VER+1,font=('Radio Canada Big',10),bg='#273746',fg='snow')
                            texto.place(x=10+x,y=170+f,relwidth=0.2,relheight=0.06)
                            texto=Label(frame,text=MP[VER][1],font=('Radio Canada Big',10),bg='#273746',fg='snow')
                            texto.place(x=140+x,y=170+f,relwidth=0.2,relheight=0.06)
                            VER+=1
                            f+=40
                            if VER % 6 == 0:
                                break
                            if VER % 3 == 0:
                                f=40
                                x=350
                                continue
                    except IndexError:
                        if VER == 0:
                            messagebox.showwarning("ERROR", "NO HAY MATERIAS PRIMAS")
                            frame.destroy()
                        if f == 40 and x == 0:
                            guarda=1
                            if CONTADOR > 0:
                                messagebox.showwarning("ERROR", "NO HAY MAS MATERIAS PRIMAS")
                                atrasEMP()
        if VER>0:
            texto=Label(frame,text='INGRESE EL CODIGO DE LA MATERIA PRIMA:',font=('Radio Canada Big',12),bg='#273746',fg='snow')
            texto.place(x=10,y=130,relwidth=0.75,relheight=0.06)
            cuadro0=Entry(frame,textvariable=cuadro01)
            cuadro0.place(x=500,y=130,relheight=0.06)
            Button2=Button(frame,text='CONFIRMAR',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:confirmar42())
            Button2.place(x=540,y=360,relwidth=0.17,relheight=0.05)
        try:
            if MP[VER][0]==4:
                pass
            Button2=Button(frame,text='SIGUIENTE',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:siguienteEMP())
            Button2.place(x=180,y=360,relwidth=0.17,relheight=0.05)
        except IndexError:
            pass
        if CONTADOR>0:
            Button2=Button(frame,text='ATRAS',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:atrasEMP())
            Button2.place(x=40,y=360,relwidth=0.17,relheight=0.05)
    #################################################################################################################################################################
    #################################################################################################################################################################
    # INICIO
    VER=0
    CONTADOR=0
    raiz1.destroy()
    raiz=tk.Tk()
    raiz.title('LAURA INC')
    raiz.config(bg='#273746')
    raiz.geometry('700x476')
    raiz.resizable(0,0)

    titulo=Label(raiz,text='MENU PRINCIPAL',font=('Radio Canada Big', 16),fg='snow')
    titulo.place(relx=0.5,y=60,anchor=tk.CENTER,relwidth=1,relheight=0.1)
    titulo.config(bg='#273746')
    cerrar=Button(raiz,text='CERRAR',font=('Radio Canada Big',11),fg='black',command=lambda:volverainicio())
    cerrar.place(x=570,y=440,relwidth=0.15,relheight=0.05)
    cerrar.config(bg='snow')
    
    menubarra=Menu(raiz)
    
    menu0=Menu(menubarra,tearoff=0)
    menu0.add_command(label='INGRESAR MATERIAS PRIMAS',font=('Radio Canada Big',10), command=lambda:menu12())
    menu0.add_command(label='INGRESAR PRODUCTOS',font=('Radio Canada Big',10), command=lambda:menu1())
    menubarra.add_cascade(label='INGRESAR DATOS',font=('Radio Canada Big',10), menu=menu0)
        
    menu2=Menu(menubarra,tearoff=0)
    menu2.add_command(label='VER MATERIAS PRIMAS',font=('Radio Canada Big',10), command=lambda:menu22A())
    menu2.add_command(label='VER PRODUCTOS',font=('Radio Canada Big',10), command=lambda:menu21A())
    menubarra.add_cascade(label='CONSULTAR DATOS',font=('Radio Canada Big',10), menu=menu2)
        
    menu3=Menu(menubarra,tearoff=0)
    menu3.add_command(label='MODIFICAR MATERIAS PRIMAS',font=('Radio Canada Big',10),command=lambda:menu32A())
    menu3.add_command(label='MODIFICAR PRODUCTOS',font=('Radio Canada Big',10),command=lambda:menu31A())
    menubarra.add_cascade(label='MODIFICAR DATOS',font=('Radio Canada Big',10),menu=menu3)

    menu4=Menu(menubarra,tearoff=0)
    menu4.add_command(label='ELIMINAR MATERIAS PRIMAS',font=('Radio Canada Big',10),command=lambda:menu42A())
    menu4.add_command(label='ELIINAR PRODUCTOS',font=('Radio Canada Big',10),command=lambda:menu41A())
    menubarra.add_cascade(label='ELIMINAR DATOS',font=('Radio Canada Big',10),menu=menu4)
        
    raiz.config(menu=menubarra)
    raiz.mainloop
#####################################################################################################################################################################
#####################################################################################################################################################################
# CODE IN ENGLISH
def english():
    global raiz,VARIABLE,frame,Y,v,VER,CONTADOR,Y,VARIABLE1
    VARIABLE = 0
    VARIABLE1 = 0
    Y=0
    v=0
    #################################################################################################################################################################
    #################################################################################################################################################################
    # INGRESAR DATOS DE PRODUCTO
    def confirmar1111():
        global VARIABLE,unidad,precio
        try:
            unidad=cuadro1.get()
            precio=float(cuadro2.get())
            if unidad.isalpha() == True:
                cursor.execute('SELECT * FROM MATERIA_PRIMA')
                MP=cursor.fetchall()
                v=0
                try:
                    while True:
                        if MP[v][1] == materiaprima.upper():
                            # LA MATERIA PRIMA EXISTE
                            VARIABLE=3
                            menu1111()
                            break
                        else:
                            v+=1
                        if v == len(MP):
                            cursor.execute('INSERT INTO MATERIA_PRIMA VALUES(NULL,?,?,?,?,?)',(materiaprima.upper(),unidad.upper(),precio,'C',0),)
                            base.commit()
                            cursor.execute('SELECT * FROM MATERIA_PRIMA')
                            MP=cursor.fetchall()
                            v=0
                            try:
                                while True:
                                    if MP[v][1] == materiaprima.upper():
                                        # LA MATERIA PRIMA EXISTE
                                        cursor.execute('INSERT INTO RECETA VALUES(NULL,?,?,?,?)',(producto.upper(),materiaprima.upper(),cantidad,MP[v][4]),)
                                        base.commit()
                                        if tipo.upper() == 'F':
                                            variable=0
                                            cursor.execute('SELECT * FROM PRODUCTO')
                                            PRO=cursor.fetchall()
                                            try:
                                                while True:
                                                    if PRO[variable][1] == producto.upper():
                                                        break
                                                    else:
                                                        variable+=1
                                                    if variable == len(PRO):
                                                        cursor.execute('INSERT INTO PRODUCTO VALUES(NULL,?,?)',(producto.upper(),preciocarta),)
                                                        base.commit()
                                                        break
                                            except IndexError:
                                                cursor.execute('INSERT INTO PRODUCTO VALUES(NULL,?,?)',(producto.upper(),preciocarta),)
                                                base.commit()
                                            VARIABLE=2
                                            menu111()
                                            break
                                        else:
                                            variable=0
                                            cursor.execute('SELECT * FROM MATERIA_PRIMA')
                                            MP=cursor.fetchall()
                                            try:
                                                while True:
                                                    if MP[variable][1] == producto.upper():
                                                        cursor.execute('UPDATE MATERIA_PRIMA set preciomateriaprima = (?) WHERE codigomateriaprima = (?)',(MP[variable][3]+((MP[v][3]*cantidad)/MP[variable][5]),MP[variable][0]),)
                                                        base.commit()
                                                        break
                                                    else:
                                                        variable+=1
                                                    if variable == len(MP):
                                                        cursor.execute('INSERT INTO MATERIA_PRIMA VALUES(NULL,?,?,?,?,?)',(producto.upper(),unidad.upper(),(MP[v][3]*cantidad)/cant,'E',cant),)
                                                        base.commit()
                                                        break
                                            except IndexError:
                                                cursor.execute('INSERT INTO MATERIA_PRIMA VALUES(NULL,?,?,?,?,?)',(producto.upper(),unidad.upper(),(MP[v][3]*cantidad)/cant,'E',cant),)
                                                base.commit()
                                            VARIABLE=2
                                            menu111()
                                        break
                                    else:
                                        v+=1
                                    if v == len(MP):
                                        # LA MATERIA PRIMA NO EXISTE
                                        VARIABLE=4
                                        menu1111()
                                        break
                            except IndexError:
                                VARIABLE=4
                                menu1111()
                            break
                except IndexError:
                    cursor.execute('INSERT INTO MATERIA_PRIMA VALUES(NULL,?,?,?,?,?)',(materiaprima.upper(),unidad.upper(),precio,'C',0),)
                    base.commit()
                    cursor.execute('INSERT INTO RECETA VALUES(NULL,?,?,?,?)',(producto.upper(),materiaprima.upper(),cantidad,'C'),)
                    base.commit()
                    variable=0
                    if tipo.upper() == 'F':
                        cursor.execute('SELECT * FROM PRODUCTO')
                        PRO=cursor.fetchall()
                        try:
                            while True:
                                if PRO[variable][1] == producto.upper():
                                    break
                                else:
                                    variable+=1
                                if variable == len(PRO):
                                    cursor.execute('INSERT INTO PRODUCTO VALUES(NULL,?,?)',(producto.upper(),preciocarta),)
                                    base.commit()
                                    break
                        except IndexError:
                            cursor.execute('INSERT INTO PRODUCTO VALUES(NULL,?,?)',(producto.upper(),preciocarta),)
                            base.commit()
                        VARIABLE=2
                        menu111()
                    else:
                        cursor.execute('SELECT * FROM MATERIA_PRIMA')
                        MP=cursor.fetchall()
                        try:
                            while True:
                                if MP[variable][1] == producto.upper():
                                    break
                                else:
                                    variable+=1
                                if variable == len(MP):
                                    cursor.execute('INSERT INTO MATERIA_PRIMA VALUES(NULL,?,?,NULL,?,?)',(producto.upper(),unidad.upper(),'E',cant),)
                                    base.commit()
                                    break
                        except IndexError:
                            cursor.execute('INSERT INTO MATERIA_PRIMA VALUES(NULL,?,?,NULL,?,?)',(producto.upper(),unidad.upper(),'E',cant),)
                            base.commit()
                        VARIABLE=2
                        menu111()
            else:
                VARIABLE=1
                menu1111()
        except ValueError:
            VARIABLE=1
            menu1111()
    def menu1111():
        eliminartodo()
        global frame,cuadro1,cuadro2,VARIABLE
        frame=Frame(raiz,width='700',height='430',bg='#273746')
        frame.pack()
        cuadro11=StringVar()
        cuadro10=StringVar()
        
        texto=Label(frame,text='ENTER RAW MATERIALS',font=('Radio Canada Big',16),bg='#273746',fg='snow')
        texto.place(relx=0.5,y=60,anchor=tk.CENTER,relwidth=1,relheight=0.10)
        if VARIABLE == 1:
            messagebox.showerror("ERROR", "WRONG DATA ENTERED")
            VARIABLE=0
        else:
            if VARIABLE == 3:
                messagebox.showerror("ERROR", "THE RAW MATERIAL HAS BEEN ENTERED")
                VARIABLE=0
            else:
                if VARIABLE == 4:
                    messagebox.showerror("ERROR", "YOU HAVE TO ADD THAT RAW MATERIAL (OR YOU CAN RETURN)")
                    VARIABLE=0
        texto=Label(frame,text='ENTER RAW MATERIAL NAME:',font=('Radio Canada Big',12),bg='#273746',fg='snow')
        texto.place(x=10,y=130,relwidth=0.75,relheight=0.06)
        texto=Label(frame,text=materiaprima.upper(),font=('Radio Canada Big',12),bg='#273746',fg='snow')
        texto.place(x=500,y=130,relwidth=0.20,relheight=0.06)
        texto=Label(frame,text='ENTER UNIT OF MEASURE:',font=('Radio Canada Big',12),bg='#273746',fg='snow')
        texto.place(x=10,y=170,relwidth=0.75,relheight=0.06)
        cuadro1=Entry(frame,textvariable=cuadro11)
        cuadro1.place(x=500,y=170,relheight=0.06)
        texto=Label(frame,text='ENTER UNIT PRICE: ',font=('Radio Canada Big',12),bg='#273746',fg='snow')
        texto.place(x=10,y=210,relwidth=0.75,relheight=0.06)
        cuadro2=Entry(frame,textvariable=cuadro10)
        cuadro2.place(x=500,y=210,relheight=0.06)
        Button2=Button(frame,text='CONFIRM',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:confirmar1111())
        Button2.place(x=540,y=360,relwidth=0.17,relheight=0.05)
        Button2=Button(frame,text='RETURN',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:menu111())
        Button2.place(x=40,y=360,relwidth=0.17,relheight=0.05)
    def confirmar111():
        global VARIABLE,materiaprima,cantidad
        try:
            materiaprima=cuadro0.get()
            if materiaprima == '':
                VARIABLE=1
                menu111()
            else:
                cantidad=float(cuadro1.get())
                cursor.execute('SELECT * FROM MATERIA_PRIMA')
                MP=cursor.fetchall()
                cursor.execute('SELECT * FROM RECETA')
                REC=cursor.fetchall()
                v=0
                try:
                    while True:
                        if MP[v][1] == materiaprima.upper():
                            # LA MATERIA PRIMA EXISTE
                            w=0
                            try:
                                while True:
                                    if materiaprima.upper() == REC[w][2] and producto.upper() == REC[w][1]:
                                        VARIABLE=4
                                        menu111()
                                        break
                                    else:
                                        w+=1
                                    if w == len(REC):
                                        cursor.execute('INSERT INTO RECETA VALUES(NULL,?,?,?,?)',(producto.upper(),materiaprima.upper(),cantidad,MP[v][4]),)
                                        base.commit()
                                        if tipo.upper() == 'F':
                                            variable=0
                                            cursor.execute('SELECT * FROM PRODUCTO')
                                            PRO=cursor.fetchall()
                                            try:
                                                while True:
                                                    if PRO[variable][1] == producto.upper():
                                                        break
                                                    else:
                                                        variable+=1
                                                    if variable == len(PRO):
                                                        cursor.execute('INSERT INTO PRODUCTO VALUES(NULL,?,?)',(producto.upper(),preciocarta),)
                                                        base.commit()
                                                        break
                                            except IndexError:
                                                cursor.execute('INSERT INTO PRODUCTO VALUES(NULL,?,?)',(producto.upper(),preciocarta),)
                                                base.commit()
                                            VARIABLE=2
                                            menu111()
                                        else:
                                            variable=0
                                            cursor.execute('SELECT * FROM MATERIA_PRIMA')
                                            MP=cursor.fetchall()
                                            try:
                                                while True:
                                                    if MP[variable][1] == producto.upper():
                                                        cursor.execute('UPDATE MATERIA_PRIMA set preciomateriaprima = (?) WHERE codigomateriaprima = (?)',(MP[variable][3]+((MP[v][3]*cantidad)/MP[variable][5]),MP[variable][0]),)
                                                        base.commit()
                                                        break
                                                    else:
                                                        variable+=1
                                                    if variable == len(MP):
                                                        cursor.execute('INSERT INTO MATERIA_PRIMA VALUES(NULL,?,?,?,?,?)',(producto.upper(),unidad.upper(),(MP[v][3]*cantidad)/cant,'E',cant),)
                                                        base.commit()
                                                        break
                                            except IndexError:
                                                cursor.execute('INSERT INTO MATERIA_PRIMA VALUES(NULL,?,?,NULL,?,?)',(producto.upper(),unidad.upper(),(MP[v][3]*cantidad)/cant,'E',cant),)
                                                base.commit()
                                            VARIABLE=2
                                            menu111()
                                        break
                            except IndexError:
                                cursor.execute('INSERT INTO RECETA VALUES(NULL,?,?,?,?)',(producto.upper(),materiaprima.upper(),cantidad,MP[v][4]),)
                                base.commit()
                                if tipo.upper() == 'F':
                                    variable=0
                                    cursor.execute('SELECT * FROM PRODUCTO')
                                    PRO=cursor.fetchall()
                                    try:
                                        while True:
                                            if PRO[variable][1] == producto.upper():
                                                break
                                            else:
                                                variable+=1
                                            if variable == len(PRO):
                                                cursor.execute('INSERT INTO PRODUCTO VALUES(NULL,?,?)',(producto.upper(),preciocarta),)
                                                base.commit()
                                                break
                                    except IndexError:
                                        cursor.execute('INSERT INTO PRODUCTO VALUES(NULL,?,?)',(producto.upper(),preciocarta),)
                                        base.commit()
                                    VARIABLE=2
                                    menu111()
                                else:
                                    variable=0
                                    cursor.execute('SELECT * FROM MATERIA_PRIMA')
                                    MP=cursor.fetchall()
                                    try:
                                        while True:
                                            if MP[variable][1] == producto.upper():
                                                cursor.execute('UPDATE MATERIA_PRIMA set preciomateriaprima = (?) WHERE codigomateriaprima = (?)',(MP[variable][3]+((MP[v][3]*cantidad)/MP[variable][5]),MP[variable][0]),)
                                                base.commit()
                                                break
                                            else:
                                                variable+=1
                                            if variable == len(MP):
                                                cursor.execute('INSERT INTO MATERIA_PRIMA VALUES(NULL,?,?,?,?,?)',(producto.upper(),unidad.upper(),(MP[v][3]*cantidad)/cant,'E',cant),)
                                                base.commit()
                                                break
                                    except IndexError:
                                        cursor.execute('INSERT INTO MATERIA_PRIMA VALUES(NULL,?,?,?,?,?)',(producto.upper(),unidad.upper(),(MP[v][3]*cantidad)/cant,'E',cant),)
                                        base.commit()
                                    VARIABLE=2
                                    menu111()
                            break
                        else:
                            v+=1
                        if v == len(MP):
                            # LA MATERIA PRIMA NO EXISTE
                            VARIABLE=4
                            menu1111()
                            break
                except IndexError:
                    VARIABLE=4
                    menu1111()
        except ValueError:
            VARIABLE=1
            menu111()
    def menu111():
        eliminartodo()
        global frame,cuadro0,cuadro1,VARIABLE,VARIABLE1
        frame=Frame(raiz,width='700',height='430',bg='#273746')
        frame.pack()
        cuadro01=StringVar()
        cuadro11=StringVar()

        texto=Label(frame,text='ENTER PRODUCTS',font=('Radio Canada Big',16),bg='#273746',fg='snow')
        texto.place(relx=0.5,y=60,anchor=tk.CENTER,relwidth=1,relheight=0.10)
        if VARIABLE == 1:
            messagebox.showerror("ERROR", "WRONG DATA ENTERED")
            VARIABLE=0
        else:
            if VARIABLE == 2:
                messagebox.showinfo("CONGRATULATIONS", "DATA ADDED CORRECTLY")
                VARIABLE=0
            else:
                if VARIABLE == 4:
                    messagebox.showerror("ERROR", "THE RAW MATERIAL HAS BEEN ENTERED")
                    VARIABLE=0
        texto=Label(frame,text='PRODUCT NAME:',font=('Radio Canada Big',12),bg='#273746',fg='snow')
        texto.place(x=10,y=130,relwidth=0.75,relheight=0.06)
        texto=Label(frame,text=producto.upper(),font=('Radio Canada Big',12),bg='#273746',fg='snow')
        texto.place(x=500,y=130,relwidth=0.20,relheight=0.06)
        texto=Label(frame,text='PRODUCT TYPE:',font=('Radio Canada Big',12),bg='#273746',fg='snow')
        texto.place(x=10,y=170,relwidth=0.75,relheight=0.06)
        if VARIABLE1 == 3:
            if tipo.upper() == 'F':
                texto=Label(frame,text='FINAL PRODUCT',font=('Radio Canada Big',12),bg='#273746',fg='snow')
                texto.place(x=500,y=170,relwidth=0.20,relheight=0.06)
                texto=Label(frame,text='MENU PRICE:',font=('Radio Canada Big',12),bg='#273746',fg='snow')
                texto.place(x=10,y=210,relwidth=0.75,relheight=0.06)
                texto=Label(frame,text='${:.2f}'.format(PRO[v][2]),font=('Radio Canada Big',12),bg='#273746',fg='snow')
                texto.place(x=500,y=210,relwidth=0.20,relheight=0.06)
            else:
                texto=Label(frame,text='MAIN PRODUCT',font=('Radio Canada Big',12),bg='#273746',fg='snow')
                texto.place(x=500,y=170,relwidth=0.20,relheight=0.06)
                texto=Label(frame,text='QUANTITY:',font=('Radio Canada Big',12),bg='#273746',fg='snow')
                texto.place(x=10,y=210,relwidth=0.75,relheight=0.06)
                texto=Label(frame,text=(MP[v][5],MP[v][2]),font=('Radio Canada Big',12),bg='#273746',fg='snow')
                texto.place(x=500,y=210,relwidth=0.20,relheight=0.06)
        else:
            if tipo.upper() == 'F':
                texto=Label(frame,text='FINAL PRODUCT',font=('Radio Canada Big',12),bg='#273746',fg='snow')
                texto.place(x=500,y=170,relwidth=0.20,relheight=0.06)
                texto=Label(frame,text='MENU PRICE:',font=('Radio Canada Big',12),bg='#273746',fg='snow')
                texto.place(x=10,y=210,relwidth=0.75,relheight=0.06)
                texto=Label(frame,text='${:.2f}'.format(preciocarta),font=('Radio Canada Big',12),bg='#273746',fg='snow')
                texto.place(x=500,y=210,relwidth=0.20,relheight=0.06)
            else:
                texto=Label(frame,text='MAIN PRODUCT',font=('Radio Canada Big',12),bg='#273746',fg='snow')
                texto.place(x=500,y=170,relwidth=0.20,relheight=0.06)
                texto=Label(frame,text='QUANTITY:',font=('Radio Canada Big',12),bg='#273746',fg='snow')
                texto.place(x=10,y=210,relwidth=0.75,relheight=0.06)
                texto=Label(frame,text=(cant,unidad.upper()),font=('Radio Canada Big',12),bg='#273746',fg='snow')
                texto.place(x=500,y=210,relwidth=0.20,relheight=0.06)

        texto=Label(frame,text='ENTER RAW MATERIAL NAME:',font=('Radio Canada Big',12),bg='#273746',fg='snow')
        texto.place(x=10,y=250,relwidth=0.75,relheight=0.06)
        cuadro0=Entry(frame,textvariable=cuadro01)
        cuadro0.place(x=500,y=250,relheight=0.06)
        texto=Label(frame,text='ENTER QUANTITY:',font=('Radio Canada Big',12),bg='#273746',fg='snow')
        texto.place(x=10,y=290,relwidth=0.75,relheight=0.06)
        cuadro1=Entry(frame,textvariable=cuadro11)
        cuadro1.place(x=500,y=290,relheight=0.06)
        Button2=Button(frame,text='CONFIRM',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:confirmar111())
        Button2.place(x=540,y=360,relwidth=0.17,relheight=0.05)
        Button2=Button(frame,text='RETURN',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:menu1())
        Button2.place(x=40,y=360,relwidth=0.17,relheight=0.05)
    def confirmar11():
        global VARIABLE,preciocarta,unidad,cant
        if tipo.upper() == 'F':
            try:
                preciocarta=float(cuadro0.get())
                menu111()
            except ValueError:
                VARIABLE=1
                menu11()
        else:
            try:
                unidad=cuadro0.get()
                cant=float(cuadro1.get())
                if unidad.isalpha() == True:
                    menu111()
                else:
                    VARIABLE=1
                    menu11()
            except ValueError:
                VARIABLE=1
                menu11()
    def menu11():
        eliminartodo()
        global frame,cuadro0,cuadro1,VARIABLE
        frame=Frame(raiz,width='700',height='430',bg='#273746')
        frame.pack()
        cuadro01=StringVar()
        cuadro10=StringVar()

        texto=Label(frame,text='ENTER PRODUCTS',font=('Radio Canada Big',16),bg='#273746',fg='snow')
        texto.place(relx=0.5,y=60,anchor=tk.CENTER,relwidth=1,relheight=0.10)
        if VARIABLE == 1:
            messagebox.showerror("ERROR", "WRONG DATA ENTERED")
            VARIABLE=0
        else:
            if VARIABLE == 2:
                messagebox.showinfo("CONGRATULATIONS", "DATA ADDED CORRECTLY")
                VARIABLE=0
        texto=Label(frame,text='PRODUCT NAME:',font=('Radio Canada Big',12),bg='#273746',fg='snow')
        texto.place(x=10,y=130,relwidth=0.75,relheight=0.06)
        texto=Label(frame,text=producto.upper(),font=('Radio Canada Big',12),bg='#273746',fg='snow')
        texto.place(x=500,y=130,relwidth=0.20,relheight=0.06)
        texto=Label(frame,text='PRODUCT TYPE:',font=('Radio Canada Big',12),bg='#273746',fg='snow')
        texto.place(x=10,y=170,relwidth=0.75,relheight=0.06)

        if tipo.upper() == 'F':
            texto=Label(frame,text='FINAL PRODUCT',font=('Radio Canada Big',12),bg='#273746',fg='snow')
            texto.place(x=500,y=170,relwidth=0.20,relheight=0.06)
            texto=Label(frame,text='ENTER MENU PRICE:',font=('Radio Canada Big',12),bg='#273746',fg='snow')
            texto.place(x=10,y=210,relwidth=0.75,relheight=0.06)
            cuadro0=Entry(frame,textvariable=cuadro01)
            cuadro0.place(x=500,y=210,relheight=0.06)
        else:
            texto=Label(frame,text='MAIN PRODUCT',font=('Radio Canada Big',12),bg='#273746',fg='snow')
            texto.place(x=500,y=170,relwidth=0.20,relheight=0.06)
            texto=Label(frame,text='ENTER UNIT OF MEASURE:',font=('Radio Canada Big',12),bg='#273746',fg='snow')
            texto.place(x=10,y=210,relwidth=0.75,relheight=0.06)
            cuadro0=Entry(frame,textvariable=cuadro01)
            cuadro0.place(x=500,y=210,relheight=0.06)
            texto=Label(frame,text='ENTER QUANTITY:',font=('Radio Canada Big',12),bg='#273746',fg='snow')
            texto.place(x=10,y=250,relwidth=0.75,relheight=0.06)
            cuadro1=Entry(frame,textvariable=cuadro10)
            cuadro1.place(x=500,y=250,relheight=0.06)
        Button2=Button(frame,text='CONFIRM',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:confirmar11())
        Button2.place(x=540,y=360,relwidth=0.17,relheight=0.05)
        Button2=Button(frame,text='RETURN',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:menu1())
        Button2.place(x=40,y=360,relwidth=0.17,relheight=0.05)
    def confirmar1():
        global VARIABLE,producto,tipo,PRO,v,MP,VARIABLE1
        try:
            producto=cuadro0.get()
            if producto == '':
                VARIABLE=1
                menu1()
            else:
                tipo=cuadro1.get()
                if tipo.upper() == 'F':
                    # PRODUCTO FINAL
                    cursor.execute('SELECT * FROM PRODUCTO')
                    PRO=cursor.fetchall()
                    v=0
                    try:
                        while True:
                            if PRO[v][1] == producto.upper():
                                # EL PRODUCTO FINAL EXISTE
                                VARIABLE=0
                                VARIABLE1=3
                                menu111()
                                break
                            else:
                                v+=1
                            if v == len(PRO):
                                # EL PRODUCTO FINAL NO EXISTE
                                VARIABLE=0
                                VARIABLE1=0
                                menu11()
                                break
                    except IndexError:
                        VARIABLE=0
                        menu11()
                else:
                    if tipo.upper() == 'B':
                        # PRODUCTO BASE
                        cursor.execute('SELECT * FROM MATERIA_PRIMA')
                        MP=cursor.fetchall()
                        v=0
                        try:
                            while True:
                                if MP[v][1] == producto.upper():
                                    # EL PRODUCTO BASE EXISTE
                                    VARIABLE=0
                                    VARIABLE1=3
                                    menu111()
                                    break
                                else:
                                    v+=1
                                if v == len(MP):
                                    # EL PRODUCTO BASE NO EXISTE
                                    VARIABLE=0
                                    VARIABLE1=0
                                    menu11()
                                    break
                        except IndexError:
                            VARIABLE=0
                            menu11()
                    else:
                        VARIABLE=1
                        menu1()
        except ValueError:
            VARIABLE=1
            menu1()
    def menu1():
        eliminartodo()
        global frame,cuadro0,cuadro1,VARIABLE
        frame=Frame(raiz,width='700',height='430',bg='#273746')
        frame.pack()
        cuadro01=StringVar()
        cuadro11=StringVar()

        texto=Label(frame,text='ENTER PRODUCTS',font=('Radio Canada Big',16),bg='#273746',fg='snow')
        texto.place(relx=0.5,y=60,anchor=tk.CENTER,relwidth=1,relheight=0.10)
        if VARIABLE == 1:
            messagebox.showerror("ERROR", "WRONG DATA ENTERED")
            VARIABLE=0
        else:
            if VARIABLE == 2:
                messagebox.showinfo("CONGRATULATIONS", "DATA ADDED CORRECTLY")
                VARIABLE=0
        texto=Label(frame,text='ENTER PRODUCT NAME:',font=('Radio Canada Big',12),bg='#273746',fg='snow')
        texto.place(x=10,y=130,relwidth=0.75,relheight=0.06)
        cuadro0=Entry(frame,textvariable=cuadro01)
        cuadro0.place(x=500,y=130,relheight=0.06)
        texto=Label(frame,text='ENTER B (MAIN PRODUCT) OR F (FINAL PRODUCT):',font=('Radio Canada Big',12),bg='#273746',fg='snow')
        texto.place(x=10,y=170,relwidth=0.75,relheight=0.06)
        cuadro1=Entry(frame,textvariable=cuadro11)
        cuadro1.place(x=500,y=170,relheight=0.06)
        Button2=Button(frame,text='CONFIRM',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:confirmar1())
        Button2.place(x=540,y=360,relwidth=0.17,relheight=0.05)
    # INGRESAR DATOS DE MATERIA PRIMA
    def confirmar12():
        global VARIABLE,materiaprima,unidad,precio
        try:
            materiaprima=cuadro0.get()
            unidad=cuadro1.get()
            precio=float(cuadro2.get())
            if unidad.isalpha() == True:
                cursor.execute('SELECT * FROM MATERIA_PRIMA')
                MP=cursor.fetchall()
                v=0
                try:
                    while True:
                        if MP[v][1] == materiaprima.upper():
                            # LA MATERIA PRIMA EXISTE
                            VARIABLE=3
                            menu12()
                            break
                        else:
                            v+=1
                        if v == len(MP):
                            cursor.execute('INSERT INTO MATERIA_PRIMA VALUES(NULL,?,?,?,?,?)',(materiaprima.upper(),unidad.upper(),precio,'C',0),)
                            base.commit()
                            VARIABLE=2
                            menu12()
                            break
                except IndexError:
                    cursor.execute('INSERT INTO MATERIA_PRIMA VALUES(NULL,?,?,?,?,?)',(materiaprima.upper(),unidad.upper(),precio,'C',0),)
                    base.commit()
                    VARIABLE=2
                    menu12()
            else:
                VARIABLE=1
                menu12()
        except ValueError:
            VARIABLE=1
            menu12()
    def menu12():
        eliminartodo()
        global frame,cuadro0,cuadro1,cuadro2,VARIABLE
        frame=Frame(raiz,width='700',height='430',bg='#273746')
        frame.pack()

        cuadro01=StringVar()
        cuadro11=StringVar()
        cuadro10=StringVar()

        texto=Label(frame,text='ENTER RAW MATERIALS',font=('Radio Canada Big',16),bg='#273746',fg='snow')
        texto.place(relx=0.5,y=60,anchor=tk.CENTER,relwidth=1,relheight=0.10)
        texto=Label(frame,text='ENTER RAW MATERIAL NAME:',font=('Radio Canada Big',12),bg='#273746',fg='snow')
        texto.place(x=10,y=130,relwidth=0.75,relheight=0.06)
        cuadro0=Entry(frame,textvariable=cuadro01)
        cuadro0.place(x=500,y=130,relheight=0.06)
        texto=Label(frame,text='ENTER UNIT OF MEASURE:',font=('Radio Canada Big',12),bg='#273746',fg='snow')
        texto.place(x=10,y=170,relwidth=0.75,relheight=0.06)
        cuadro1=Entry(frame,textvariable=cuadro11)
        cuadro1.place(x=500,y=170,relheight=0.06)
        texto=Label(frame,text='ENTER UNIT PRICE: ',font=('Radio Canada Big',12),bg='#273746',fg='snow')
        texto.place(x=10,y=210,relwidth=0.75,relheight=0.06)
        cuadro2=Entry(frame,textvariable=cuadro10)
        cuadro2.place(x=500,y=210,relheight=0.06)
        Button2=Button(frame,text='CONFIRM',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:confirmar12())
        Button2.place(x=540,y=360,relwidth=0.17,relheight=0.05)
        if VARIABLE == 1:
            messagebox.showerror("ERROR", "WRONG DATA ENTERED")
            VARIABLE=0
        else:
            if VARIABLE == 2:
                messagebox.showinfo("CONGRATULATIONS", "DATA ADDED CORRECTLY")
                VARIABLE=0
            else:
                if VARIABLE == 3:
                    messagebox.showerror("ERROR", "THE RAW MATERIAL HAS BEEN ENTERED")
                    VARIABLE=0
    #################################################################################################################################################################
    #################################################################################################################################################################
    # VER DATOS DE PRODUCTO
    def menu21A():
        eliminartodo()
        menu21()
    def siguiente():
        global CONTADOR
        CONTADOR+=1
        menu21()
    def atras():
        global VER,CONTADOR,f,guarda
        if guarda == 1:
            VER=0
            CONTADOR=0
            guarda=0
            menu21()
        else:
            if CONTADOR > 0:
                if f == 80:
                    VER-=5
                if f == 120:
                    VER-=6
                if f == 160:
                    VER-=7
                if f == 200:
                    VER-=8
                CONTADOR-=1
            else:
                VER=0
            menu21()
    def menu21():
        eliminartodoMENOSUNO()
        global frame,VER,f,guarda,PRO
        frame=Frame(raiz,width='700',height='430',bg='#273746')
        frame.pack()
        guarda=0
        texto=Label(frame,text='SEE PRODUCTS',font=('Radio Canada Big',16),bg='#273746',fg='snow')
        texto.place(relx=0.5,y=60,anchor=tk.CENTER,relwidth=1,relheight=0.10)
                
        cursor.execute('SELECT * FROM RECETA')
        REC=cursor.fetchall()
        cursor.execute('SELECT * FROM MATERIA_PRIMA')
        MP=cursor.fetchall()
        cursor.execute('SELECT * FROM PRODUCTO')
        PRO=cursor.fetchall()
        try:
            f=40
            while True:
                x=0
                v=0
                while True:
                    # BUSCA EL PRODUCTO EN LA TABLA DE RECETAS
                    if PRO[VER][1] == REC[x][1]:
                        z=0
                        while True:
                            # BUSCA LA MATERIA PRIMA DEL PRODUCTO
                            if REC[x][2] == MP[z][1]:
                                v+=(MP[z][3]*REC[x][3])
                                break
                            else:
                                z+=1
                            if z == len(MP):
                                break
                        x+=1
                    else:
                        x+=1
                    if x == len(REC):
                        break
                texto=Label(frame,text=VER+1,font=('Radio Canada Big',10),bg='#273746',fg='snow')
                texto.place(x=10,y=130+f,relwidth=0.15,relheight=0.06)
                texto=Label(frame,text=PRO[VER][1],font=('Radio Canada Big',10),bg='#273746',fg='snow')
                texto.place(x=120,y=130+f,relwidth=0.15,relheight=0.06)
                texto=Label(frame,text='${:.2f}'.format(PRO[VER][2]),font=('Radio Canada Big',10),bg='#273746',fg='snow')
                texto.place(x=230,y=130+f,relwidth=0.15,relheight=0.06)
                texto=Label(frame,text='${:.2f}'.format(v),font=('Radio Canada Big',10),bg='#273746',fg='snow')
                texto.place(x=340,y=130+f,relwidth=0.15,relheight=0.06)
                if (PRO[VER][2]-v) > 0:
                    texto=Label(frame,text='YOU WIN',font=('Radio Canada Big',12),bg='#273746',fg='snow')
                    texto.place(x=450,y=130+f,relwidth=0.15,relheight=0.06)
                    texto=Label(frame,text='${:.2f}'.format(PRO[VER][2]-v),font=('Radio Canada Big',10),bg='#273746',fg='snow')
                    texto.place(x=560,y=130+f,relwidth=0.15,relheight=0.06)
                else:
                    texto=Label(frame,text='YOU LOSE',font=('Radio Canada Big',12),bg='#273746',fg='snow')
                    texto.place(x=450,y=130+f,relwidth=0.15,relheight=0.06)
                    texto=Label(frame,text='${:.2f}'.format(v-PRO[VER][2]),font=('Radio Canada Big',10),bg='#273746',fg='snow')
                    texto.place(x=560,y=130+f,relwidth=0.15,relheight=0.06)
                VER+=1
                f+=40
                if VER % 4 == 0:
                    break
        except IndexError:
            if VER == 0:
                messagebox.showwarning("ERROR", "THERE ARE NO PRODUCTS")
                frame.destroy()
            if f == 40:
                guarda=1
                if CONTADOR > 0:
                    messagebox.showwarning("ERROR", "THERE ARE NO MORE PRODUCTS")
                    atras()
        if VER>0:
            texto=Label(frame,text='CODE',font=('Radio Canada Big',12),bg='#273746',fg='snow')
            texto.place(x=10,y=130,relwidth=0.15,relheight=0.06)
            texto=Label(frame,text='NAME',font=('Radio Canada Big',12),bg='#273746',fg='snow')
            texto.place(x=120,y=130,relwidth=0.15,relheight=0.06)
            texto=Label(frame,text='PRICE',font=('Radio Canada Big',12),bg='#273746',fg='snow')
            texto.place(x=230,y=130,relwidth=0.15,relheight=0.06)
            texto=Label(frame,text='COST',font=('Radio Canada Big',12),bg='#273746',fg='snow')
            texto.place(x=340,y=130,relwidth=0.15,relheight=0.06)
        try:
            if PRO[VER][0]==4:
                pass
            Button2=Button(frame,text='NEXT',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:siguiente())
            Button2.place(x=180,y=360,relwidth=0.17,relheight=0.05)
        except IndexError:
            pass
        if CONTADOR>0:
            Button2=Button(frame,text='BACK',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:atras())
            Button2.place(x=40,y=360,relwidth=0.17,relheight=0.05)
    # VER DATOS DE MATERIA PRIMA
    def menu22A():
        eliminartodo()
        menu22()
    def siguiente1():
        global CONTADOR
        CONTADOR+=1
        menu22()
    def atras1():
        global VER,CONTADOR,f,guarda
        if guarda == 1:
            VER=0
            CONTADOR=0
            guarda=0
            menu22()
        else:
            if CONTADOR > 0:
                if f == 80:
                    VER-=5
                if f == 120:
                    VER-=6
                if f == 160:
                    VER-=7
                if f == 200:
                    VER-=8
                CONTADOR-=1
            else:
                VER=0
            menu22()
    def menu22():
        eliminartodoMENOSUNO()
        global frame,VER,f,guarda,MP
        frame=Frame(raiz,width='700',height='430',bg='#273746')
        frame.pack()
        guarda=0
        texto=Label(frame,text='SEE RAW MATERIALS',font=('Radio Canada Big',16),bg='#273746',fg='snow')
        texto.place(relx=0.5,y=60,anchor=tk.CENTER,relwidth=1,relheight=0.10)
        
        cursor.execute('SELECT * FROM MATERIA_PRIMA')
        MP=cursor.fetchall()
        try:
            f=40
            while True:
                texto=Label(frame,text=MP[VER][1],font=('Radio Canada Big',10),bg='#273746',fg='snow')
                texto.place(x=140,y=130+f,relwidth=0.2,relheight=0.06)
                texto=Label(frame,text=VER+1,font=('Radio Canada Big',10),bg='#273746',fg='snow')
                texto.place(x=10,y=130+f,relwidth=0.2,relheight=0.06)
                texto=Label(frame,text=MP[VER][2],font=('Radio Canada Big',10),bg='#273746',fg='snow')
                texto.place(x=280,y=130+f,relwidth=0.2,relheight=0.06)
                texto=Label(frame,text='${:.2f}'.format(MP[VER][3]),font=('Radio Canada Big',10),bg='#273746',fg='snow')
                texto.place(x=420,y=130+f,relwidth=0.2,relheight=0.06)
                if MP[VER][4] == 'C':
                    texto=Label(frame,text='BOUGHT',font=('Radio Canada Big',10),bg='#273746',fg='snow')
                    texto.place(x=550,y=130+f,relwidth=0.2,relheight=0.06)
                else:
                    texto=Label(frame,text='MANUFACTURED',font=('Radio Canada Big',10),bg='#273746',fg='snow')
                    texto.place(x=550,y=130+f,relwidth=0.2,relheight=0.06)
                VER+=1
                f+=40
                if VER % 4 == 0:
                    break
        except IndexError:
            if VER == 0:
                messagebox.showwarning("ERROR", "THERE ARE NO RAW MATERIALS")
                frame.destroy()
            if f == 40:
                guarda=1
                if CONTADOR > 0:
                    messagebox.showwarning("ERROR", "THERE ARE NO MORE RAW MATERIALS")
                    atras1()
        if VER>0:
            texto=Label(frame,text='CODE',font=('Radio Canada Big',12),bg='#273746',fg='snow')
            texto.place(x=10,y=130,relwidth=0.2,relheight=0.06)
            texto=Label(frame,text='NAME',font=('Radio Canada Big',12),bg='#273746',fg='snow')
            texto.place(x=140,y=130,relwidth=0.2,relheight=0.06)
            texto=Label(frame,text='UNIT',font=('Radio Canada Big',12),bg='#273746',fg='snow')
            texto.place(x=280,y=130,relwidth=0.2,relheight=0.06)
            texto=Label(frame,text='PRICE',font=('Radio Canada Big',12),bg='#273746',fg='snow')
            texto.place(x=420,y=130,relwidth=0.2,relheight=0.06)
            texto=Label(frame,text='TYPE',font=('Radio Canada Big',12),bg='#273746',fg='snow')
            texto.place(x=550,y=130,relwidth=0.2,relheight=0.06)
        try:
            if MP[VER][0]==4:
                pass
            Button2=Button(frame,text='NEXT',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:siguiente1())
            Button2.place(x=180,y=360,relwidth=0.17,relheight=0.05)
        except IndexError:
            pass
        if CONTADOR>0:
            Button2=Button(frame,text='BACK',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:atras1())
            Button2.place(x=40,y=360,relwidth=0.17,relheight=0.05)
    #################################################################################################################################################################
    #################################################################################################################################################################
    # MODIFICAR DATOS DE PRODUCTO
    def menu31A():
        eliminartodo()
        menu31()
    def siguienteMP():
        global CONTADOR
        CONTADOR+=1
        menu31()
    def atrasMP():
        global VER,CONTADOR,f,guarda,x
        if guarda == 1:
            CONTADOR=0
            VER=0
            guarda=0
            menu31()
        else:
            if CONTADOR > 0:
                if x == 0:
                    if f == 80:
                        VER-=7
                    if f == 120:
                        VER-=8
                    if f == 160:
                        VER-=9
                if x == 350:
                    if f == 40:
                        VER-=9
                    if f == 80:
                        VER-=10
                    if f == 120:
                        VER-=11
                    if f == 160:
                        VER-=12
                CONTADOR-=1
            else:
                VER=0
            menu31()
    def confirmar311111():
        global VARIABLE,cantidad,REC,PRO,Y
        try:
            cantidad=float(cuadro0.get())
            cursor.execute('UPDATE RECETA SET cantidadmateriaprima = (?) WHERE nombrereceta = (?) AND nombremateriaprimareceta = (?)',(cantidad,PRO[v][1],REC[Y][2]))
            base.commit()
            VARIABLE=2
            menu311()
        except ValueError:
            VARIABLE=1
            Mcantidades()
    def menu3111():
        eliminartodo()
        global frame,cuadro0,VARIABLE,REC,PRO,Y
        frame=Frame(raiz,width='700',height='430',bg='#273746')
        frame.pack()

        cuadro01=StringVar()

        texto=Label(frame,text='MODIFY PRODUCTS',font=('Radio Canada Big',16),bg='#273746',fg='snow')
        texto.place(relx=0.5,y=60,anchor=tk.CENTER,relwidth=1,relheight=0.10)
        texto=Label(frame,text='ENTER NEW QUANTITY:',font=('Radio Canada Big',12),bg='#273746',fg='snow')
        texto.place(x=10,y=130,relwidth=0.75,relheight=0.06)
        cuadro0=Entry(frame,textvariable=cuadro01)
        cuadro0.place(x=500,y=130,relheight=0.06)
        Button2=Button(frame,text='CONFIRM',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:confirmar311111())
        Button2.place(x=540,y=360,relwidth=0.17,relheight=0.05)
        Button2=Button(frame,text='RETURN',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:menu311())
        Button2.place(x=40,y=360,relwidth=0.17,relheight=0.05)
        if VARIABLE == 1:
            messagebox.showerror("ERROR", "WRONG DATA ENTERED")
            VARIABLE=0
    def confirmar31111():
        global VARIABLE,opcion,REC,PRO,Y
        cursor.execute('SELECT * FROM RECETA')
        REC=cursor.fetchall()
        cursor.execute('SELECT * FROM PRODUCTO')
        PRO=cursor.fetchall()
        Y=0
        v=0
        bandera=0
        try:
            opcion=cuadro0.get()
            if opcion == '':
                VARIABLE=1
                Mcantidades()
            else:
                while True:
                    if PRO[v][0] == codigo:
                        while True:
                            if REC[Y][1] == PRO[v][1]:
                                if opcion.upper() == REC[Y][2]:
                                    VARIABLE=0
                                    bandera = 1
                                    menu3111()
                                    break
                                else:
                                    Y+=1
                                    break
                            else:
                                Y+=1
                        if bandera == 1:
                            break
                    else:
                        v+=1
        except ValueError:
            VARIABLE=1
            Mcantidades()
    def Mcantidades():
        eliminartodo()
        global frame,cuadro0,VARIABLE,Y
        frame=Frame(raiz,width='700',height='430',bg='#273746')
        frame.pack()

        cursor.execute('SELECT * FROM PRODUCTO')
        PRO=cursor.fetchall()
        cursor.execute('SELECT * FROM RECETA')
        REC=cursor.fetchall()
        Button2=Button(frame,text='NEXT',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:Mcantidades())
        Button2.place(x=180,y=360,relwidth=0.17,relheight=0.05)
        try:
            while True:
                if REC[Y][1] == PRO[v][1]:
                    texto=Label(frame,text=REC[Y][2],font=('Radio Canada Big',10),bg='#273746',fg='snow')
                    texto.place(x=120,y=170,relwidth=0.25,relheight=0.06)
                    texto=Label(frame,text='QUANTITY:',font=('Radio Canada Big',10),bg='#273746',fg='snow')
                    texto.place(x=120,y=210,relwidth=0.25,relheight=0.06)
                    texto=Label(frame,text=REC[Y][3],font=('Radio Canada Big',10),bg='#273746',fg='snow')
                    texto.place(x=120,y=250,relwidth=0.25,relheight=0.06)
                    Y+=1
                    if Y>=1:
                        break
                else:
                    Y+=1
        except  IndexError:
            messagebox.showwarning("ERROR", "THERE ARE NO MORE RAW MATERIALS")
            Y=0
            Mcantidades()

        cuadro01=StringVar()

        texto=Label(frame,text='MODIFY PRODUCTS',font=('Radio Canada Big',16),bg='#273746',fg='snow')
        texto.place(relx=0.5,y=60,anchor=tk.CENTER,relwidth=1,relheight=0.10)
        texto=Label(frame,text='ENTER RAW MATERIAL NAME:',font=('Radio Canada Big',12),bg='#273746',fg='snow')
        texto.place(x=10,y=130,relwidth=0.75,relheight=0.06)
        cuadro0=Entry(frame,textvariable=cuadro01)
        cuadro0.place(x=500,y=130,relheight=0.06)
        Button2=Button(frame,text='CONFIRM',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:confirmar31111())
        Button2.place(x=540,y=360,relwidth=0.17,relheight=0.05)
        Button2=Button(frame,text='RETURN',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:menu311())
        Button2.place(x=40,y=360,relwidth=0.17,relheight=0.05)
        if VARIABLE == 1:
            messagebox.showerror("ERROR", "WRONG DATA ENTERED")
            VARIABLE=0
    def confirmar3111():
        global VARIABLE
        try:
            precio=float(cuadro0.get())
            cursor.execute('UPDATE PRODUCTO SET precioproducto = (?) WHERE codigoproducto = (?)',(precio,codigo))
            base.commit()
            VARIABLE=2
            menu311()
        except ValueError:
            VARIABLE=1
            Mpreciodecarta()  
    def Mpreciodecarta():
        eliminartodo()
        global frame,cuadro0,VARIABLE
        frame=Frame(raiz,width='700',height='430',bg='#273746')
        frame.pack()

        cuadro01=StringVar()

        texto=Label(frame,text='MODIFY PRODUCTS',font=('Radio Canada Big',16),bg='#273746',fg='snow')
        texto.place(relx=0.5,y=60,anchor=tk.CENTER,relwidth=1,relheight=0.10)
        texto=Label(frame,text='ENTER NEW MENU PRICE:',font=('Radio Canada Big',12),bg='#273746',fg='snow')
        texto.place(x=10,y=130,relwidth=0.75,relheight=0.06)
        cuadro0=Entry(frame,textvariable=cuadro01)
        cuadro0.place(x=500,y=130,relheight=0.06)
        Button2=Button(frame,text='CONFIRM',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:confirmar3111())
        Button2.place(x=540,y=360,relwidth=0.17,relheight=0.05)
        Button2=Button(frame,text='RETURN',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:menu311())
        Button2.place(x=40,y=360,relwidth=0.17,relheight=0.05)
        if VARIABLE == 1:
            messagebox.showerror("ERROR", "WRONG DATA ENTERED")
            VARIABLE=0
    def confirmar311():
        global VARIABLE,PRO,v
        try:
            producto=cuadro0.get()
            if producto == '':
                VARIABLE=1
                Mnombre()
            else:
                cursor.execute('UPDATE RECETA SET nombrereceta = (?) WHERE nombrereceta = (?)',(producto.upper(),PRO[v][1]))
                base.commit()
                cursor.execute('UPDATE PRODUCTO SET nombreproducto = (?) WHERE codigoproducto = (?)',(producto.upper(),codigo))
                base.commit()
                VARIABLE=2
                menu311()
        except ValueError:
            VARIABLE=1
            Mnombre() 
    def Mnombre():
        eliminartodo()
        global frame,cuadro0,VARIABLE
        frame=Frame(raiz,width='700',height='430',bg='#273746')
        frame.pack()

        cuadro01=StringVar()

        texto=Label(frame,text='MODIFY PRODUCTS',font=('Radio Canada Big',16),bg='#273746',fg='snow')
        texto.place(relx=0.5,y=60,anchor=tk.CENTER,relwidth=1,relheight=0.10)
        texto=Label(frame,text='ENTER NEW NAME:',font=('Radio Canada Big',12),bg='#273746',fg='snow')
        texto.place(x=10,y=130,relwidth=0.75,relheight=0.06)
        cuadro0=Entry(frame,textvariable=cuadro01)
        cuadro0.place(x=500,y=130,relheight=0.06)
        Button2=Button(frame,text='CONFIRM',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:confirmar311())
        Button2.place(x=540,y=360,relwidth=0.17,relheight=0.05)
        Button2=Button(frame,text='RETURN',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:menu311())
        Button2.place(x=40,y=360,relwidth=0.17,relheight=0.05)
        if VARIABLE == 1:
            messagebox.showerror("ERROR", "WRONG DATA ENTERED")
            VARIABLE=0
    def menu311():
        eliminartodo()
        global frame,cuadro0,VARIABLE,Y
        frame=Frame(raiz,width='700',height='430',bg='#273746')
        frame.pack()
        Y=0
        if VARIABLE == 2:
            messagebox.showinfo("CONGRATULATIONS", "DATA MODIFIED CORRECTLY")
            VARIABLE=0
        cursor.execute('SELECT * FROM PRODUCTO')
        PRO=cursor.fetchall()
        texto=Label(frame,text='MODIFY PRODUCTS',font=('Radio Canada Big',16),bg='#273746',fg='snow')
        texto.place(relx=0.5,y=60,anchor=tk.CENTER,relwidth=1,relheight=0.10)
        texto=Label(frame,text='PRODUCT NUMBER:',font=('Radio Canada Big',12),bg='#273746',fg='snow')
        texto.place(x=10,y=130,relwidth=0.75,relheight=0.06)
        texto=Label(frame,text=codMP,font=('Radio Canada Big',10),bg='#273746',fg='snow')
        texto.place(x=500,y=130,relwidth=0.25,relheight=0.06)
        Button2=Button(frame,text='MODIFY NAME',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:Mnombre())
        Button2.place(x=120,y=170,relwidth=0.5,relheight=0.05)
        texto=Label(frame,text=PRO[v][1],font=('Radio Canada Big',10),bg='#273746',fg='snow')
        texto.place(x=500,y=170,relwidth=0.25,relheight=0.06)
        Button2=Button(frame,text='MODIFY MENU PRICE',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:Mpreciodecarta())
        Button2.place(x=120,y=210,relwidth=0.5,relheight=0.05)
        texto=Label(frame,text=PRO[v][2],font=('Radio Canada Big',10),bg='#273746',fg='snow')
        texto.place(x=500,y=210,relwidth=0.25,relheight=0.06)
        Button2=Button(frame,text='MODIFY RAW MATERIALS QUANTITY',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:Mcantidades())
        Button2.place(x=120,y=250,relwidth=0.5,relheight=0.05)
        Button2=Button(frame,text='RETURN',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:menu31A())
        Button2.place(x=40,y=360,relwidth=0.17,relheight=0.05)
    def confirmar31():
        global codigo,VARIABLE,PRO,v,CONTADOR,VER,guarda,codMP
        try:
            codMP=int(cuadro0.get())
            #try:
            v=0
            cursor.execute('SELECT * FROM PRODUCTO')
            PRO=cursor.fetchall()
            codigo=PRO[codMP-1][0]
            VARIABLE=0
            while True:
                if codigo == PRO[v][0]:
                    VARIABLE=0
                    menu311()
                    break
                else:
                    v+=1
                if v == len(PRO):
                    VARIABLE=1
                    menu31()
                    break
            #except IndexError:
            #        VARIABLE=1
            #        menu31()
        except ValueError:
            VARIABLE=1
            menu31()
    def menu31():
        eliminartodo()
        global frame,cuadro0,VARIABLE,VER,f,guarda,x,PRO
        frame=Frame(raiz,width='700',height='430',bg='#273746')
        frame.pack()
        guarda=0

        cuadro01=StringVar()

        texto=Label(frame,text='MODIFY PRODUCTS',font=('Radio Canada Big',16),bg='#273746',fg='snow')
        texto.place(relx=0.5,y=60,anchor=tk.CENTER,relwidth=1,relheight=0.10)
        
        if VARIABLE == 1:
            messagebox.showerror("ERROR", "WRONG DATA ENTERED")
            VARIABLE=0
            guarda=1
            atrasMP()
        else:
            if VARIABLE == 2:
                messagebox.showinfo("CONGRATULATIONS", "DATA MODIFIED CORRECTLY")
                VARIABLE=0
                guarda=1
                atrasMP()
            else:
                cursor.execute('SELECT * FROM RECETA')
                REC=cursor.fetchall()
                cursor.execute('SELECT * FROM MATERIA_PRIMA')
                MP=cursor.fetchall()
                cursor.execute('SELECT * FROM PRODUCTO')
                PRO=cursor.fetchall()
                try:
                    x=0
                    f=40
                    while True:
                        x=0
                        v=0
                        while True:
                            # BUSCA EL PRODUCTO EN LA TABLA DE RECETAS
                            if PRO[VER][1] == REC[x][1]:
                                z=0
                                while True:
                                    # BUSCA LA MATERIA PRIMA DEL PRODUCTO
                                    if REC[x][2] == MP[z][1]:
                                        # ES COMPRADA
                                        if MP[z][4] == 'C':
                                            v+=(MP[z][3]*REC[x][3])
                                            break
                                        else:
                                            w=0
                                            # ES ELABORADA ASI QUE BUSCA LA MATERIA PRIMA EN LA TABLA DE RECETAS
                                            while True:
                                                if MP[z][1] == REC[w][1]:
                                                    u=0
                                                    t=0
                                                    while True:
                                                        # BUSCA LA MATERIA PRIMA DE LA MPE
                                                        if REC[w][2] == MP[u][1]:
                                                            while True:
                                                                if MP[u][1]==REC[t][2]:
                                                                    break
                                                                else:
                                                                    t+=1
                                                                if t == len(REC):
                                                                    break
                                                            v+=(REC[x][3]*(MP[u][3]*REC[w][3])/REC[t][3])
                                                            break
                                                        else:
                                                            u+=1
                                                        if u == len(MP):
                                                            break
                                                    w+=1
                                                else:
                                                    w+=1
                                                if w == len(REC):
                                                    break
                                        break
                                    else:
                                        z+=1
                                    if z == len(MP):
                                        break
                                x+=1
                            else:
                                x+=1
                            if x == len(REC):
                                break
                        texto=Label(frame,text=VER+1,font=('Radio Canada Big',10),bg='#273746',fg='snow')
                        texto.place(x=10+x,y=170+f,relwidth=0.15,relheight=0.06)
                        texto=Label(frame,text=PRO[VER][1],font=('Radio Canada Big',10),bg='#273746',fg='snow')
                        texto.place(x=120+x,y=170+f,relwidth=0.15,relheight=0.06)
                        VER+=1
                        f+=40
                        if VER % 6 == 0:
                            break
                        if VER % 3 == 0:
                            f=40
                            x=350
                            continue
                except IndexError:
                    if VER == 0:
                            messagebox.showwarning("ERROR", "THERE ARE NO PRODUCTS")
                            frame.destroy()
                    if f == 40 and x == 0:
                        guarda=1
                        if CONTADOR > 0:
                            messagebox.showwarning("ERROR", "THERE ARE NO MORE PRODUCTS")
                            atrasMP()
        if VER>0:
            texto=Label(frame,text='ENTER PRODUCT CODE:',font=('Radio Canada Big',12),bg='#273746',fg='snow')
            texto.place(x=10,y=130,relwidth=0.75,relheight=0.06)
            cuadro0=Entry(frame,textvariable=cuadro01)
            cuadro0.place(x=500,y=130,relheight=0.06)
            Button2=Button(frame,text='CONFIRM',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:confirmar31())
            Button2.place(x=540,y=360,relwidth=0.17,relheight=0.05)
        try:
            if PRO[VER][0]==4:
                pass
            Button2=Button(frame,text='NEXT',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:siguienteMP())
            Button2.place(x=180,y=360,relwidth=0.17,relheight=0.05)
        except IndexError:
            pass
        if CONTADOR>0:
            Button2=Button(frame,text='BACK',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:atrasMP())
            Button2.place(x=40,y=360,relwidth=0.17,relheight=0.05)
    # MODIFICAR DATOS DE MATERIA PRIMA
    def menu32A():
        eliminartodo()
        menu32()
    def siguienteMMP():
        global CONTADOR
        CONTADOR+=1
        menu32()
    def atrasMMP():
        global VER,CONTADOR,f,guarda,x
        if guarda == 1:
            CONTADOR=0
            VER=0
            guarda=0
            menu32()
        else:
            if CONTADOR > 0:
                if x == 0:
                    if f == 80:
                        VER-=7
                    if f == 120:
                        VER-=8
                    if f == 160:
                        VER-=9
                if x == 350:
                    if f == 40:
                        VER-=9
                    if f == 80:
                        VER-=10
                    if f == 120:
                        VER-=11
                    if f == 160:
                        VER-=12
                CONTADOR-=1
            else:
                VER=0
            menu32()
    def confirmarMP1():
        global VARIABLE,cantidad,REC,MP,Y
        try:
            cantidad=float(cuadro0.get())
            cursor.execute('UPDATE RECETA SET cantidadmateriaprima = (?) WHERE nombrereceta = (?) AND nombremateriaprimareceta = (?)',(cantidad,MP[v][1],REC[Y][2]))
            base.commit()
            VARIABLE=2
            menu322()
        except ValueError:
            VARIABLE=1
            MPcantidades()
    def menuMP():
        eliminartodo()
        global frame,cuadro0,VARIABLE,REC,PRO,Y
        frame=Frame(raiz,width='700',height='430',bg='#273746')
        frame.pack()

        cuadro01=StringVar()

        texto=Label(frame,text='MODIFY RAW MATERIALS',font=('Radio Canada Big',16),bg='#273746',fg='snow')
        texto.place(relx=0.5,y=60,anchor=tk.CENTER,relwidth=1,relheight=0.10)
        texto=Label(frame,text='ENTER NEW QUANTITY:',font=('Radio Canada Big',12),bg='#273746',fg='snow')
        texto.place(x=10,y=130,relwidth=0.75,relheight=0.06)
        cuadro0=Entry(frame,textvariable=cuadro01)
        cuadro0.place(x=500,y=130,relheight=0.06)
        Button2=Button(frame,text='CONFIRM',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:confirmarMP1())
        Button2.place(x=540,y=360,relwidth=0.17,relheight=0.05)
        Button2=Button(frame,text='BACK',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:menu322())
        Button2.place(x=40,y=360,relwidth=0.17,relheight=0.05)
        if VARIABLE == 1:
            messagebox.showerror("ERROR", "WRONG DATA ENTERED")
            VARIABLE=0
    def confirmarMP():
        global VARIABLE,opcion,REC,MP,Y
        cursor.execute('SELECT * FROM RECETA')
        REC=cursor.fetchall()
        cursor.execute('SELECT * FROM MATERIA_PRIMA')
        MP=cursor.fetchall()
        Y=0
        v=0
        bandera=0
        try:
            opcion=cuadro0.get()
            if opcion == '':
                VARIABLE=1
                MPcantidades()
            else:
                while True:
                    if MP[v][0] == codigo:
                        while True:
                            if REC[Y][1] == MP[v][1]:
                                if opcion.upper() == REC[Y][2]:
                                    VARIABLE=0
                                    bandera = 1
                                    menuMP()
                                    break
                                else:
                                    Y+=1
                                    break
                            else:
                                Y+=1
                        if bandera == 1:
                            break
                    else:
                        v+=1
        except ValueError:
            VARIABLE=1
            MPcantidades()
    def MPcantidades():
        eliminartodo()
        global frame,cuadro0,VARIABLE,Y
        frame=Frame(raiz,width='700',height='430',bg='#273746')
        frame.pack()

        cursor.execute('SELECT * FROM MATERIA_PRIMA')
        MP=cursor.fetchall()
        cursor.execute('SELECT * FROM RECETA')
        REC=cursor.fetchall()
        Button2=Button(frame,text='NEXT',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:MPcantidades())
        Button2.place(x=180,y=360,relwidth=0.17,relheight=0.05)
        try:
            while True:
                if REC[Y][1] == MP[v][1]:
                    texto=Label(frame,text=REC[Y][2],font=('Radio Canada Big',10),bg='#273746',fg='snow')
                    texto.place(x=120,y=170,relwidth=0.25,relheight=0.06)
                    texto=Label(frame,text='QUANTITY:',font=('Radio Canada Big',10),bg='#273746',fg='snow')
                    texto.place(x=120,y=210,relwidth=0.25,relheight=0.06)
                    texto=Label(frame,text=REC[Y][3],font=('Radio Canada Big',10),bg='#273746',fg='snow')
                    texto.place(x=120,y=250,relwidth=0.25,relheight=0.06)
                    Y+=1
                    if Y>=1:
                        break
                else:
                    Y+=1
        except  IndexError:
            messagebox.showwarning("ERROR", "THERE ARE NO MORE RAW MATERIALS")
            Y=0
            MPcantidades()

        cuadro01=StringVar()

        texto=Label(frame,text='MODIFY RAW MATERIALS',font=('Radio Canada Big',16),bg='#273746',fg='snow')
        texto.place(relx=0.5,y=60,anchor=tk.CENTER,relwidth=1,relheight=0.10)
        texto=Label(frame,text='ENTER RAW MATERIAL NAME:',font=('Radio Canada Big',12),bg='#273746',fg='snow')
        texto.place(x=10,y=130,relwidth=0.75,relheight=0.06)
        cuadro0=Entry(frame,textvariable=cuadro01)
        cuadro0.place(x=500,y=130,relheight=0.06)
        Button2=Button(frame,text='CONFIRM',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:confirmarMP())
        Button2.place(x=540,y=360,relwidth=0.17,relheight=0.05)
        Button2=Button(frame,text='RETURN',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:menu322())
        Button2.place(x=40,y=360,relwidth=0.17,relheight=0.05)
        if VARIABLE == 1:
            messagebox.showerror("ERROR", "WRONG DATA ENTERED")
            VARIABLE=0
    def confirmar3222222():
        global VARIABLE,cant
        try:
            cant=float(cuadro0.get())
            cursor.execute('UPDATE MATERIA_PRIMA SET cantidadmateriaprima = (?) WHERE codigomateriaprima = (?)',(cant,codigo))
            base.commit()
            VARIABLE=2
            menu322()
        except ValueError:
            VARIABLE=1
            MPcantidad()
    def MPcantidad():
        eliminartodo()
        global frame,cuadro0,VARIABLE
        frame=Frame(raiz,width='700',height='430',bg='#273746')
        frame.pack()
        cuadro01=StringVar()

        texto=Label(frame,text='MODIFY RAW MATERIALS',font=('Radio Canada Big',16),bg='#273746',fg='snow')
        texto.place(relx=0.5,y=60,anchor=tk.CENTER,relwidth=1,relheight=0.10)
        texto=Label(frame,text='ENTER NEW QUANTITY:',font=('Radio Canada Big',12),bg='#273746',fg='snow')
        texto.place(x=10,y=130,relwidth=0.75,relheight=0.06)
        cuadro0=Entry(frame,textvariable=cuadro01)
        cuadro0.place(x=500,y=130,relheight=0.06)
        Button2=Button(frame,text='CONFIRM',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:confirmar3222222())
        Button2.place(x=540,y=360,relwidth=0.17,relheight=0.05)
        Button2=Button(frame,text='RETURN',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:menu322())
        Button2.place(x=40,y=360,relwidth=0.17,relheight=0.05)
        if VARIABLE == 1:
            messagebox.showerror("ERROR", "WRONG DATA ENTERED")
            VARIABLE=0
    def confirmar322222():
        global VARIABLE,precio
        try:
            precio=float(cuadro0.get())
            cursor.execute('SELECT * FROM MATERIA_PRIMA')
            MP=cursor.fetchall()
            cursor.execute('SELECT * FROM RECETA')
            REC=cursor.fetchall()
            v=0
            while True:
                if codigo == MP[v][0]:
                    w=0
                    while True:
                        if MP[v][1] == REC[w][2]:
                            p=0
                            while True:
                                if REC[w][1] == MP[p][1]:
                                    cursor.execute('UPDATE MATERIA_PRIMA SET preciomateriaprima = (?) WHERE codigomateriaprima = (?)',(MP[p][3]-(MP[v][3]*REC[w][3]/MP[p][5]),MP[p][0]))
                                    base.commit()
                                    break
                                else:
                                    p+=1
                                if p == len(MP):
                                    break
                            w+=1
                        else:
                            w+=1
                        if w == len(REC):
                            break
                    break
                else:
                    v+=1
                if v == len(MP):
                    break
            cursor.execute('UPDATE MATERIA_PRIMA SET preciomateriaprima = (?) WHERE codigomateriaprima = (?)',(precio,codigo))
            base.commit()
            cursor.execute('SELECT * FROM MATERIA_PRIMA')
            MP=cursor.fetchall()
            cursor.execute('SELECT * FROM RECETA')
            REC=cursor.fetchall()
            v=0
            while True:
                if codigo == MP[v][0]:
                    w=0
                    while True:
                        if MP[v][1] == REC[w][2]:
                            p=0
                            while True:
                                if REC[w][1] == MP[p][1]:
                                    cursor.execute('UPDATE MATERIA_PRIMA SET preciomateriaprima = (?) WHERE codigomateriaprima = (?)',(MP[p][3]+(MP[v][3]*REC[w][3]/MP[p][5]),MP[p][0]))
                                    base.commit()
                                    break
                                else:
                                    p+=1
                                if p == len(MP):
                                    break
                            w+=1
                        else:
                            w+=1
                        if w == len(REC):
                            break
                    break
                else:
                    v+=1
                if v == len(MP):
                    break
            VARIABLE=2
            menu322()
        except ValueError:
            VARIABLE=1
            MPprecio()
    def MPprecio():
        eliminartodo()
        global frame,cuadro0,VARIABLE
        frame=Frame(raiz,width='700',height='430',bg='#273746')
        frame.pack()

        cuadro01=StringVar()

        texto=Label(frame,text='MODIFY RAW MATERIALS',font=('Radio Canada Big',16),bg='#273746',fg='snow')
        texto.place(relx=0.5,y=60,anchor=tk.CENTER,relwidth=1,relheight=0.10)
        texto=Label(frame,text='ENTER NEW PRICE:',font=('Radio Canada Big',12),bg='#273746',fg='snow')
        texto.place(x=10,y=130,relwidth=0.75,relheight=0.06)
        cuadro0=Entry(frame,textvariable=cuadro01)
        cuadro0.place(x=500,y=130,relheight=0.06)
        Button2=Button(frame,text='CONFIRM',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:confirmar322222())
        Button2.place(x=540,y=360,relwidth=0.17,relheight=0.05)
        Button2=Button(frame,text='RETURN',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:menu322())
        Button2.place(x=40,y=360,relwidth=0.17,relheight=0.05)
        if VARIABLE == 1:
            messagebox.showerror("ERROR", "WRONG DATA ENTERED")
            VARIABLE=0
    def confirmar3222():
        global VARIABLE,unidad
        try:
            unidad=cuadro0.get()
            if unidad.isalpha() == True:
                cursor.execute('UPDATE MATERIA_PRIMA SET unidadmateriaprima = (?) WHERE codigomateriaprima = (?)',(unidad.upper(),codigo))
                base.commit()
                VARIABLE=2
                menu322()
            else:
                VARIABLE=1
                MPunidaddemedida()
        except ValueError:
            VARIABLE=1
            MPunidaddemedida()  
    def MPunidaddemedida():
        eliminartodo()
        global frame,cuadro0,VARIABLE
        frame=Frame(raiz,width='700',height='430',bg='#273746')
        frame.pack()

        cuadro01=StringVar()

        texto=Label(frame,text='MODIFY RAW MATERIALS',font=('Radio Canada Big',16),bg='#273746',fg='snow')
        texto.place(relx=0.5,y=60,anchor=tk.CENTER,relwidth=1,relheight=0.10)
        texto=Label(frame,text='ENTER NEW UNIT OF MEASURE:',font=('Radio Canada Big',12),bg='#273746',fg='snow')
        texto.place(x=10,y=130,relwidth=0.75,relheight=0.06)
        cuadro0=Entry(frame,textvariable=cuadro01)
        cuadro0.place(x=500,y=130,relheight=0.06)
        Button2=Button(frame,text='CONFIRM',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:confirmar3222())
        Button2.place(x=540,y=360,relwidth=0.17,relheight=0.05)
        Button2=Button(frame,text='RETURN',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:menu322())
        Button2.place(x=40,y=360,relwidth=0.17,relheight=0.05)
        if VARIABLE == 1:
            messagebox.showerror("ERROR", "WRONG DATA ENTERED")
            VARIABLE=0
    def confirmar322():
        global VARIABLE,materiaprima
        try:
            materiaprima=cuadro0.get()
            if materiaprima == '':
                VARIABLE=1
                MPnombre()
            else:
                cursor.execute('UPDATE RECETA SET nombrereceta = (?) WHERE nombrereceta = (?)',(materiaprima.upper(),MP[v][1]))
                base.commit()
                cursor.execute('UPDATE RECETA SET nombremateriaprimareceta = (?) WHERE nombremateriaprimareceta = (?)',(materiaprima.upper(),MP[v][1]))
                base.commit()
                cursor.execute('UPDATE MATERIA_PRIMA SET nombremateriaprima = (?) WHERE codigomateriaprima = (?)',(materiaprima.upper(),codigo))
                base.commit()
                VARIABLE=2
                menu322()
        except ValueError:
            VARIABLE=1
            MPnombre()  
    def MPnombre():
        eliminartodo()
        global frame,cuadro0,VARIABLE
        frame=Frame(raiz,width='700',height='430',bg='#273746')
        frame.pack()

        cuadro01=StringVar()

        texto=Label(frame,text='MODIFY RAW MATERIALS',font=('Radio Canada Big',16),bg='#273746',fg='snow')
        texto.place(relx=0.5,y=60,anchor=tk.CENTER,relwidth=1,relheight=0.10)
        texto=Label(frame,text='ENTER NEW NAME:',font=('Radio Canada Big',12),bg='#273746',fg='snow')
        texto.place(x=10,y=130,relwidth=0.75,relheight=0.06)
        cuadro0=Entry(frame,textvariable=cuadro01)
        cuadro0.place(x=500,y=130,relheight=0.06)
        Button2=Button(frame,text='CONFIRM',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:confirmar322())
        Button2.place(x=540,y=360,relwidth=0.17,relheight=0.05)
        Button2=Button(frame,text='RETURN',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:menu322())
        Button2.place(x=40,y=360,relwidth=0.17,relheight=0.05)
        if VARIABLE == 1:
            messagebox.showerror("ERROR", "WRONG DATA ENTERED")
            VARIABLE=0
    def menu322():
        eliminartodo()
        global frame,cuadro0,VARIABLE,Y
        Y=0
        frame=Frame(raiz,width='700',height='430',bg='#273746')
        frame.pack()
        cursor.execute('SELECT * FROM MATERIA_PRIMA')
        MP=cursor.fetchall()
        texto=Label(frame,text='MODIFY RAW MATERIAL',font=('Radio Canada Big',16),bg='#273746',fg='snow')
        texto.place(relx=0.5,y=60,anchor=tk.CENTER,relwidth=1,relheight=0.10)
        texto=Label(frame,text='RAW MATERIAL NUMBER:',font=('Radio Canada Big',12),bg='#273746',fg='snow')
        texto.place(x=10,y=130,relwidth=0.75,relheight=0.06)
        texto=Label(frame,text=codMMP,font=('Radio Canada Big',10),bg='#273746',fg='snow')
        texto.place(x=500,y=130,relwidth=0.25,relheight=0.06)
        Button2=Button(frame,text='MODIFY NAME',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:MPnombre())
        Button2.place(x=120,y=170,relwidth=0.5,relheight=0.05)
        texto=Label(frame,text=MP[v][1],font=('Radio Canada Big',10),bg='#273746',fg='snow')
        texto.place(x=500,y=170,relwidth=0.25,relheight=0.06)
        Button2=Button(frame,text='MODIFY UNIT OF MEASURE',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:MPunidaddemedida())
        Button2.place(x=120,y=210,relwidth=0.5,relheight=0.05)
        texto=Label(frame,text=MP[v][2],font=('Radio Canada Big',10),bg='#273746',fg='snow')
        texto.place(x=500,y=210,relwidth=0.25,relheight=0.06)
        if MP[v][4]=='C':
            Button2=Button(frame,text='MODIFY PRICE',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:MPprecio())
            Button2.place(x=120,y=250,relwidth=0.5,relheight=0.05)
            texto=Label(frame,text='${:.2f}'.format(MP[v][3]),font=('Radio Canada Big',10),bg='#273746',fg='snow')
            texto.place(x=500,y=250,relwidth=0.25,relheight=0.06)
        else:
            Button2=Button(frame,text='MODIFY QUANTITY',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:MPcantidad())
            Button2.place(x=120,y=250,relwidth=0.5,relheight=0.05)
            texto=Label(frame,text=MP[v][5],font=('Radio Canada Big',10),bg='#273746',fg='snow')
            texto.place(x=500,y=250,relwidth=0.25,relheight=0.06)
            Button2=Button(frame,text='MODIFY RAW MATERIALS QUANTITY',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:MPcantidades())
            Button2.place(x=120,y=290,relwidth=0.5,relheight=0.05)
        Button2=Button(frame,text='RETURN',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:menu32A())
        Button2.place(x=40,y=360,relwidth=0.17,relheight=0.05)
        if VARIABLE == 2:
            messagebox.showinfo("CONGRATULATIONS", "DATA ADDED CORRECTLY")
            VARIABLE=0
    def confirmar32():
        global codigo,VARIABLE,MP,v,CONTADOR,VER,guarda,codMMP
        try:
            codMMP=int(cuadro0.get())
            try:
                v=0
                cursor.execute('SELECT * FROM MATERIA_PRIMA')
                MP=cursor.fetchall()
                codigo=MP[codMMP-1][0]
                VARIABLE=0
                while True:
                    if codigo == MP[v][0]:
                        VARIABLE=0
                        menu322()
                        break
                    else:
                        v+=1
                    if v == len(MP):
                        VARIABLE=1
                        menu32()
                        break
            except IndexError:
                    VARIABLE=1
                    menu32()
        except ValueError:
            VARIABLE=1
            menu32()
    def menu32():
        eliminartodoMENOSUNO()
        global frame,cuadro0,VARIABLE,VER,f,guarda,x,MP
        frame=Frame(raiz,width='700',height='430',bg='#273746')
        frame.pack()
        guarda=0

        cuadro01=StringVar()

        texto=Label(frame,text='MODIFY RAW MATERIALS',font=('Radio Canada Big',16),bg='#273746',fg='snow')
        texto.place(relx=0.5,y=60,anchor=tk.CENTER,relwidth=1,relheight=0.10)
        
        if VARIABLE == 1:
            messagebox.showerror("ERROR", "WRONG DATA ENTERED")
            VARIABLE=0
            guarda=1
            atrasMMP()
        else:
            if VARIABLE == 2:
                messagebox.showinfo("CONGRATULATIONS", "DATA MODIFIED CORRECTLY")
                VARIABLE=0
                guarda=1
                atrasMMP()
            else:
                cursor.execute('SELECT * FROM MATERIA_PRIMA')
                MP=cursor.fetchall()
                cursor.execute('SELECT * FROM RECETA')
                REC=cursor.fetchall()
                try:
                    x=0
                    f=40
                    while True:
                        t=0
                        if MP[VER][4] == 'E':
                            w=0
                            # ES ELABORADA ASI QUE BUSCA LA MATERIA PRIMA EN LA TABLA DE RECETAS
                            while True:
                                if MP[VER][1] == REC[w][1]:
                                    u=0
                                    while True:
                                        z=0
                                        # BUSCA LA MATERIA PRIMA DE LA MPE
                                        if REC[w][2] == MP[u][1]:
                                            while True:
                                                if MP[u][1]==REC[z][2]:
                                                    break
                                                else:
                                                    z+=1
                                                if z == len(REC):
                                                    break
                                            t+=(1*(MP[u][3]*REC[w][3])/REC[z][3])
                                            break
                                        else:
                                            u+=1
                                        if u == len(MP):
                                            break
                                    w+=1
                                else:
                                    w+=1
                                if w == len(REC):
                                    break
                        texto=Label(frame,text=VER+1,font=('Radio Canada Big',10),bg='#273746',fg='snow')
                        texto.place(x=10+x,y=170+f,relwidth=0.2,relheight=0.06)
                        texto=Label(frame,text=MP[VER][1],font=('Radio Canada Big',10),bg='#273746',fg='snow')
                        texto.place(x=140+x,y=170+f,relwidth=0.2,relheight=0.06)
                        VER+=1
                        f+=40
                        if VER % 6 == 0:
                            break
                        if VER % 3 == 0:
                            f=40
                            x=350
                            continue
                except IndexError:
                    if VER == 0:
                        messagebox.showwarning("ERROR", "THERE ARE NO RAW MATERIALS")
                        frame.destroy()
                    if f == 40 and x == 0:
                        guarda=1
                        if CONTADOR > 0:
                            messagebox.showwarning("ERROR", "THERE ARE NO MORE RAW MATERIALS")
                            atrasMMP()
        if VER>0:
            texto=Label(frame,text='ENTER RAW MATERIAL CODE:',font=('Radio Canada Big',12),bg='#273746',fg='snow')
            texto.place(x=10,y=130,relwidth=0.75,relheight=0.06)
            cuadro0=Entry(frame,textvariable=cuadro01)
            cuadro0.place(x=500,y=130,relheight=0.06)
            Button2=Button(frame,text='CONFIRM',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:confirmar32())
            Button2.place(x=540,y=360,relwidth=0.17,relheight=0.05)
        try:
            if MP[VER][0]==4:
                pass
            Button2=Button(frame,text='NEXT',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:siguienteMMP())
            Button2.place(x=180,y=360,relwidth=0.17,relheight=0.05)
        except IndexError:
            pass
        if CONTADOR>0:
            Button2=Button(frame,text='BACK',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:atrasMMP())
            Button2.place(x=40,y=360,relwidth=0.17,relheight=0.05)
    #################################################################################################################################################################
    #################################################################################################################################################################
    # ELIMINAR DATOS DE PRODUCTO
    def menu41A():
        eliminartodo()
        menu41()
    def siguienteEP():
        global CONTADOR
        CONTADOR+=1
        menu41()
    def atrasEP():
        global VER,CONTADOR,f,guarda,x
        if guarda == 1:
            CONTADOR=0
            VER=0
            guarda=0
            menu41()
        else:
            if CONTADOR > 0:
                if x == 0:
                    if f == 80:
                        VER-=7
                    if f == 120:
                        VER-=8
                    if f == 160:
                        VER-=9
                if x == 350:
                    if f == 40:
                        VER-=9
                    if f == 80:
                        VER-=10
                    if f == 120:
                        VER-=11
                    if f == 160:
                        VER-=12
                CONTADOR-=1
            else:
                VER=0
            menu41()
    def confirmar41():
        global codigo,VARIABLE,PRO,v,CONTADOR,VER,guarda
        try:
            cod=int(cuadro0.get())
            try:
                v=0
                cursor.execute('SELECT * FROM PRODUCTO')
                PRO=cursor.fetchall()
                codigo=PRO[cod-1][0]
                VARIABLE=0
                while True:
                    if codigo == PRO[v][0]:
                        VARIABLE=2
                        cursor.execute('DELETE FROM RECETA WHERE nombrereceta == (?)',(PRO[v][1],))
                        base.commit()
                        cursor.execute('DELETE FROM PRODUCTO WHERE codigoproducto == (?)',(PRO[v][0],))
                        base.commit()
                        guarda=1
                        atrasEP()
                        break
                    else:
                        v+=1
                    if v == len(PRO):
                        VARIABLE=1
                        menu41()
                        break
            except IndexError:
                    VARIABLE=1
                    menu41()
        except ValueError:
            VARIABLE=1
            menu41()
    def menu41():
        eliminartodoMENOSUNO()
        global frame,cuadro0,VARIABLE,VER,f,guarda,x,PRO
        frame=Frame(raiz,width='700',height='430',bg='#273746')
        frame.pack()
        guarda=0

        cuadro01=StringVar()

        texto=Label(frame,text='DELETE PRODUCTS',font=('Radio Canada Big',16),bg='#273746',fg='snow')
        texto.place(relx=0.5,y=60,anchor=tk.CENTER,relwidth=1,relheight=0.10)

        if VARIABLE == 1:
            messagebox.showerror("ERROR", "WRONG DATA ENTERED")
            VARIABLE=0
            guarda=1
            atrasEP()
        else:
            if VARIABLE == 2:
                messagebox.showinfo("CONGRATULATIONS", "DATA DELETED CORRECTLY")
                VARIABLE=0
                guarda=1
                atrasEP()
            else:
                cursor.execute('SELECT * FROM RECETA')
                REC=cursor.fetchall()
                cursor.execute('SELECT * FROM MATERIA_PRIMA')
                MP=cursor.fetchall()
                cursor.execute('SELECT * FROM PRODUCTO')
                PRO=cursor.fetchall()
                try:
                    x=0
                    f=40
                    while True:
                        x=0
                        v=0
                        while True:
                            # BUSCA EL PRODUCTO EN LA TABLA DE RECETAS
                            if PRO[VER][1] == REC[x][1]:
                                z=0
                                while True:
                                    # BUSCA LA MATERIA PRIMA DEL PRODUCTO
                                    if REC[x][2] == MP[z][1]:
                                        # ES COMPRADA
                                        if MP[z][4] == 'C':
                                            v+=(MP[z][3]*REC[x][3])
                                            break
                                        else:
                                            w=0
                                            # ES ELABORADA ASI QUE BUSCA LA MATERIA PRIMA EN LA TABLA DE RECETAS
                                            while True:
                                                if MP[z][1] == REC[w][1]:
                                                    u=0
                                                    t=0
                                                    while True:
                                                        # BUSCA LA MATERIA PRIMA DE LA MPE
                                                        if REC[w][2] == MP[u][1]:
                                                            while True:
                                                                if MP[u][1]==REC[t][2]:
                                                                    break
                                                                else:
                                                                    t+=1
                                                                if t == len(REC):
                                                                    break
                                                            v+=(REC[x][3]*(MP[u][3]*REC[w][3])/REC[t][3])
                                                            break
                                                        else:
                                                            u+=1
                                                        if u == len(MP):
                                                            break
                                                    w+=1
                                                else:
                                                    w+=1
                                                if w == len(REC):
                                                    break
                                        break
                                    else:
                                        z+=1
                                    if z == len(MP):
                                        break
                                x+=1
                            else:
                                x+=1
                            if x == len(REC):
                                break
                        texto=Label(frame,text=VER+1,font=('Radio Canada Big',10),bg='#273746',fg='snow')
                        texto.place(x=10+x,y=170+f,relwidth=0.15,relheight=0.06)
                        texto=Label(frame,text=PRO[VER][1],font=('Radio Canada Big',10),bg='#273746',fg='snow')
                        texto.place(x=120+x,y=170+f,relwidth=0.15,relheight=0.06)
                        VER+=1
                        f+=40
                        if VER % 6 == 0:
                            break
                        if VER % 3 == 0:
                            f=40
                            x=350
                            continue
                except IndexError:
                    if VER == 0:
                            messagebox.showwarning("ERROR", "THERE ARE NO PRODUCTS")
                            frame.destroy()
                    if f == 40 and x == 0:
                        guarda=1
                        if CONTADOR > 0:
                            messagebox.showwarning("ERROR", "THERE ARE NO MORE PRODUCTS")
                            atrasEP()
        if VER>0:
            texto=Label(frame,text='ENTER PRODUCT CODE:',font=('Radio Canada Big',12),bg='#273746',fg='snow')
            texto.place(x=10,y=130,relwidth=0.75,relheight=0.06)
            cuadro0=Entry(frame,textvariable=cuadro01)
            cuadro0.place(x=500,y=130,relheight=0.06)
            Button2=Button(frame,text='CONFIRM',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:confirmar41())
            Button2.place(x=540,y=360,relwidth=0.17,relheight=0.05)
        try:
            if PRO[VER][0]==4:
                pass
            Button2=Button(frame,text='NEXT',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:siguienteEP())
            Button2.place(x=180,y=360,relwidth=0.17,relheight=0.05)
        except IndexError:
            pass
        if CONTADOR>0:
            Button2=Button(frame,text='BACK',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:atrasEP())
            Button2.place(x=40,y=360,relwidth=0.17,relheight=0.05)
    # ELIMINAR DATOS DE MATERIA PRIMA
    def menu42A():
        eliminartodo()
        menu42()
    def siguienteEMP():
        global CONTADOR
        CONTADOR+=1
        menu42()
    def atrasEMP():
        global VER,CONTADOR,f,guarda,x
        if guarda == 1:
            CONTADOR=0
            VER=0
            guarda=0
            menu42()
        else:
            if CONTADOR > 0:
                if x == 0:
                    if f == 80:
                        VER-=7
                    if f == 120:
                        VER-=8
                    if f == 160:
                        VER-=9
                if x == 350:
                    if f == 40:
                        VER-=9
                    if f == 80:
                        VER-=10
                    if f == 120:
                        VER-=11
                    if f == 160:
                        VER-=12
                CONTADOR-=1
            else:
                VER=0
            menu42()
    def confirmar42():
        global codigo,VARIABLE,MP,v,CONTADOR,VER,guarda
        try:
            cod=int(cuadro0.get())
            try:
                cursor.execute('SELECT * FROM MATERIA_PRIMA')
                MP=cursor.fetchall()
                cursor.execute('SELECT * FROM RECETA')
                REC=cursor.fetchall()
                codigo=MP[cod-1][0]
                v=0
                u=0
                VARIABLE=0
                while True:
                    if codigo == MP[v][0]:
                        try:
                            while True:
                                if MP[v][1] == REC[u][2]:
                                    VARIABLE=3
                                    menu42()
                                    break
                                else:
                                    u+=1
                                if u == len(REC):
                                    VARIABLE=2
                                    cursor.execute('DELETE FROM RECETA WHERE nombrereceta == (?)',(MP[v][1],))
                                    base.commit()
                                    cursor.execute('DELETE FROM MATERIA_PRIMA WHERE codigomateriaprima == (?)',(MP[v][0],))
                                    base.commit()
                                    guarda=1
                                    atrasEMP()
                                    break
                        except IndexError:
                            cursor.execute('DELETE FROM MATERIA_PRIMA WHERE codigomateriaprima == (?)',(MP[v][0],))
                            base.commit()
                            guarda=1
                            VARIABLE=2
                            atrasEMP()
                        break
                    else:
                        v+=1
                    if v == len(MP):
                        VARIABLE=1
                        menu42()
                        break
            except IndexError:
                VARIABLE=1
                menu42()
        except ValueError:
            VARIABLE=1
            menu42()
    def menu42():
        eliminartodoMENOSUNO()
        global frame,cuadro0,VARIABLE,VER,f,guarda,x,MP
        frame=Frame(raiz,width='700',height='430',bg='#273746')
        frame.pack()
        guarda=0

        cuadro01=StringVar()

        texto=Label(frame,text='DELETE RAW MATERIALS',font=('Radio Canada Big',16),bg='#273746',fg='snow')
        texto.place(relx=0.5,y=60,anchor=tk.CENTER,relwidth=1,relheight=0.10)

        if VARIABLE == 1:
            messagebox.showerror("ERROR", "WRONG DATA ENTERED")
            VARIABLE=0
            guarda=1
            atrasEMP()
        else:
            if VARIABLE == 2:
                messagebox.showinfo("CONGRATULATIONS", "DATA DELETED CORRECTLY")
                VARIABLE=0
                guarda=1
                atrasEMP()
            else:   
                if VARIABLE == 3:
                    messagebox.showwarning("ERROR", "THE DATA CAN NOT BE DELETED")
                    VARIABLE=0
                    guarda=1
                    atrasEMP()
                else:
                    cursor.execute('SELECT * FROM MATERIA_PRIMA')
                    MP=cursor.fetchall()
                    cursor.execute('SELECT * FROM RECETA')
                    REC=cursor.fetchall()
                    try:
                        x=0
                        f=40
                        while True:
                            t=0
                            if MP[VER][4] == 'E':
                                w=0
                                # ES ELABORADA ASI QUE BUSCA LA MATERIA PRIMA EN LA TABLA DE RECETAS
                                while True:
                                    if MP[VER][1] == REC[w][1]:
                                        u=0
                                        while True:
                                            z=0
                                            # BUSCA LA MATERIA PRIMA DE LA MPE
                                            if REC[w][2] == MP[u][1]:
                                                while True:
                                                    if MP[u][1]==REC[z][2]:
                                                        break
                                                    else:
                                                        z+=1
                                                    if z == len(REC):
                                                        break
                                                t+=(1*(MP[u][3]*REC[w][3])/REC[z][3])
                                                break
                                            else:
                                                u+=1
                                            if u == len(MP):
                                                break
                                        w+=1
                                    else:
                                        w+=1
                                    if w == len(REC):
                                        break
                            texto=Label(frame,text=VER+1,font=('Radio Canada Big',10),bg='#273746',fg='snow')
                            texto.place(x=10+x,y=170+f,relwidth=0.2,relheight=0.06)
                            texto=Label(frame,text=MP[VER][1],font=('Radio Canada Big',10),bg='#273746',fg='snow')
                            texto.place(x=140+x,y=170+f,relwidth=0.2,relheight=0.06)
                            VER+=1
                            f+=40
                            if VER % 6 == 0:
                                break
                            if VER % 3 == 0:
                                f=40
                                x=350
                                continue
                    except IndexError:
                        if VER == 0:
                            messagebox.showwarning("ERROR", "THERE ARE NO RAW MATERIALS")
                            frame.destroy()
                        if f == 40 and x == 0:
                            guarda=1
                            if CONTADOR > 0:
                                messagebox.showwarning("ERROR", "THERE ARE NO MORE RAW MATERIALS")
                                atrasEMP()
        if VER>0:
            texto=Label(frame,text='ENTER RAW MATERIAL CODE:',font=('Radio Canada Big',12),bg='#273746',fg='snow')
            texto.place(x=10,y=130,relwidth=0.75,relheight=0.06)
            cuadro0=Entry(frame,textvariable=cuadro01)
            cuadro0.place(x=500,y=130,relheight=0.06)
            Button2=Button(frame,text='CONFIRM',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:confirmar42())
            Button2.place(x=540,y=360,relwidth=0.17,relheight=0.05)
        try:
            if MP[VER][0]==4:
                pass
            Button2=Button(frame,text='NEXT',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:siguienteEMP())
            Button2.place(x=180,y=360,relwidth=0.17,relheight=0.05)
        except IndexError:
            pass
        if CONTADOR>0:
            Button2=Button(frame,text='BACK',font=('Radio Canada Big',11),bg='snow',fg='black',command=lambda:atrasEMP())
            Button2.place(x=40,y=360,relwidth=0.17,relheight=0.05)
    #################################################################################################################################################################
    #################################################################################################################################################################
    # INICIO
    VER=0
    CONTADOR=0
    raiz1.destroy()
    raiz=tk.Tk()
    raiz.title('LAURA INC')
    raiz.config(bg='#273746')
    raiz.geometry('700x476')
    raiz.resizable(0,0)

    titulo=Label(raiz,text='PRINCIPAL MENU',font=('Radio Canada Big', 16),fg='snow')
    titulo.place(relx=0.5,y=60,anchor=tk.CENTER,relwidth=1,relheight=0.1)
    titulo.config(bg='#273746')
    cerrar=Button(raiz,text='CLOSE',font=('Radio Canada Big',11),fg='black',command=lambda:volverainicio())
    cerrar.place(x=570,y=440,relwidth=0.15,relheight=0.05)
    cerrar.config(bg='snow')
    
    menubarra=Menu(raiz)
    
    menu0=Menu(menubarra,tearoff=0)
    menu0.add_command(label='ENTER RAW MATERIALS',font=('Radio Canada Big',10), command=lambda:menu12())
    menu0.add_command(label='ENTER PRODUCTS',font=('Radio Canada Big',10), command=lambda:menu1())
    menubarra.add_cascade(label='ENTER DATA',font=('Radio Canada Big',10), menu=menu0)
        
    menu2=Menu(menubarra,tearoff=0)
    menu2.add_command(label='SEE RAW MATERIALS',font=('Radio Canada Big',10), command=lambda:menu22A())
    menu2.add_command(label='SEE PRODUCTS',font=('Radio Canada Big',10), command=lambda:menu21A())
    menubarra.add_cascade(label='SEE DATA',font=('Radio Canada Big',10), menu=menu2)
        
    menu3=Menu(menubarra,tearoff=0)
    menu3.add_command(label='MODIFY RAW MATERIALS',font=('Radio Canada Big',10),command=lambda:menu32A())
    menu3.add_command(label='MODIFY PRODUCTS',font=('Radio Canada Big',10),command=lambda:menu31A())
    menubarra.add_cascade(label='MODIFY DATA',font=('Radio Canada Big',10),menu=menu3)

    menu4=Menu(menubarra,tearoff=0)
    menu4.add_command(label='DELETE RAW MATERIALS',font=('Radio Canada Big',10),command=lambda:menu42A())
    menu4.add_command(label='DELETE PRODUCTS',font=('Radio Canada Big',10),command=lambda:menu41A())
    menubarra.add_cascade(label='DELETE DATA',font=('Radio Canada Big',10),menu=menu4)
        
    raiz.config(menu=menubarra)
    raiz.mainloop
#####################################################################################################################################################################
#####################################################################################################################################################################
# MAIN
def acasecreanlastablas():
    try:
        cursor.execute('CREATE TABLE RECETA (codigoreceta INTEGER PRIMARY KEY AUTOINCREMENT, nombrereceta VARCHAR(20), nombremateriaprimareceta VARCHAR(20), cantidadmateriaprima INTEGER, tipomateriaprimareceta VARCHAR(1))')
    except OperationalError:
        pass
    try:
        cursor.execute('CREATE TABLE MATERIA_PRIMA (codigomateriaprima INTEGER PRIMARY KEY AUTOINCREMENT, nombremateriaprima VARCHAR(20), unidadmateriaprima VARCHAR(5), preciomateriaprima INTEGER, tipomateriaprima VARCHAR(1), cantidadmateriaprima INTEGER)')
    except OperationalError:
        pass
    try:
        cursor.execute('CREATE TABLE PRODUCTO (codigoproducto INTEGER PRIMARY KEY AUTOINCREMENT, nombreproducto VARCHAR(20), precioproducto INTEGER)')
    except OperationalError:
        pass
def inicio():
    global raiz1
    raiz1=tk.Tk()
    raiz1.title('LAURA INC')
    raiz1.config(bg='#273746')
    raiz1.geometry('800x476')
    raiz1.resizable(0,0)
    titulo=Label(raiz1,text='WELCOME TO OUR SOFTWARE / BIENVENIDO A NUESTRO SOFTWARE',fg='snow',font=('Radio Canada Big', 16))
    titulo.place(relx=0.5,y=110,anchor=tk.CENTER,relwidth=1,relheight=0.07)
    titulo.config(bg='#273746')
    titulo=Label(raiz1,text='PLEASE CHOOSE A LANGUAGE / POR FAVOR SELECCIONE UN IDIOMA',fg='snow',font=('Radio Canada Big', 13))
    titulo.place(relx=0.5,y=150,anchor=tk.CENTER,relwidth=1,relheight=0.07)
    titulo.config(bg='#273746')
    cerrar=Button(raiz1,text='SPANISH / ESPANOL',font=('Radio Canada Big',11),fg='black',command=lambda:spanish())
    cerrar.place(relx=0.5,y=210,anchor=tk.CENTER,relwidth=0.3,relheight=0.05)
    cerrar.config(bg='snow')
    cerrar=Button(raiz1,text='ENGLISH / INGLES',font=('Radio Canada Big',11),fg='black',command=lambda:english())
    cerrar.place(relx=0.5,y=250,anchor=tk.CENTER,relwidth=0.3,relheight=0.05)
    cerrar.config(bg='snow')
    cerrar=Button(raiz1,text='CLOSE / CERRAR',font=('Radio Canada Big',11),fg='black',command=lambda:cerrar0())
    cerrar.place(x=540,y=440,relwidth=0.2,relheight=0.05)
    cerrar.config(bg='snow')
    raiz1.mainloop()
#####################################################################################################################################################################
#####################################################################################################################################################################
acasecreanlastablas()
inicio()