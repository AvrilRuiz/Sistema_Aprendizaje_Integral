nombre_archivo = "preguntas_guardadas.txt"
def leer_archivo(nombre):
  preguntas = []
  with open(nombre_archivo, "r") as archivo:
    contenido = archivo.readlines()
    for linea in contenido:
      strings = linea.split(",")
      strings[7] = strings[7][:-1]
      strings[0] = int(strings[0])
      strings[1] = int(strings[1])
      preguntas.append(strings)
  return preguntas


def grabar_archivo(nombre, lista_preguntas):
  with open(nombre, "w") as archivo:
    for pregunta in lista_preguntas:
      pregunta[0] = str(pregunta[0])
      pregunta[1] = str(pregunta[1])
      texto = ",".join(pregunta)
      archivo.write(texto + "\n")

enfoques = ["", "Lectura", "Matemáticas", "Ciencias"]
ids_mate = []
ids_lectura = []
ids_ciencias = []
preguntas_quiz = []
contador_usuario = 0
calificaciones = []


def registrar_pregunta():
  preguntas = leer_archivo(nombre_archivo)
  pregunta = []
  print("Bienvenido a la opción para registrar preguntas, por favor sigue las instrucciones")
  id_pregunta = len(preguntas) + 1
  print(f"ID de la pregunta: {id_pregunta}")
  pregunta.append(id_pregunta)
  while True:
    enfoque = int(input("Ingresa el número de enfoque de la pregunta:\n"
    "Para Lectura escriba 1, Para Matemáticas escriba 2, Para Ciencias escriba 3: "))
    if enfoque >= 1 and enfoque <= 3:
      pregunta.append(enfoque)
      break
    else:
      print("Número incorrecto.\n")
  texto_pregunta = input("Ingresa el texto de la pregunta: ")
  pregunta.append(texto_pregunta)
  for num in range(4):
    respuesta = input("Ingresa la respuesta " + str(num + 1) + ": ")
    pregunta.append(respuesta)
  correcta = input("Ingresa la respuesta correcta: ")
  pregunta.append(correcta)
  preguntas.append(pregunta)
  grabar_archivo(nombre_archivo, preguntas)


def actualizar_pregunta():
  preguntas = leer_archivo(nombre_archivo)
  existe = False
  print("Bienvenido a la opción para actualizar preguntas, por favor sigue las instrucciones \n"
  "A continuación se despliega la lista de preguntas guardadas\n")
  print(preguntas)
  for pregunta in preguntas:
    id_pregunta, enfoque, texto_pregunta, respuesta1, respuesta2, respuesta3, respuesta4, correcta = pregunta  # esto (pregunta) es una lista, hacemos asignación múltiple
    print(f"ID de la pregunta: {id_pregunta} \nEnfoque de la pregunta: {enfoques[enfoque]} \nPregunta: {texto_pregunta}")
    print(f"a){respuesta1:<15}b){respuesta2:<15}c){respuesta3:<15}d){respuesta4:<15} \n")
  id_cambio = int(input("Ingresa el id de la pregunta que quieres cambiar: "))
  for pregunta in preguntas:
    id_pregunta, enfoque, texto_pregunta, respuesta1, respuesta2, respuesta3, respuesta4, correcta = pregunta
    if id_cambio == id_pregunta:
      existe = True
      print(f"\nPregunta: {texto_pregunta}\na){respuesta1:<15}b){respuesta2:<15}c){respuesta3:<15}d){respuesta4:<15}\nCorrecta: {correcta}")
      enfoque_nuevo = input("Ingresa el número de enfoque de la pregunta:\n"
                      "Para Lectura escriba 1, Para Matemáticas escriba 2, Para Ciencias escriba 3: ")
      texto_pregunta_nueva = input("Ingresa el texto de la pregunta: ")
      respuesta_nueva1 = input("Ingresa la respuesta 1: ")
      respuesta_nueva2 = input("Ingresa la respuesta 2: ")
      respuesta_nueva3 = input("Ingresa la respuesta 3: ")
      respuesta_nueva4 = input("Ingresa la respuesta 4: ")
      correcta_nueva = input("Ingresa la respuesta correcta:")
      pregunta_seguro = input("¿Está seguro de que quiere actualizar los datos de la pregunta? (si/no): ")
      if pregunta_seguro.lower() == "si":
        if enfoque_nuevo == '':
          pass
        else:
          pregunta[1] = int(enfoque_nuevo)
        if texto_pregunta_nueva == '':
          pass
        else:
          pregunta[2] = texto_pregunta_nueva
        if respuesta_nueva1 == '':
          pass
        else:
          pregunta[3] = respuesta_nueva1
        if respuesta_nueva2 == '':
          pass
        else:
          pregunta[4] = respuesta_nueva2
        if respuesta_nueva3 == '':
          pass
        else:
          pregunta[5] = respuesta_nueva3
        if respuesta_nueva4 == '':
          pass
        else:
          pregunta[6] = respuesta_nueva4
        if correcta_nueva == '':
          pass
        else:
          pregunta[7] = correcta_nueva
      else:
        pass
      break
  if not existe:
    print("No existe ninguna pregunta con este ID.")
  grabar_archivo(nombre_archivo, preguntas)


