import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from db_access import obtener_personas, insertar_persona

app = ttk.Window(title="Administrador Access", themename="flatly", size=(500, 400))

ttk.Label(app, text="Nombre:").pack(pady=5)
nombre_entry = ttk.Entry(app)
nombre_entry.pack()

ttk.Label(app, text="Edad:").pack(pady=5)
edad_entry = ttk.Entry(app)
edad_entry.pack()

def guardar():
    nombre = nombre_entry.get()
    edad = edad_entry.get()
    if nombre and edad.isdigit():
        insertar_persona(nombre, int(edad))
        actualizar_tabla()

def actualizar_tabla():
    for row in tabla.get_children():
        tabla.delete(row)
    for persona in obtener_personas():
        tabla.insert("", "end", values=persona)

ttk.Button(app, text="Guardar", command=guardar, bootstyle=SUCCESS).pack(pady=10)

tabla = ttk.Treeview(app, columns=("ID", "Nombre", "Edad"), show="headings")
for col in ("ID", "Nombre", "Edad"):
    tabla.heading(col, text=col)
tabla.pack(expand=True, fill="both", pady=10)

actualizar_tabla()
app.mainloop()
