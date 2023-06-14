
import os
import subprocess
import stat
from datetime import datetime

def buscar_archivo(directorio, nombre_archivos):
    ruta_completa = None
    for root, dirs, files in os.walk(directorio):
        if nombre_archivos in files:
            ruta_completa = os.path.join(root, nombre_archivos)
            break
    return ruta_completa

def mostrar_propiedades_archivo(ruta_archivo):
    if ruta_archivo is not None:
        stat_info = os.stat(ruta_archivo)
        ruta = os.path.abspath(ruta_archivo)
        print(f"Propiedades del archivo: {ruta_archivo}")
        print(f"Tamaño: {stat_info.st_size} bytes")
        print(f"Permisos: {stat.filemode(stat_info.st_mode)}")
        print(f"Último acceso: {datetime.fromtimestamp(stat_info.st_atime)}")
        print(f"Última modificación: {datetime.fromtimestamp(stat_info.st_mtime)}")
        print(f"Último cambio: {datetime.fromtimestamp(stat_info.st_ctime)}")
        print(f"Ruta: {ruta}")
    else:
        print("Archivo no encontrado.")

directorio = input("Ingrese el directorio para buscar el archivo: ")
nombre_archivo = input("Ingrese el nombre del archivo a buscar: ")

ruta_archivo = buscar_archivo(directorio, nombre_archivo)
mostrar_propiedades_archivo(ruta_archivo)
