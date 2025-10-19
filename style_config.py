import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# Tema visual: puedes cambiarlo por 'flatly', 'darkly', 'cyborg', 'solar', etc.
THEME = "flatly"

# Tamaño de ventana por defecto
WINDOW_SIZE = (600, 450)

# Estilos personalizados
BUTTON_STYLE = SUCCESS
LABEL_STYLE = INFO
ENTRY_STYLE = PRIMARY

# Función para crear la ventana principal con estilo
def crear_ventana(titulo="Administrador de Datos"):
    return ttk.Window(
        title=titulo,
        themename=THEME,
        size=WINDOW_SIZE
    )
