import tkinter as tk

def Opcion1():
    print(entrada.get())


app = tk.Tk()
palabra = tk.StringVar(app)
entrada = tk.StringVar(app)

app.geometry("300x600")
app.config(background="black")
app.title("Multitools")
tk.Label(app, text="Multitools", font=("Calabri", 40), bg="#000000", fg="white", justify="center").pack(fill=tk.X, expand=True)
tk.Entry(bg="black", fg="White", justify="center", textvariable=entrada).pack(fill=tk.BOTH, expand=True)
tk.Button(app, text="Opcion 1", font=("Calabri", 40), bg="#00a8e8", fg="white", relief="flat", command= Opcion1).pack(fill=tk.BOTH, expand=True)
app.mainloop()