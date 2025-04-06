from pathlib import Path
import shutil

def menu():
    print("Ingrese la direccion de la carpeta que desea respaldar:")
    link = input("Direccion: ")
    link_path = Path(link)

    #Comprobar si la carpeta existe
    if link_path.is_dir():
        print("Ruta Correcta.")
        print("Ingrese la direccion de la carpeta de respaldo:")
        link_respaldo = Path(input("Direccion: "))

        #Comprobar si la carpeta de respaldo existe
        if link_respaldo.is_dir():
            print("Ruta de respaldo correcta.")

            #Leer archivos de la ruta de origen
            archivos = [archivo for archivo in link_path.iterdir() if archivo.is_file()]
            print("Archivos en la carpeta:")
            for archivo in archivos:
                print("Copiando archivo...")
                #Copiar archivos a la carpeta de respaldo
                link = link_respaldo / archivo.name
                shutil.copy(archivo, link)

            print("Archivos copiados correctamente.")

        else:
            print("Ruta de respaldo incorrecta.")
    else:
        print("La carpeta no existe")



if __name__ == "__main__":
    menu()