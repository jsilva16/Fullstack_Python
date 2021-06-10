# Utilice funciones para calcular lo siguiente
# Ingrese por pantalla 4 notas de un alumno (Pruebas)
# Calcule el promedio de notas de presentación a examen
# Solicite la nota del examen
# Calcule el promedio final de la nota de presentación y la nota del examen
# nota_final = nota_presentacion*0.7+examen*0.3
# Valide el rango de las notas entre (1-7)
# El alumno debe obtener en el examen al menos un 3.5 para aprobar el curso
# El aprueba con un promedio o nota final es mayor o igual a 3.95
# Imprima en pantalla el promedio y el estado del alumno ("Aprobado", "Reprobado")


def promedio():
    suma=0.0
    notas=[]
    for i in range(4):
        nota=float(input("Ingrese la nota "+str(i+1)+": "))
        while nota<1 or nota>7:
            print("La nota ingresada está fuera de rango")
            nota=float(input("Ingrese la nota "+str(i+1)+": "))
            if nota>=1 and nota<=7:
                break
            
        notas.append(nota)
        suma+=nota
    avg=suma/len(notas)
    print("El promedio de notas es: ",avg)
    examen=float(input("Ingrese la nota del examen: "))
    while examen<1 or examen>7:
            print("La nota ingresada está fuera de rango")
            examen=float(input("Ingrese la nota "+str(i+1)+": "))
            if examen>=1 and examen<=7:
                break
    nota_final= (avg*0.7)+(examen*0.3)
    if nota_final<3.95 or examen<3.5 or avg<3.95:
        estado = "REPROBADO"
    else:
        estado = "APROBADO"
    print("El promedio de notas es: ",avg)
    print("La nota del examen es: ",examen)
    print("La nota final es: ",nota_final)
    print("El alumno ha "+estado+" el curso!")

promedio()
