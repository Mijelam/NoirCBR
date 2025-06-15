from PIL import Image
import os
import time
import multiprocessing as mp


def convertir_a_gris(ruta_imagen, ruta_salida):
    """Convierte una imagen a escala de grises.""" 
    try:
        imagen = Image.open(ruta_imagen).convert('L')
        nombre_archivo, extension = os.path.splitext(os.path.basename(ruta_imagen))
        ruta_guardado = os.path.join(ruta_salida, f"{nombre_archivo}_gris{extension}")
        imagen.save(ruta_guardado)
        print(f"Imagen convertida: {nombre_archivo}")
    except FileNotFoundError:
        print("Error: No se encontró la imagen.")
    except Exception as e:
        print(f"Error al procesar la imagen: {e}")

def procesar_imagenes_paralelamente(lista_imagenes, ruta_salida):
    """Procesa una lista de imágenes paralelamente."""
    with mp.Pool() as p:
        p.starmap(convertir_a_gris, [(imagen, ruta_salida) for imagen in lista_imagenes])
        

if __name__ == '__main__':

    # Carpetas de entrada y salida 
    directorio_imagenes = r"Ruta de las imágenes a convertir"

    ruta_salida_personalizada = input("¿Dónde quieres guardar las imágenes en blanco y negro? (presiona Enter para usar la ruta por defecto 'Comic_Noir'): ").strip()

    if ruta_salida_personalizada:
        directorio_salida=ruta_salida_personalizada
    else:
    #Carpeta por defecto  llamada  Comic_Noir en el mismo directorio del script.
        directorio_salida=os.path.join(os.path.dirname(__file__), "Comic_Noir")

    os.makedirs(directorio_salida, exist_ok=True)

    extensiones_permitidas = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff')
    lista_imagenes = [
    os.path.join(directorio_imagenes, f)
    for f in os.listdir(directorio_imagenes)
    if os.path.isfile(os.path.join(directorio_imagenes, f)) and f.lower().endswith(extensiones_permitidas)
    ]

    
    inicio = time.time()
    procesar_imagenes_paralelamente(lista_imagenes,directorio_salida)
    fin = time.time()

    print(f"Tiempo total de procesamiento: {fin - inicio:.2f} segundos")