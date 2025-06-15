# NoirCBR

Este proyecto está pensado para convertir imágenes a escala de grises de forma rápida usando procesamiento paralelo. Es especialmente útil si se tienen muchas imágenes, por ejemplo, páginas de un cómic extraídas desde un archivo `.cbr`.

## Archivos incluidos

- `CBR_TO_JPG.py`: Extrae las imágenes desde un archivo `.cbr`  y las guarda en una carpeta.
- `NoirCBR_map.py`: Convierte todas las imágenes de una carpeta a blanco y negro usando multiprocessing.

## Cómo usar

1. **Extraer imágenes desde un CBR (opcional)**  
   Si tienes un archivo `.cbr`, puedes usar `CBR_TO_JPG.py`.  
   Al ejecutarlo, el script te preguntará si deseas indicar una carpeta de salida personalizada. Si no respondes(presionas Enter), creará una por defecto llamada `Imagenes_extraidas` en el mismo directorio del script.

2. **Convertir imágenes a blanco y negro**  
   Ejecuta `NoirCBR_map.py`.  
   El script te pedirá una carpeta de salida para las imágenes en escala de grises. Si no das ninguna(presionas enter), usará una carpeta por defecto llamada `Comic_Noir`.

## Requisitos

- Python 3.x
-Instalar las  dependencias
- WinRAR instalado (necesario para extraer archivos `.cbr` con `patoolib`)

## Notas

- El procesamiento de imágenes se realiza en paralelo para acelerar el tiempo de ejecución.
- Los archivos convertidos se guardan con el mismo nombre que el original, añadiendo `_gris` al final.
