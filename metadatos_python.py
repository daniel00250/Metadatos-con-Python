import tkinter as tk
from tkinter import filedialog
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

# Lista de metadatos que se mostrarán siempre
metadatos_fijos = [
    "Dimensiones de la imagen",
    "Formato de la imagen",
    "Fecha de creación y modificación",
    "Ubicación geográfica",
    "Configuraciones de la cámara",
    "Derechos de autor y derechos de uso",
    "Palabras clave y etiquetas",
    "Resolución de la imagen",
    "Espacio de color y perfil de color",
    "Historial de edición",
    "Software de edición",
    "Número de serie de la cámara",
    "Modelo de la cámara",
    "Fabricante de la cámara",
    "Orientación de la imagen",
    "Comentarios y descripciones",
    "Número de bits por canal"
]

def cargar_imagen():
    archivo = filedialog.askopenfilename(filetypes=[("Imágenes", "*.jpg;*.jpeg;*.png;*.gif;*.bmp;*.tif;*.tiff")])
    if archivo:
        imagen = Image.open(archivo)
        metadatos = imagen.info
        metadatos_text.config(state=tk.NORMAL)
        metadatos_text.delete(1.0, tk.END)
        
        metadatos_text.insert(tk.END, "Metadatos generales:\n")
        metadatos_text.insert(tk.END, f"Dimensiones de la imagen: {imagen.size[0]} x {imagen.size[1]}\n")
        metadatos_text.insert(tk.END, f"Formato de la imagen: {imagen.format}\n")
        
        for metadato in metadatos_fijos:
            metadatos_text.insert(tk.END, f"{metadato}: \n")

        try:
            exif_data = imagen._getexif()
            if exif_data:
                metadatos_text.insert(tk.END, "\nMetadatos EXIF:\n")
                for tag, valor in exif_data.items():
                    tag_nombre = TAGS.get(tag, tag)
                    metadatos_text.insert(tk.END, f"{tag_nombre}: {valor}\n")
                
                gps_info = exif_data.get(34853)
                if gps_info:
                    metadatos_text.insert(tk.END, "\nMetadatos GPS:\n")
                    for tag, valor in gps_info.items():
                        tag_nombre = GPSTAGS.get(tag, tag)
                        metadatos_text.insert(tk.END, f"{tag_nombre}: {valor}\n")
        except AttributeError:
            pass

        metadatos_text.config(state=tk.DISABLED)

app = tk.Tk()
app.title("Metadatos con Python")
app.geometry("400x600")

titulo_label = tk.Label(app, text="Metadatos con Python", font=("Helvetica", 16))
titulo_label.pack(pady=10)

subtitulo_label = tk.Label(app, text="Autor DxN", font=("Helvetica", 12))
subtitulo_label.pack()

cargar_boton = tk.Button(app, text="Cargar Imagen", command=cargar_imagen)
cargar_boton.pack(pady=20)

metadatos_label = tk.Label(app, text="Metadatos de la imagen:")
metadatos_label.pack()

metadatos_text = tk.Text(app, height=20, width=40)
metadatos_text.config(state=tk.DISABLED)
metadatos_text.pack()

app.mainloop()