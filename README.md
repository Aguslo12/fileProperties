# Propiedades de Archivos 


Un proyecto de [Python](https://www.python.org/) que se basa en la administración de archivos de un SO para permitirle al usuario poder buscar un archivo en un directorio, ver sus [propiedades](https://help.gnome.org/users/gnome-help/stable/nautilus-file-properties-basic.html.es), cambiar los permisos, y ejecutarlo simulando un doble click sobre él en el explorador de Windows.

## Setup
### ⬇️Instalacion de Python
1. Lo primero que debemos hacer es verificar que tenemos Python instalado en nuestro dispositivo. Podemos hacerlo ejecutando el siguiente comando.
```shell
python --version
```
De no tenerlo instalado, puede hacerlo desde la [pagina oficial de Python](https://www.python.org/downloads/).
2. Instale las siguientes dependencias necesarias.
```shell
pip install os
pip install stat
pip install subprocess
pip install zipfile
pip install datetime
```

### 📁 Acceso al proyecto
1. Descargue el codigo fuente desde el [repositorio en Github](https://github.com/Aguslo12/fileProperties).

### 🛠️ Abre y ejecuta el proyecto
1. Abra una terminal con permisos de adminsitrador y busque el directorio donde se encuentra el archivo main.py del proyecto.
2. Ejecute el siguiente comando para poder iniciar el proyecto.
```shell
python main.py
```

## ⚙️ Uso
Cuando el programa ya esta en uso, lo primero va a hacer es mostrarnos el directorio actual en el que se encuentra y nos va a pedir:
1. Saber si queremos cambiar a otro directorio.
2. Buscar un archivo en el directorio actual.

Una vez que estemos seguros de querer buscar un archivo en el directorio, ingresamos el archivo al cual queremos acceder y vamos a poder escribir los siguientes comando para generar acciones con el archivo seleccionado:

- `ayuda`: Muestra información de los comandos disponibles.
- `prop`: Muestra todas las propiedades del archivo.
- `abrir`: Abre el archivo con una aplicación relacionada en el SO.
- `permisos`: Permite cambiar los permisos del archivo.
- `inicio`: Vuelve al inicio del programa para permitir cambiar de directorio.
- `salir`: Termina la ejecución del programa.
- `abzip`; Permite abrir los archivos que son .zip y ver los elementos que contienen.

## Más Explicaciones
La principal base de funcionamiento de nuestro programa es la [librería os](https://docs.python.org/es/3.10/library/os.html) la cual nos permite tener un contacto directo con el sistema operativo en el cual se ejecuta el código. La utilizamos para poder llegar a obtener intformación sobre las propiedades del archivo que seleccionamos y las interacciones que podemos tener con dicho archivo a través del SO.

## Autores
| [Agustin Lobos](https://github.com/Aguslo12) |  [Franco Santibañez](https://github.com/francosantzz) |
| :---: | :---: |
