
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
        nombre_archivo, extension = os.path.splitext(ruta_archivo)
        print(f"Nombre del archivo: {nombre_archivo}")
        print(f"Extension del archivo: {extension}")
        print(f"Propiedades del archivo: {ruta_archivo}")
        print(f"Tamaño: {stat_info.st_size} bytes")
        print(f"Permisos: {stat.filemode(stat_info.st_mode)}")
        print(f"Último acceso: {datetime.fromtimestamp(stat_info.st_atime)}")
        print(f"Última modificación: {datetime.fromtimestamp(stat_info.st_mtime)}")
        print(f"Último cambio: {datetime.fromtimestamp(stat_info.st_ctime)}")
    else:
        print("Archivo no encontrado.")

def eleccion_usuario(ruta_archivo):
    extension = os.path.splitext(ruta_archivo)
    eleccion = input("Ingrese a continuacion que accion desea realizar: "
                     "\nCambiar los permisos del archivo = 1"
                     "\nEjecutar el archivo con una app = 2\n")
    if int(eleccion) == 1:
        permisos = input("Ingrese los permisos deseados (ejemplo: 'grant Nombre_Usuario:F'): ")
        cambiar_permisos_archivo(ruta_archivo, permisos)
    if int(eleccion) == 2:
        abrir_app(ruta_archivo,extension)

def abrir_app(ruta_archivo, extension):
    print(extension)
    if extension == ".docx":
        os.startfile(ruta_archivo)
    elif extension == ".mp3":
        os.startfile(ruta_archivo)
    elif extension == ".pdf":
        os.startfile(ruta_archivo)
    else:
        print("No se puede abrir el archivo con esta extension")

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
print("-----------------------------------------")
opcion = input("Desea realizar alguna accion con el archivo nombrado?\nIngrese S para si y N para no: \n")
if opcion.lower() == "s":
    eleccion_usuario(ruta_archivo)
elif opcion.lower() == "n":
    print("Caracter ingresado no valido")
else:
    exit()
