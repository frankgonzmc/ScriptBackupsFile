from pathlib import Path

def menu():
    print("Ingrese la direccion de la carpeta que desea respaldar:")
    link = input("Direccion: ")
    link_path = Path(link)

    #Comprobar si la carpeta existe
    if link_path.exists():
        print("La carpeta existe")
    else:
        print("La carpeta no existe")



if __name__ == "__main__":
    menu()