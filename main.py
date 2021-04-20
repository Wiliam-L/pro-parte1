import json 
import os

try:
    with open('Datos.json','r') as archvio_a:
        print("Caragando base de datos....")
        lista_alum = json.load(archvio_a)
        print("Base de datos cargada exitosamente")
except:
    print("Creando nueva base de datos...")
    lista_alum = []

def anio_inscripcion():
    return

def cursos_asignados(lista_notas):
    cursos = len(lista_notas)
    return cursos

def promedio_estudiante(lista_notas):
    if len(lista_notas) == 0:
        promedio = 0
        return promedio
  
    else:
        Total_suma = 0 
        for i in lista_notas:
            Total_suma = Total_suma + i
        cantidad_not = len(lista_notas)
        Promedio = Total_suma/cantidad_not
        return Promedio

def cursos_aprobados(lista_notas):
    for i in lista_notas:
        if i >=61:
            i=i
            return i  
def comparando_carnet():
    if carnet == lista_alum['carnet']:
        print("carnet existente")       
        #no funciona estando dentro de ingreso de estudiante
        #el error esta al seleccionar la opcion " 1 "

def ingreso_alumno():
    nombre = input("ingrese el nombre Nombre: ")
    carnet = input(" ingrese el carnet: ")

    lista_notas = [] 
    lista_cursos = []
            
    opcion_nota = input("ingresar nota (y/n): ")        
    while opcion_nota == 'Y' or opcion_nota == 'y':
        nota = input("ingrese la nota: ")
        try:
            nota = int(nota)
            lista_notas.append(nota)
        except:
            print("NOTA INCORRECTA 'No ingreso un numero'")
        opcion_nota = input("ingresar nota (y/n): ")
    if opcion_nota != 'Y' or opcion_nota != 'y':
            
        calculo_promedio = promedio_estudiante(lista_notas) 
        calculo = cursos_aprobados(lista_notas)
        Cursos = cursos_asignados(lista_notas)
        alumnos = {
            'Nombre ': nombre,
            'Carnet ': carnet, 
            'Notas ': lista_notas,
            'Promedio ': calculo_promedio,
            'Cursos asignados': Cursos,
            'Cursos aprobados': calculo #cursos_aprobados(lista_notas)
        }
        lista_alum.append(alumnos)     
    else:
        Calculo_Promedio = promedio_estudiante(lista_notas) 
        Calculo = curso_aprobados(lista_notas)
        cursos = cursos_asignados(lista_notas)

        alumnos = {
            'Nombre ': nombre,
            'Carnet ': carnet, 
            'Notas ': lista_notas,
            'Promedio ': Calculo_Promedio,
            'Cusrsos asignados': cursos,
            'Cursos aprobados': Calculo
        }
        lista_alum.append(alumnos)
    os.system("clear")
    print("ingreso completado")
    return          
  

def Busqueda():
    busqueda = input("ingrese el numero de carnet para buscar: ")
    for i in lista_alum:
        if busqueda == i['carnet']:
            print(lista[busqueda])
    return

def numero_alumnos():
    for i in lista_alum:
        i = len(lista_alum)
    print("Cantidad de alumnos: ",i)
    return

def mostra_lista():
    numero_alumnos()
    num = len(lista_alum)
    for num in lista_alum:
        print("------------------------------------------")
        print( "Nombre: ",notas)
        print( "Carnet: ")
        print( "Notas: ")
        print( "Promedio: ")
        print( "Cursos asignados: ")
        print( "Cursos aprobados: ")
    
def SubMenu():
    os.system("clear")
    mostrar_submenu = """\n--------------------\ningrese una opcion\n--------------------
    \n1. Guardar y Salir
    \n2. Salir sin guardar
    \n> """
    opcion_subm = input(mostrar_submenu)
    try:
        opcion_subm = int(opcion_subm)
        if opcion_subm == 1:
            with open('Datos.json','w') as archvio_a:
                print("Saliendo y Guardando base de datos...")
                json.dump(lista_alum, archvio_a)   
        elif opcion_subm == 2:
            print("Saliendo....")
        else:
            os.system("clear")
            print("Opcion: ",opcion_subm," invalido")
            os.system("pause")
            return SubMenu()
    except:
        os.system("clear")
        print("'",opcion_subm,"' no es una opcion")
        os.system("pause")
        return SubMenu()
        
def Menu_principal():
    mostrar_mensaje = """\n--------------------\ningrese una opcion\n--------------------
    \n1. Ingresar un nuevo estudiante
    \n2. Buscar un usuario
    \n3. Mostrar listado de estudiantes
    \n4. Salir\n> """
     
    opcion = input(mostrar_mensaje)
    try:
        opcion = int(opcion)
        
        if opcion == 1:
            os.system("clear")
            print("Los datos ingresados se guardaran si lo desea\n")
            os.system("pause")
            ingreso_alumno()
           
        elif opcion == 2:
            os.system("clear")
            Busqueda()
                          
        elif opcion == 3:
            os.system("clear")
            mostra_lista()
         
        elif opcion == 4:
            SubMenu() 
            return
        os.system("pause")
        Menu_principal()
        
    except:
        os.system("clear")
        print("'",opcion,"' no es una opcion")
        os.system("pause")
        os.system("clear")
        return Menu_principal()
    

              
Menu_principal()

