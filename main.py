
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
def cambiar_permisos_archivo(ruta_archivo, permisos):
    comando = f"icacls {ruta_archivo} /{permisos}"
    proceso = subprocess.Popen(comando, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    _, error = proceso.communicate()

    if proceso.returncode == 0:
        print("Los permisos se han cambiado correctamente.")
    else:
        print(f"Error al cambiar los permisos: {error.decode('latin-1')}")
directorio = input("Ingrese el directorio para buscar el archivo: ")
nombre_archivo = input("Ingrese el nombre del archivo a buscar: ")

ruta_archivo = buscar_archivo(directorio, nombre_archivo)
mostrar_propiedades_archivo(ruta_archivo)
opcion = input("Desea cambiar los permisos del archivo? (s/n): ")
if opcion.lower() == "s":
    permisos = input("Ingrese los permisos deseados (ejemplo: 'grant Administrators:F'): ")
    cambiar_permisos_archivo(ruta_archivo, permisos)