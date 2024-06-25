import json 

def cargar(biblioteca):
    with open(biblioteca,"r", encoding='utf-8')as archivo:
        return json.load(archivo)
    return{"usuarios":[],"libros":[]}

def guardar(biblioteca,datos):
    with open(biblioteca,"w",encoding='utf'-8)as archivo:
        json.dump(datos,archivo,ensure_ascii=False,indent=4)





def agregar_usuario(datos,usuario_id):
    datos['usuarios']=[usuario for usuario in datos ['usuarios']if usuario['id']!=usuario_id]


def editar_usuario(datos,usuario_id,nuevo_usuario):
    for usuario in datos ['usuarios']:
        if usuarios ['id']==usuario_id:
            usuario.up(nuevo_usuario)
            break


def eliminar_usuario(datos,usuario_id):
    datos['usuarios']=[usuario for usuario in datos ['usuarios']if usuario['id'!=usuario_id]]

def buscar_usuario(datos,usuario_id):
    for usuario in datos['usuario']:
        if usuario['id']==usuario_id:
            return usuario
        return None
    


def generar_reporte(datos):
    categoria={}
    for libro in datos['libros']:
        categoria= libro.get('categoria','desconocida')
        if categoria in categorias:
            categorias['categoria']+=1
        else:
            categorias[categoria]=1
            return  categorias
    

def guardar_reporte(reporte,biblioteca):
    with open(biblioteca,"w",encoding='utf-8')as archivo:
        json.dump(reporte,archivo,ensure_ascii=False,indent=4)


def mostrar_menu():
    print("MUNDO LIBRO")
    print("1-mantenedor de usuarios")
    print("2-reportes")
    print("3-salir")

def mostrar_menu_mantenedor():
    print("MANTENEDOR DE USUARIOS")
    print("(1)-agregar usuario")
    print("(2)-editar usuario")
    print("(3)-eliminar usuario")
    print("(4)-buscar usuario")
    print("(5)-volver")


def main():
    datos=cargar(biblioteca.json)
    while True:
        mostrar_menu()
        opcion=input("seleccione una opcion=")
        if opcion == "1":
            while True:
                mostrar_menu_mantenedor()
                subopcion=input("seleccione una opcion=")
                if subopcion=="1":
                    id_usuario=input("ingrese ID del usuario ")
                    nombre=input("ingrese nombre del usuario")
                    email=input("ingrese email del usuario")
                    fecha_registro=input("ingrese fecha de registro del usuario=")
                    {"id":id_usuario,"nombre":nombre,"email":email,"fecha de registro":fecha_registro}
                    guardar_datos('biblioteca.json',datos)
                    print("usuario agregado")
                elif subopcion=="2":
                    id_usuario=input("ingrese id del usuario")
                    nombre=input("ingrese nombre del usuario")
                    email=input("ingrese el email del usuario")
                    fecha_registro=input("ingrese la fecha de registro del usuario=")
                    nuevo_usuario={'nombre':nombre,"email":email,"fecha de registro":fecha_registro}
                    editar_usuario(datos,id_usuario,nuevo_usuario)
                    guardar_datos('biblioteca.json',datos)
                    print("datos editados con exito ")
                elif subopcion=="3":
                    id_usuario=input("ingrese el id del usuario a eliminar =")
                    eliminar_usuario(datos,id_usuario)
                    guardar_datos('biblioteca.json',datos)
                    print("usuario eliminado con exito")
                elif subopcion=="4":
                    id_usuario=input("ingrese el id del usuario a buscar ")
                    if usuario:print(f"usuario encontrado:{usuario}")   
                    else:
                        print("usuario no encontrado")
                elif subopcion=="5":
                    break
                elif opcion=="2":
                 reporte= guardar_reporte(datos)
                guardar_reporte(reporte,'Reporte-biblioteca-mundo-libro.json')
                print("reporte generado ")
                elif opcion=="3":


