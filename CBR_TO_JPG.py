import patoolib
import os

# Ruta del archivo .CBR 
archivo_cbr = r"Ruta  del archivo  CBR"

#  Preguntar si quiere una carpeta personalizada 
ruta_personalizada = input("¿Dónde quieres extraer las imágenes? (presiona Enter para usar la ruta por defecto 'Imagenes_extraidas'): ").strip()

if ruta_personalizada:
    directorio_imagenes = ruta_personalizada
else:
    # Carpeta por defecto llamada "Imagenes_extraidas" en el mismo directorio del script
    directorio_imagenes = os.path.join(os.path.dirname(__file__), "Imagenes_extraidas")

#  Crear la carpeta si no existe 
os.makedirs(directorio_imagenes, exist_ok=True)

#  Extraer las imágenes del archivo .CBR 
try:
    patoolib.extract_archive(archivo_cbr, outdir=directorio_imagenes)
    print(f" Extracción completada en: {directorio_imagenes}")
except Exception as e:
    print(f" Error al extraer el archivo .cbr: {e}")
