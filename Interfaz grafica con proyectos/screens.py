import tkinter as tk
from constantes import style
from constantes import codigos

class Home(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background=style.BACKGROUND)
        self.controller = controller
        self.choise = tk.StringVar(self, value= "codigo1")

        self.init_widgets()

    def move_code(self):
        choise = self.choise.get()
        if choise == "codigo1":
            self.controller.show_frame(Code1)
        elif choise == "codigo2":
            self.controller.show_frame(Code2)
        # self.controller.mode = self.choise.get()
        # self.controller.show_frame(Code1)

    def init_widgets(self):
        tk.Label(
            self,
            text = "Multitools Version PYTHON",
            justify = tk.CENTER,
            **style.STYLE
        ).pack(
            side = tk.TOP,
            fill = tk.BOTH,
            expand= True,
            padx = 22,
            pady = 11
        )
        optionsFrame = tk.Frame(self)
        optionsFrame.configure(background= style.BACKGROUND)
        optionsFrame.pack(
            side = tk.TOP,
            fill = tk.BOTH,
            expand=	True,
            padx= 22,
            pady= 11
        )
        tk.Label(
            optionsFrame,
            text = "Eligue la herramienta:",
            justify = tk.CENTER,
            **style.STYLE
        ).pack(
            side = tk.TOP,
            fill = tk.X,
            padx = 11,
            pady = 11
        )
        # SELECCION MULTIPLE
        for (key, value) in codigos.Nombres.items():
            tk.Radiobutton(
                optionsFrame,
                text = key,
                variable= self.choise,
                value = value,
                activebackground= style.BACKGROUND,
                activeforeground= style.TEXT,
                **style.STYLE
            ).pack(
                side = tk.LEFT,
                fill = tk.BOTH,
                expand= True,
                padx= 6,
                pady= 3
            )
        
        tk.Button(
            self,
            text= "EJECUTAR",
            command= self.move_code,
            **style.STYLE,
            relief= tk.FLAT,
            activebackground= style.BACKGROUND,
            activeforeground= style.TEXT
        ).pack(
            side = tk.TOP,
            fill = tk.X,
            padx= 22,
            pady= 11
        )
        

class Code1(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background=style.BACKGROUND)
        self.controller = controller
        self.entry = tk.StringVar(self)
        self.entry_num = tk.StringVar(self)

        self.init_widgets()

    
    def init_widgets(self):
        tk.Label(
            self,
            text = "Spamer de teclado",
            justify = tk.CENTER,
            **style.STYLE
        ).pack(
            side = tk.TOP,
            fill = tk.X,
            padx = 11,
            pady = 11
        )
        tk.Label(
            self,
            text = "Eligue la palabra:",
            justify = tk.CENTER,
            **style.STYLE
        ).pack(
            side = tk.TOP,
            fill = tk.X,
            padx = 11,
            pady = 0
        )
        tk.Entry(
            self,
            justify="center",
            **style.STYLE,
            background="black",
            textvariable= self.entry
        ).pack(
            side= tk.TOP,
            fill=tk.X,
            expand=True,
            padx = 22,
            pady = 11
        )
        tk.Label(
            self,
            text = "Numero de veces que se repetira:",
            justify = tk.CENTER,
            **style.STYLE
        ).pack(
            side = tk.TOP,
            fill = tk.X,
            padx = 11,
            pady = 0
        )
        tk.Entry(
            self,
            justify="center",
            **style.STYLE,
            background="black",
            textvariable= self.entry_num
        ).pack(
            side= tk.TOP,
            fill=tk.X,
            expand=True,
            padx = 22,
            pady = 11
        )
        tk.Button(
            self,
            text="Empezar",
            **style.STYLE,
            relief="flat",
            command= lambda: codigos.corazon.Codigo1(self.entry.get(), self.entry_num.get())
        ).pack(
                side= tk.TOP,
                fill=tk.BOTH,
                expand=True
        )
        tk.Button(
            self,
            text="Volver",
            **style.STYLE,
            relief="flat",
            command= lambda: self.controller.show_frame(Home)
        ).pack(
                side= tk.TOP,
                fill=tk.BOTH,
                expand=True
        )

class Code2(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background=style.BACKGROUND)
        self.controller = controller
        self.entry = tk.StringVar(self)

        self.init_widgets()

    
    def init_widgets(self):
        tk.Label(
            self,
            text = "Bots de telegram",
            justify = tk.CENTER,
            **style.STYLE
        ).pack(
            side = tk.TOP,
            fill = tk.X,
            padx = 11,
            pady = 11
        )
        tk.Button(
            self,
            text="Empezar",
            **style.STYLE,
            relief="flat",
            command= codigos.corazon.Codigo2
        ).pack(
                side= tk.TOP,
                fill=tk.BOTH,
                expand=True
        )
        tk.Button(
            self,
            text="Volver",
            **style.STYLE,
            relief="flat",
            command= lambda: self.controller.show_frame(Home)
        ).pack(
                side= tk.TOP,
                fill=tk.BOTH,
                expand=True
        )