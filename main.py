import os
import subprocess
import stat
from datetime import datetime
import zipfile
import re
def main():
    def buscar_archivo(directorio, nombre_archivos):
        ruta_completa = None
        for root, dirs, files in os.walk(directorio):
            if nombre_archivos in files:
                ruta_completa = os.path.join(root, nombre_archivos)
                print(ruta_completa)
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

    def mostrar_archivos_zip(archivo_zip):
        with zipfile.ZipFile(archivo_zip, 'r') as zip_ref:
            archivos = zip_ref.namelist()
            print("Archivos en el ZIP:")
            for archivo in archivos:
                print(archivo)

    def elegir_archivo_zip():
        directorio_actual = os.getcwd()
        archivo_zip = input("Ingrese el nombre del archivo ZIP:\n>")
        archivo_zip_path = os.path.join(directorio_actual, archivo_zip)
        if os.path.isfile(archivo_zip_path) and archivo_zip.endswith('.zip'):
            mostrar_archivos_zip(archivo_zip_path)
            print("-----------------------------------------")
            elegir_opcion_zip(archivo_zip_path)
        else:
            print("Archivo ZIP inválido.")
            elegir_archivo_zip()

    def elegir_opcion_zip(archivo_zip):
        opcion = input("Ingrese N para ingresar un archivo o la letra 'C' para entrar a una carpeta:\n>")
        if opcion == "C":
            elegir_carpeta_zip(archivo_zip)
        else:
            seleccionar_archivo_zip(archivo_zip)

    def elegir_carpeta_zip(archivo_zip):
        carpeta = input("Ingrese el nombre de la carpeta:\n>")
        with zipfile.ZipFile(archivo_zip, 'r') as zip_ref:
            archivos = zip_ref.namelist()
            carpetas = set()
            for archivo in archivos:
                if archivo.startswith(carpeta) and archivo != carpeta:
                    carpetas.add(archivo.split('/')[0])
            if len(carpetas) > 0:
                print("Se entró a la carpeta.")
                print("Carpetas disponibles:")
                for carpeta in carpetas:
                    print(carpeta)
                print("-----------------------------------------")
                elegir_opcion_zip(archivo_zip)
            else:
                print("No se encontraron carpetas con ese nombre.")
                print("-----------------------------------------")
                elegir_opcion_zip(archivo_zip)

    def seleccionar_archivo_zip(archivo_zip):
        with zipfile.ZipFile(archivo_zip, 'r') as zip_ref:
            archivos = zip_ref.namelist()
            print("Archivos disponibles:")
            for i, archivo in enumerate(archivos, 1):
                print(f"{i}. {archivo}")
            opcion = input("Ingrese el nombre del archivo:\n>")
            archivo_seleccionado = opcion.strip()
            for archivo in archivos:
                if archivo.endswith(archivo_seleccionado):
                    ruta_archivo_zip = os.path.join(archivo_zip, archivo)
                    ruta_archivo_zip = ruta_archivo_zip.replace("\\\\", "\\")
                    ruta_archivo_zip = ruta_archivo_zip.replace("/", "\\")
                    print(ruta_archivo_zip)
                    ruta_directorio = str(os.path.dirname(ruta_archivo_zip)).replace("\\\\", "\\")
                    print(ruta_directorio)
                    realizar_accion(archivo_seleccionado, ruta_archivo_zip)
                    return
            print("Archivo inválido.")
            print("-----------------------------------------")
            elegir_opcion_zip(archivo_zip)
    def inicio():
        decision = input(f"Directorio actual: {os.getcwd()}\n"
                         "1: Moverse a otro directorio\n"
                         "2: Buscar un archivo en el directorio\n"
                         "3: Ver archivos dentro de un ZIP\n>")
        if int(decision) == 1:
            mov = input("Directorio al cual moverse:")
            os.chdir(mov)
            post_inicio()
        elif int(decision) == 2:
            post_inicio()
        elif int(decision) == 3:
            mov = input("Directorio del archivo zip:")
            os.chdir(mov)
            elegir_archivo_zip()
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
        comando = input(f"Ingrese la accion que desea realizar(Si desconoce las opciones ingrese 'ayuda'):\n{os.getcwd()}\\{nombre_archivo}>")
        eleccion_comando(comando, ruta_archivo,nombre_archivo)

    # Es la misma funcion que la de arriba pero sin pedir que ingrese la accion.
    def realizar_accion2(nombre_archivo,ruta_archivo):
        comando = input(f"{os.getcwd()}\\{nombre_archivo}>")
        eleccion_comando(comando,ruta_archivo,nombre_archivo)
    inicio()


main()
