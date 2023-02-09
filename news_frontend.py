from tkinter import *
from news_backend import News

database = News("app.db")

class Window(object):

    def __init__(self,window):

        self.window = window
        self.window.geometry("1024x272")
        self.window.wm_title("Archivero")

        l1 = Label(window, text = "Titulo")
        l1.grid(row = 0, column = 0)

        l2 = Label(window, text = "Novedad")
        l2.grid(row = 0, column = 2)

        l3 = Label(window, text = "Imagen")
        l3.grid(row = 1, column = 0)

        l4 = Label(window, text = "Fuente")
        l4.grid(row = 1, column = 2)


        self.e1_titulo=StringVar()
        self.e1=Entry(window,textvariable=self.e1_titulo,width=64)
        self.e1.grid(row=0,column=1)

        self.e2_novedad=StringVar()
        self.e2=Entry(window,textvariable=self.e2_novedad,width=64)
        self.e2.grid(row=0,column=3)

        self.e3_imagen=StringVar()
        self.e3=Entry(window,textvariable=self.e3_imagen,width=64)
        self.e3.grid(row=1,column=1)

        self.e4_fuente=StringVar()
        self.e4=Entry(window,textvariable=self.e4_fuente,width=64)
        self.e4.grid(row=1,column=3)
        
    
        self.list1=Listbox(window, height=16,width=64)
        self.list1.grid(row=2,column=0,rowspan=6,columnspan=2)

        sb1=Scrollbar(window)
        sb1.grid(row=2,column=2,rowspan=6,sticky="NS")

        self.list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=self.list1.yview)

        self.list1.bind('<<ListboxSelect>>',self.get_selected_row)

        b1=Button(window,text="Ver todos", width=32  , command=self.view_command)
        b1.grid(row=2,column=3)

        b2=Button(window,text="Buscar", width=32  , command=self.search_command)
        b2.grid(row=3,column=3)

        b3=Button(window,text="Agregar entrada", width=32  , command=self.add_command)
        b3.grid(row=4,column=3)

        b4=Button(window,text="Actualizar selección", width=32  , command=self.update_command)
        b4.grid(row=5,column=3)

        b5=Button(window,text="Borrar selección", width=32  , command=self.delete_command)
        b5.grid(row=6,column=3)

        b6=Button(window,text="Cerrar", width=32  , command=window.destroy)
        b6.grid(row=7,column=3)

    def get_selected_row(self,event):
        index=self.list1.curselection()[0]
        self.selected_tuple=self.list1.get(index) #very clever
        self.e1.delete(0,END)
        self.e1.insert(END,self.selected_tuple[1])
        self.e2.delete(0,END)
        self.e2.insert(END,self.selected_tuple[2])
        self.e3.delete(0,END)
        self.e3.insert(END,self.selected_tuple[3])
        self.e4.delete(0,END)
        self.e4.insert(END,self.selected_tuple[4])
        
        

    def view_command(self):
        self.list1.delete(0,END)
        for row in database.view():
            self.list1.insert(END,row)

    def search_command(self):
        self.list1.delete(0,END)
        for row in database.search(self.e1_titulo.get(), self.e2_novedad.get(), self.e3_imagen.get(), self.e4_fuente):
            self.list1.insert(END,row)
        self.list1.delete(1,END) #si no pones esta linea te enlista todas las coincidencias parciales despues de la primera


    def add_command(self):
        database.insert(self.e1_titulo.get(), self.e2_novedad.get(), self.e3_imagen.get(), self.e4_fuente.get())
        self.list1.delete(0,END)
        self.list1.insert(END, self.e1_titulo.get(), self.e2_novedad.get(), self.e3_imagen.get(), self.e4_fuente.get())

    def delete_command(self):
        database.delete(self.selected_tuple[0])

    def update_command(self):
        database.update(self.selected_tuple[0],self.e1_titulo.get(), self.e2_novedad.get(), self.e3_imagen.get(), self.e4_fuente.get())

window=Tk()
Window(window)
window.mainloop()
