import os
import subprocess
import stat
from datetime import datetime

def main():
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
            print("------------------------------\nPROPIEDADES")
            print(f"Nombre del archivo: {nombre_archivo}")
            print(f"Extension del archivo: {extension}")
            print(f"Tamaño: {stat_info.st_size} bytes")
            print(f"Permisos: {stat.filemode(stat_info.st_mode)}")
            print(f"Último acceso: {datetime.fromtimestamp(stat_info.st_atime)}")
            print(f"Última modificación: {datetime.fromtimestamp(stat_info.st_mtime)}")
            print(f"Último cambio: {datetime.fromtimestamp(stat_info.st_ctime)}")
        else:
            print("Archivo no encontrado.")
            main()


    def eleccion_usuario(ruta_archivo):
        nom, extension = os.path.splitext(ruta_archivo)
        eleccion = input("Ingrese a continuacion que accion desea realizar: "
                         "\nCambiar los permisos del archivo = 1"
                         "\nEjecutar el archivo con una app = 2\n>")
        if int(eleccion) == 1:
            permisos = input("Ingrese los permisos deseados (ejemplo: 'grant Nombre_Usuario:F'):\n "
                             "F: Full Control\n"
                             "M: Modify\n"
                             "RX: Read & Execute\n"
                             "R: Read\n"
                             "W: Write\n"
                             "D: Denied access\n>")
            cambiar_permisos_archivo(ruta_archivo, permisos)
        if int(eleccion) == 2:
            abrir_app(ruta_archivo)


    def abrir_app(ruta_archivo):
        os.startfile(ruta_archivo)


    def cambiar_permisos_archivo(ruta_archivo, permisos):
        comando = f"icacls {ruta_archivo} /{permisos}"
        proceso = subprocess.Popen(comando, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        _, error = proceso.communicate()

        if proceso.returncode == 0:
            print("Los permisos se han cambiado correctamente.")
        else:
            print(f"Error al cambiar los permisos: {error.decode('latin-1')}")


    def vol_accion():
        opcion = input("Desea realizar alguna accion con el archivo nombrado?\nIngrese S para si y N para no: \n")
        if opcion.lower() == "s":
            eleccion_usuario(ruta_archivo)
        elif opcion.lower() == "n":
            print("¡Nos vemos! Espero haber sido de mucha ayuda")
            exit()
        else:
            print("Caracter ingresado no valido")
            vol_accion()


    directorio = input("Ingrese el directorio para buscar el archivo\n> ")
    nombre_archivo = input("Ingrese el nombre del archivo a buscar\n> ")
    ruta_archivo = buscar_archivo(directorio, nombre_archivo)
    mostrar_propiedades_archivo(ruta_archivo)
    print("-----------------------------------------")
    vol_accion()

main()
