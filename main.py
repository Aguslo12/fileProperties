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
        if ruta_completa is not None:
            return ruta_completa
        else:
            print("Archivo no encontrado.")
            inicio()


    def mostrar_propiedades_archivo(ruta_archivo):
        if ruta_archivo is not None:
            stat_info = os.stat(ruta_archivo)
            nombre_archivo, extension = os.path.splitext(ruta_archivo)
            print("------------------------------\nPROPIEDADES")
            print(f"Nombre del archivo: {nombre_archivo}")
            print(f"Extension del archivo: {extension}")
            print(f"ID del nodo del archivo: {stat_info.st_ino}")
            print(f"Numeros de enlances al archivo: {stat_info.st_nlink}")
            print(f"Propietario del archivo: {stat_info.st_uid}")
            print(f"Tamaño: {stat_info.st_size} bytes")
            print(f"Permisos: {stat.filemode(stat_info.st_mode)}")
            print(f"Último acceso: {datetime.fromtimestamp(stat_info.st_atime)}")
            print(f"Última modificación: {datetime.fromtimestamp(stat_info.st_mtime)}")
            print(f"Último cambio de estado: {datetime.fromtimestamp(stat_info.st_ctime)}")
        else:
            print("Archivo no encontrado.")
            main()

    def mostrar_ayuda():
        print("-----------------------------------------")
        print("PROP                             Muestra las propiedades del archivo seleccionado.\n"
              "ABRIR                            Abre el archivo con una aplicaión relacionada dentro del SO.\n"
              "PERMISOS                         Permite cambiar los permisos del archivo dentro del dispositivo\n"
              "INICIO                           Volver al inicio.\n"
              "SALIR                            Cierra la aplicación.")

    #Funcion que abre la aplicacion
    def abrir_app(ruta_archivo):
        os.startfile(ruta_archivo)

    #Funcion para cambiar los permisos de los archivos
    def cambiar_permisos_archivo(ruta_archivo, permisos):
        comando = f"icacls {ruta_archivo} /{permisos}"
        proceso = subprocess.Popen(comando, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        _, error = proceso.communicate()

        if proceso.returncode == 0:
            print("Los permisos se han cambiado correctamente.")
        else:
            print(f"Error al cambiar los permisos: {error.decode('latin-1')}")


    #Genera la accion que el usuario decida
    def eleccion_comando(comando,ruta_archivo,nombre_archivo):
        if comando == "ayuda":
            mostrar_ayuda()
            print("-----------------------------------------")
            realizar_accion2(nombre_archivo,ruta_archivo)
        elif comando == "prop":
            mostrar_propiedades_archivo(ruta_archivo)
            print("-----------------------------------------")
            realizar_accion2(nombre_archivo, ruta_archivo)
        elif comando == "abrir":
            abrir_app(ruta_archivo)
            print("-----------------------------------------")
            realizar_accion2(nombre_archivo, ruta_archivo)
        elif comando == "permisos":
            permisos = input("Ingrese los permisos deseados (ejemplo: 'grant Nombre_Usuario:F'):\n "
                             "F: Full Control\n"
                             "M: Modify\n"
                             "RX: Read & Execute\n"
                             "R: Read\n"
                             "W: Write\n"
                             "D: Denied access\n>")
            cambiar_permisos_archivo(ruta_archivo,permisos)
            print("-----------------------------------------")
            realizar_accion2(nombre_archivo, ruta_archivo)
        elif comando == "inicio":
            inicio()
        elif comando == "salir":
            exit()
        else:
            print("Comando no válido, escriba AYUDA para poder ver los comandos disponibles.")
            realizar_accion2(nombre_archivo,ruta_archivo)

    def inicio():
        decision = input(f"Directorio actual:{os.getcwd()}\n"
              "1: Moverse a otro directorio\n"
              "2: Buscar un archivo en el directorio \n"
                         ">")
        if int(decision) == 1:
            mov = input("Directorio al cual moverse:")
            os.chdir(mov)
            post_inicio()
        elif int(decision) == 2:
            post_inicio()
        else:
            print("Comando incorrecto")
            inicio()

    def post_inicio():
        nombre_archivo = input("Ingrese el archivo en el cual desea hacer una accion:\n"
                               f"{os.getcwd()}>")
        directorio = os.getcwd()
        ruta_archivo = buscar_archivo(directorio, nombre_archivo)
        realizar_accion(nombre_archivo,ruta_archivo)
        print("-----------------------------------------")

    def realizar_accion(nombre_archivo,ruta_archivo):
        comando = input(f"Ingrese la accion que desea realizar:\n{os.getcwd()}\\{nombre_archivo}>")
        eleccion_comando(comando, ruta_archivo,nombre_archivo)

    # Es la misma funcion que la de arriba pero sin pedir que ingrese la accion.
    def realizar_accion2(nombre_archivo,ruta_archivo):
        comando = input(f"{os.getcwd()}\\{nombre_archivo}>")
        eleccion_comando(comando,ruta_archivo,nombre_archivo)
    inicio()


main()