def organizar_preguntas(lista_preguntas):
  for pregunta in lista_preguntas:
    id_pregunta, enfoque, texto_pregunta, respuesta1, respuesta2, respuesta3, respuesta4, correcta = pregunta
    if enfoque == 1 and id_pregunta not in ids_lectura:
      ids_lectura.append(id_pregunta)
    elif enfoque == 2 and id_pregunta not in ids_mate:
      ids_mate.append(id_pregunta)
    elif enfoque == 3 and id_pregunta not in ids_ciencias:
      ids_ciencias.append(id_pregunta)


def estudiar_area():
  preguntas = leer_archivo(nombre_archivo)
  organizar_preguntas(preguntas)
  preguntas_estudiar = []
  print("Bienvenido a la opción para estudiar preguntas de cierta área, por favor sigue las instrucciones: \n")
  enfoque_estudiar = int(input("Ingrese el área de enfoque a estudiar\nPara Lectura escriba 1, Para Matemáticas escriba 2, Para Ciencias escriba 3: "))
  if enfoque_estudiar == 1:
    print(f"Cantidad de preguntas disponibles del enfoque Lectura: {len(ids_lectura)}")
  elif enfoque_estudiar == 2:
    print(f"Cantidad de preguntas disponibles del enfoque Matemáticas: {len(ids_mate)}")
  elif enfoque_estudiar == 3:
    print(f"Cantidad de preguntas disponibles del enfoque Ciencias: {len(ids_ciencias)}")
  cantidad_preguntas = int(input("Ingrese la cantidad de preguntas a estudiar: "))
  if enfoque_estudiar == 1 and len(ids_lectura) >= cantidad_preguntas:
    for num in range(cantidad_preguntas):
      preguntas_estudiar.append(ids_lectura[num])
    for id in preguntas_estudiar:
      id_pregunta, enfoque, texto_pregunta, respuesta1, respuesta2, respuesta3, respuesta4, correcta = preguntas[id - 1]
      print(f"\nPregunta: {texto_pregunta}\na){respuesta1:<15}b){respuesta2:<15}c){respuesta3:<15}d){respuesta4:<15}\nCorrecta: {correcta}")
  elif enfoque_estudiar == 2 and len(ids_mate) >= cantidad_preguntas:
    for num in range(cantidad_preguntas):
      preguntas_estudiar.append(ids_mate[num])
    for id in preguntas_estudiar:
      id_pregunta, enfoque, texto_pregunta, respuesta1, respuesta2, respuesta3, respuesta4, correcta = preguntas[id - 1]
      print(f"\nPregunta: {texto_pregunta}\na){respuesta1:<15}b){respuesta2:<15}c){respuesta3:<15}d){respuesta4:<15}\nCorrecta: {correcta}")
  elif enfoque_estudiar == 3 and len(ids_ciencias) >= cantidad_preguntas:
    for num in range(cantidad_preguntas):
      preguntas_estudiar.append(ids_ciencias[num])
    for id in preguntas_estudiar:
      id_pregunta, enfoque, texto_pregunta, respuesta1, respuesta2, respuesta3, respuesta4, correcta = preguntas[id - 1]
      print(f"\nPregunta: {texto_pregunta}\na){respuesta1:<15}b){respuesta2:<15}c){respuesta3:<15}d){respuesta4:<15}\nCorrecta: {correcta}")
  else:
    print("No hay suficientes preguntas de esta área.")


