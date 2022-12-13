import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import util.generic as utl
from forms.form_master import MasterPanel
from forms.form_registrar import RegistrarPanel
import math

class App:
    
    def verificar(self):
        usu = self.usuario.get()
        password = self.password.get()        
        if(usu == "belu" and password == "123") :
            self.ventana.destroy()
            MasterPanel()
        else:
            messagebox.showerror(message="La contraseña no es correcta",title="Mensaje")           

    def registrar(self):
        self.ventana.destroy()
        RegistrarPanel()

    def __init__(self):        
        self.ventana = tk.Tk()                             
        self.ventana.title('Bienvenido al Sistema Supermark - Inicio de sesion')
        
        #  Obtenemos el largo y  ancho de la pantalla
        wtotal = math.trunc(self.ventana.winfo_screenwidth()/1.6)
        htotal = math.trunc(self.ventana.winfo_screenheight()/1.3)     
        size = str(wtotal) + "x" + str(htotal)
        self.ventana.geometry(size)
        self.ventana.resizable(width=0, height=0)    
        utl.centrar_ventana(self.ventana,wtotal,htotal)
        logo =utl.leer_imagen("./imagenes/logo.png", (math.trunc(wtotal/1.5), math.trunc(htotal/1.5)))

        #self.ventana.geometry('800x500')
        #self.ventana.config(bg='#fcfcfc')
        #self.ventana.resizable(width=0, height=0)    
        #utl.centrar_ventana(self.ventana,800,500)
        #logo =utl.leer_imagen("./imagenes/logo.png", (500, 500))

        # frame_logo
        #frame_logo = tk.Frame(self.ventana, bd=0, width=300, relief=tk.SOLID, padx=10, pady=10,bg='black')
        frame_logo = tk.Frame(self.ventana, bd=0, width=math.trunc(wtotal/2), relief=tk.SOLID, padx=10, pady=10,bg='black')
        frame_logo.pack(side="left",expand=tk.YES,fill=tk.BOTH)
        label = tk.Label( frame_logo, image=logo,bg='black' )
        label.place(x=0,y=0,relwidth=1, relheight=1)
        
        #frame_form
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form.pack(side="right",expand=tk.YES,fill=tk.BOTH)
        #frame_form
        
        #frame_form_top
        frame_form_top = tk.Frame(frame_form,height = 50, bd=0, relief=tk.SOLID,bg='black')
        frame_form_top.pack(side="top",fill=tk.X)
        title = tk.Label(frame_form_top, text="Inicio de sesion",font=('Times', 30), fg="#666a88",bg='#fcfcfc',pady=50)
        title.pack(expand=tk.YES,fill=tk.BOTH)
        #end frame_form_top

        #frame_form_fill
        frame_form_fill = tk.Frame(frame_form,height = 50,  bd=0, relief=tk.SOLID,bg='#fcfcfc')
        frame_form_fill.pack(side="bottom",expand=tk.YES,fill=tk.BOTH)

        etiqueta_usuario = tk.Label(frame_form_fill, text="Usuario", font=('Times', 14) ,fg="#666a88",bg='#fcfcfc', anchor="w")
        etiqueta_usuario.pack(fill=tk.X, padx=20,pady=5)
        self.usuario = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.usuario.pack(fill=tk.X, padx=20,pady=10)

        etiqueta_password = tk.Label(frame_form_fill, text="Contraseña", font=('Times', 14),fg="#666a88",bg='#fcfcfc' , anchor="w")
        etiqueta_password.pack(fill=tk.X, padx=20,pady=5)
        self.password = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.password.pack(fill=tk.X, padx=20,pady=10)
        self.password.config(show="*")

        inicio = tk.Button(frame_form_fill,text="Iniciar sesion",font=('Times', 15,BOLD),bg='black', bd=0,fg="#fff",command=self.verificar)
        inicio.pack(fill=tk.X, padx=20,pady=20)        
        inicio.bind("<Return>", (lambda event: self.verificar()))
        #end frame_form_fill
        
        etiqueta_olvido = tk.Label(frame_form_fill, text="¿Olvidó su contraseña?", font=('Times', 14) ,fg="#666a88",bg='#fcfcfc', anchor="w")
        etiqueta_olvido.pack(fill=tk.X, padx=20,pady=5)
        recuperar = tk.Button(frame_form_fill,text="Recuperar",font=('Times', 15,BOLD),bg='white', bd=0,fg="black")
        recuperar.pack(fill=tk.X, padx=100,pady=10)        
        #recuperar.bind("<Return>", (lambda event: self.verificar()))
        
        etiqueta_registrarse = tk.Label(frame_form_fill, text="¿No tiene cuenta?", font=('Times', 14) ,fg="#666a88",bg='#fcfcfc', anchor="w")
        etiqueta_registrarse.pack(fill=tk.X, padx=20,pady=5)
        registrarse = tk.Button(frame_form_fill,text="Registrarse",font=('Times', 15,BOLD),bg='white', bd=0,fg="red",command=self.registrar)
        registrarse.pack(fill=tk.X, padx=100,pady=10)        
        #registrarse.bind("<Return>", (lambda event: self.verificar()))

        salir = tk.Button(frame_form_fill,text="Salir del Sistema",font=('Times', 15),bg='black', bd=0,fg="#fff",command=self.ventana.destroy)
        salir.pack(fill=tk.X, padx=20,pady=10)        
        
        self.ventana.mainloop()

if __name__ == "__main__":
   App()
