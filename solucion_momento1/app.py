numAlumnos = 0
students = []
listPrograms = [{"program":"telecominicaciones", "shortName": "T", "countWomen": 0, "countMen":  0, "countNotBinary": 0, "average": 0}, {"program":"software", "shortName": "S", "countWomen": 0, "countMen":  0, "countNotBinary": 0, "average": 0}]

countWomen = 0
countMen = 0
countStudents = 0

def averageStudent():
    average = 0
    for j in range(1,6):
        average = average + float(input(f"Ingrese nota {j}: "))
    average = average / 5
    return average


def updateDataProgram(data):
    for i in range(len(listPrograms)):
        if listPrograms[i]['shortName'] == data['shortName']:
            listPrograms[i]["average"] += data['average']
            if sex == "m" or sex == "M":
                listPrograms[i]["countWomen"]+=1
            elif sex == "h" or sex == "H":
                listPrograms[i]["countMen"]+=1
            elif sex == "nb" or sex=="NB":
                listPrograms[i]["countNotBinary"]+=1
            break


def printProgramsData():
    for program in listPrograms:
        average = program['average']/(program['countWomen'] + program['countMen'] + program['countNotBinary'])
        print(f"programa: {program['program']} - número mujeres: {program['countWomen']} - número de hombres: {program['countMen']} - número no binarios: {program['countNotBinary']} - Promedio académico: {average}")


def printStudentsData():
    for student in students:
        print(f"nombre: {student['name']} - promedio: {student['average']}")


while True:
    menu = input("¿Qué desea hacer? - admision(admi) - matrícula(matri) - Agregar programa(prog) - cualquier otra tecla para salir: ")
    if menu == "prog":
        programName = input("ingrese nombre del programa: ")
        shortName = input("Ingrese una abreviatura para el nombre del programa. Ejemplo MRC: ")
        listPrograms.append({"program": programName, "shortName": shortName})

    elif menu == "admi":
        numAlumnos = int(input("Ingrese número de alumnos: "))
        for i in range(1, numAlumnos+1):
            name = input(f"Ingrese nombre del alumno {i}: ")
            programs = ""
            for program in listPrograms:
                programs+= f"{program['program']} ({program['shortName']}) - "
            academicProgram = input(f"Ingrese programa académico -> {programs}")
            sex = input("Ingrese sexo - m(mujer), h(hombre), nb(no binario): ")
            
            average = averageStudent()
            updateDataProgram({"shortName": academicProgram.upper(), "sex": sex, "average": average})
            students.append({"name": name, "average": average})
    
    elif menu == "matri":
        while True:
            average+=int(input("Ingrese edad"))
            sex = input("Ingrese sexo")
            if sex == "m" or sex == "M":
                countWomen+=1
            elif sex == "h" or sex == "H":
                countMen+=1
            stopAdmission = input("si desea parar de matricular ingrese 0, de lo contrario cualquier tecla para continuar")
            countStudents+=1
            if stopAdmission == 0:
                break

        averageAge = averageAge/countStudents
        print(f"Número de estudiantes matriculados: {countStudents}")
        print(f"Promedio de edad de matriculados: {averageAge}")
        print(f"Número de mujeres matriculadas: {countWomen}")
        print(f"Número de hombre matriculados: {countMen}")
    
    elif menu != "prog" and menu != "admi" and menu != "matri":
        break

printProgramsData()
printStudentsData()