def presentar_quiz():
  preguntas = leer_archivo(nombre_archivo)
  global contador_usuario
  preguntas_quiz.clear()
  organizar_preguntas(preguntas)
  existe_enfoque1 = False
  existe_enfoque2 = False
  existe_enfoque3 = False
  if len(preguntas) >= 10:
    if len(ids_lectura) >= 1 and len(ids_mate) >= 1 and len(ids_ciencias) >= 1:
      # rellenar la lista preguntas_quiz con las primeras 8 listas de preguntas
      for num in range(8):
        preguntas_quiz.append(preguntas[num])
      for pregunta in preguntas_quiz:
        id_pregunta, enfoque, texto_pregunta, respuesta1, respuesta2, respuesta3, respuesta4, correcta = pregunta
        if enfoque == 1:
          existe_enfoque1 = True
        if enfoque == 2:
          existe_enfoque2 = True
        if enfoque == 3:
          existe_enfoque3 = True
      if existe_enfoque1 and existe_enfoque2 and existe_enfoque3:
        completar_1_2_3(preguntas)  # completar las 2 que faltan
      elif existe_enfoque1 and existe_enfoque2:
        completar_1_2(preguntas)  # completar las 2 que faltan con 3
      elif existe_enfoque1 and existe_enfoque3:
        completar_1_3(preguntas)  # completar las 2 que faltan con 2
      elif existe_enfoque2 and existe_enfoque3:
        completar_2_3(preguntas)   # completar las 2 que faltan con 1
      elif existe_enfoque1:
        completar_1(preguntas)  # completar las 2 que faltan con 2 y 3
      elif existe_enfoque2:
        completar_2(preguntas)     # completar las 2 que faltan con 1 y 3
      elif existe_enfoque3:
        completar_3(preguntas)   # completar las 2 que faltan con 2 y 1
      else:
        print("Todos los casos fueron cubierto y esto nunca se debe imprimir.")
    else:
      print("Debe haber al menos 1 pregunta de cada enfoque.")
  else:
    print("Deben haber al menos 10 preguntas.")
  contador_correctas = 0
  contador_incorrectas = 0
  import time
  print(f"\nEl quiz tiene una duración de 20 minutos.")
  start = time.time()
  for pregunta in preguntas_quiz:
    id_pregunta, enfoque, texto_pregunta, respuesta1, respuesta2, respuesta3, respuesta4, correcta = pregunta
    print(f"\nPregunta: {texto_pregunta}\n{respuesta1:<15}{respuesta2:<15}{respuesta3:<15}{respuesta4:<15} \n")
    respuesta_usuario = input("¿Cuál es la respuesta correcta? ")
    finish = time.time()
    segundos_en_contestar = finish - start
    segundos_restantes = 1200 - segundos_en_contestar
    print(f"\nTiempo restante: {int(segundos_restantes // 60)} minutos y {round(segundos_restantes % 60)} segundos.")
    if respuesta_usuario == correcta:
      contador_correctas += 1
    else:
      contador_incorrectas += 1
  contador_usuario += 1
  calificaciones.append(contador_correctas)


