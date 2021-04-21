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

def porc_cursos_reprobados(lista_notas):
    Repro = cursos_reprobados()
    Asig = cursos_asignados()
    total_r = Repro/Asig
    porcen_reprobados = total_r * 100
    return porcen_reprobados

def porc_cursos_ganados(lista_notas):
    Apro = cursos_aprobados()
    Asig = cursos_asignados()
    total_a = Apro/Asi
    porcentaje = total_a * 100
    return porcentaje

def cursos_reprobados(lista_notas):
    j = numero_alumnos()
    if j == 0:
        return j
    else:
        for nots in lista_notas:
            if nots < 61:
                return nots 
 
def cursos_aprobados(lista_notas):
    i = numero_alumnos()
    if i == 0:
        return i
    else:
        for nota in lista_notas:
            if nota >= 61:
                return nota    
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

def comparando_carnet():
    if carnet == lista_alum['carnet']:
        print("carnet existente")       
        return
    
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
        Cursos = cursos_asignados(lista_notas)
        #cu_aprobados = cursos_aprobados()
        #cu_reprobados = cursos_reprobados(lista_notas)
        
        alumnos = {
            'Nombre ': nombre,
            'Carnet ': carnet, 
            'Notas ': lista_notas,
            'Promedio ': calculo_promedio,
            'Cursos asignados': Cursos,
            #'Cursos Aprobados': cu_aprobados 
        }
        lista_alum.append(alumnos)     
    else:
        Calculo_Promedio = promedio_estudiante(lista_notas) 
        cursos = cursos_asignados(lista_notas)
        #Cu_aprobados = cursos_aprobados(lista_notas)
        alumnos = {
            'Nombre ': nombre,
            'Carnet ': carnet, 
            'Notas ': lista_notas,
            'Promedio ': Calculo_Promedio,
            'Cusrsos asignados': cursos,
            #'Cursos aprobados': Cu_aprobados
        }
        lista_alum.append(alumnos)
    os.system("clear")
    print("ingreso completado")
    os.system("pause")
    return          
  

def Busqueda():
    if len(lista_alum) == 0:
        print("Vacio!")
    else:
        busqueda = input("Para buscar ingrese el numero de carnet: ")
        try:
            for i in lista_alum:
                if i == lista_alum['Carnet']:
                    return lista_alum[i]
        except:
            print("No encontrado")    
         
def numero_alumnos():
    for i in lista_alum:
        i = len(lista_alum)
    print("Cantidad de alumnos: ",i)
    return

def mostra_lista():
    #for num in lista_alum:
        #print("------------------------------------------")
        #print( "Nombre: ",lista_alum['nombre'])
        #print( "Carnet: ",lista_alum['carnet'])
        #print( "Notas: ",lista_alum['lista_notas'])
        #print( "Promedio: ",lista_alum['Calculo_promedio'])
        #print( "Cursos asignados: ",lista_alum['cursos'])
        #print( "Cursos aprobados: ",lista_alum['Calculo'])
    if len(lista_alum) == 0:
            print("Vacio")
    else:
        numero_alumnos()
        print(lista_alum)           

def eliminar():
    num_elementos = len(lista_alum)      
    mensaje = """-----------------\ningrese una opcion\n---------------
    \n1. borrar todos los datos
    \n2. volver a menu de salida
    \n> """
        
    opcion_m = input(mensaje)
    try: 
        opcion_m = int(opcion_m)
        if opcion_m == 1:
            for i in range(num_elementos):
                lista_alum.remove(lista_alum[0])
            print("recuerde que al salir y guardar se aplicaran los cambios realizados")
            os.system("pause")
            
        elif opcion_m == 2:
            SubMenu()              
        
        with open('Base_de_Datos.json', 'w') as archivo:
            json.dump(lista_persona, archivo)
    except:
        return Menu_principal()
 
def SubMenu():
   
    os.system("clear")
    mostrar_submenu = """\n--------------------\ningrese una opcion\n--------------------
    \n1. Guardar y Salir
    \n2. Salir sin guardar
    \n3. Eliminar datos almacenados
    \n4. Volver al menu
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
        elif opcion_subm == 3:
            eliminar()    
        elif opcion_subm == 4:
            Menu_principal()
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
    \n4. Salir
    \n> """
     
    opcion = input(mostrar_mensaje)
    try:
        opcion = int(opcion)
        
        if opcion == 1:
            os.system("clear")
            print("Los datos ingresados se guardaran si asi lo desea\n")
            ingreso_alumno()
           
        elif opcion == 2:
            os.system("clear")
            Busqueda()
            os.system("pause")
                          
        elif opcion == 3:
            os.system("clear")
            mostra_lista()
            os.system("pause")
          
        elif opcion == 4:
            SubMenu()
            return
        os.system("clar")
        Menu_principal()
        
    except:
        os.system("clear")
        print("'",opcion,"' no es una opcion")
        os.system("pause")
        os.system("clear")
        return Menu_principal()
                
Menu_principal()
