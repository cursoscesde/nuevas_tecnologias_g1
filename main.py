# algoritmo para saber cual de los 3 números es el mayor
# number1 = int(input("Ingrese primer número: "))
# number2 = int(input("Ingrese segundo número: "))
# number3 = int(input("Ingrese tercer número: "))

# # operadoares lógicos &&(and), ||(or)
# if number1 > number2 and number1 > number3:
#     print("El número 1 es el mayor")
# if number2 > number1 and number2 > number3:
#     print("El número 2 es el mayor")
# else:
#     print("El número 3 es el mayor")

# if number1 > number2 and number1 > number3:
#     print("El número 1 es el mayor")
# elif number2 > number1 and number2 > number3:
#     print("El número 2 es el mayor")
# else:
#     print("El número 3 es el mayor")
# for i in range(5): # for(let i=0; i<5; i++)
#     print(i)
# pida 5 el nombre y 5 notas a un estudiante y calcule su nota final (promedio)
# promedio = sumatorio total / numero de datos
# average = 0
# name = input("Ingrese nombre: ")
# for i in range(1,6):
#     average += float(input(f"Ingrese nota {i}: "))

# average = average / 5
# print(f"Nombre: {name} - Nota: {average}")

# average = 0
# name = input("Ingrese nombre: ")
# count = 1
# while count < 6:
#     average += float(input(f"Ingrese nota {count}: "))
#     count += 1
    
#     if count == 3:
#         break
#     print(count)

# average = average / 5
# print(f"Nombre: {name} - Nota: {average}")

    # average = average + float(input("Ingrese nota 1"))

# lista
# myArray = [2,5,2.5,5,6,7,2.5,2.5,2.5] # tamaño : 6 - 0-5
# myArray[0] = 4
# for i in myArray:
#     print(i)

# # agrego un nuevo elemento al final del array
# #myArray.append("Esteban")
# print(myArray)
# myArray.remove(2.5)
# print(myArray)
# myArray.reverse()
# print(myArray)
# myArray.sort()
# print(myArray)
# myArray.insert(2, 10)
# print(myArray)

# # tuplas
# myTupla = (2,5,6,8,"hola")

# print(myTupla[0])

# # diccionarios
# myDictionary = {"name":15, 
#                 "identification": 12343, 
#                 "lastname": "hola",
#                 "myData": [1,2,3,5,6,7]
#                 }

# print(myDictionary["myData"][0])
# #un profesor necesita obtener el nombre de cada estudiante y sus 5 rspectivas notas y debe mostrar la lista de los estudiantes con su respectiva nota final
# names = []
# grades = []
def average(numberGrades):
    result = 0
    for i in range(1,numberGrades+1):
        result += float(input(f"ingrese la nota {i}: "))
    
    return result/numberGrades

students = []

while True:
    #names.append(input("Ingrese nombre del estudiante: "))
    name = input("Ingrese nombre del estudiante: ")
    numberGrades = input("Ingrese cuántas notas va a ingresar por estudiante")
    finalGrade = average(numberGrades)
    students.append({"name": name, "grade": finalGrade})
    #grades.append(average)
    stopProgram = input("Desea parar el programa (s - si, otra tecla continuar)")
    if stopProgram == "s" or stopProgram == "S":
        break

# for i in range(len(names)):
#     print(f"{names[i]} --- {grades[i]}")
for i in range(len(students)):
    print(f"{i + 1}: El estudiante {students[i]['name']} obtuvo: {students[i]['grade']}")

# myString = "Hola como estas"
# print(myString[2:8])