def completar_1_2_3(preguntas):
  preguntas_quiz.append(preguntas[-1])
  preguntas_quiz.append(preguntas[-2])


def completar_1_2(preguntas):
  if len(ids_ciencias) > 1:
    # agregar las dos preguntas de el enfoque de ciencias
    preguntas_quiz.append(preguntas[ids_ciencias[0] - 1])
    preguntas_quiz.append(preguntas[ids_ciencias[1] - 1])
  else:
    preguntas_quiz.append(preguntas[-1])
    preguntas_quiz.append(preguntas[ids_ciencias[0]-1])   # agregar el único elemento de preguntas ciencias



def completar_1_3(preguntas):
  if len(ids_mate) > 1:
    # agregar las dos preguntas de el enfoque de mate
    preguntas_quiz.append(preguntas[ids_mate[0] - 1])
    preguntas_quiz.append(preguntas[ids_mate[1] - 1])
  else:
    preguntas_quiz.append(preguntas[-1])
    preguntas_quiz.append(preguntas[ids_mate[0] - 1])   # agregar el único elemento de preguntas mate


def completar_2_3(preguntas):
  if len(ids_lectura) > 1:
    # agregar las dos preguntas de el enfoque de lectura
    preguntas_quiz.append(preguntas[ids_lectura[0] - 1])
    preguntas_quiz.append(preguntas[ids_lectura[1] - 1])
  else:
    preguntas_quiz.append(preguntas[-1])
    preguntas_quiz.append(preguntas[ids_lectura[0] - 1])   # agregar el único elemento de preguntas lectura


def completar_1(preguntas):
  preguntas_quiz.append(preguntas[ids_mate[0] - 1])
  preguntas_quiz.append(preguntas[ids_ciencias[0] - 1])


def completar_2(preguntas):
  preguntas_quiz.append(preguntas[ids_lectura[0] - 1])
  preguntas_quiz.append(preguntas[ids_ciencias[0] - 1])


def completar_3(preguntas):
  preguntas_quiz.append(preguntas[ids_lectura[0] - 1])
  preguntas_quiz.append(preguntas[ids_mate[0] - 1])


def reportar_calificaciones():
  if contador_usuario > 0:
    promedio = sum(calificaciones * 10) / len(calificaciones)
    total_preguntas = contador_usuario * 10
    total_preguntas_correctas = sum(calificaciones)
    porcentaje_correctas = (total_preguntas_correctas * 100) / total_preguntas
    porcetaje_incorrectas = 100 - porcentaje_correctas
    print(f"Total de usuarios:           {contador_usuario}\nPromedio de calificaciones:  {promedio}\n"
          f"Preguntas correctas:         {porcentaje_correctas}%\nPreguntas incorrectas:       {porcetaje_incorrectas}%")
  else:
    print("Aún no hay calificaciones por reportar.")

def menu():
  print("""Menú de opciones:
        1.	Alta de preguntas de prueba PISA (lectura, matemáticas, ciencias)
        2.	Actualizar preguntas de la prueba PISA (lectura, matemáticas, ciencias)
        3.	Estudiar preguntas de cierta área (lectura, matemáticas, ciencias)
        4.	Presentar un quiz (lectura, matemáticas, ciencias)
        5.	Reporte de calificaciones
        6.	Salir"""
  )
  opcion = int(input("Selecciona una opción: "))
  return opcion


def salir():
  print("Gracias por usar el sistema, hasta pronto!")


def main():
  opcion = 0

  while opcion != 6:
    opcion = menu()
    if opcion == 1:
      registrar_pregunta()
    elif opcion == 2:
      actualizar_pregunta()
    elif opcion == 3:
      estudiar_area()
    elif opcion == 4:
      presentar_quiz()
    elif opcion == 5:
      reportar_calificaciones()
    elif opcion > 6 or opcion < 1:
      print("Opción incorrecta")
  salir()


if __name__ == '__main__':
    main()