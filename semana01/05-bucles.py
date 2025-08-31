alumnos = ['sebastian','jose','paolo','eduardo','keing','luis']

#for > itera determinados pasos
#in en el bucle for sirve como asignacion

for nombre_alumno in alumnos:
   if nombre_alumno == 'paolo':
        #si quiero saltarme una iteracion
        continue
   print(nombre_alumno)


# se puede iterar el texto
texto = 'hoy es fin de mes'
for letra in texto:
    print(letra)

numeros = [10, 40, 50, 60]

for numero in numeros:
    #pass indicar que aun no hay logica en este bloque de codigo
    #{}
    pass
    #for tradicional
for numero in range(4):
    print(numero)

for numero in range(1,7):
    print(numero)


print('-------------')
for numero in range(5,10,3):
    print(numero)

#bandera: variable que sirve como incrementador para contar

veces_repetidas = 0

for numero  in range (1,100,2):
    if numero == 10:
        #incrementando en 1 la cantidad del valor que tenia veces_repetidas
        veces_repetidas += 1
        #decrementando
        #veces_repetidas -= 1

#usando el siguiente texto

texto = 'hola, mi nombre es eduardo y me gustaria aprender backend'

#necesito saber cuantas vocales hay en el texto y cuantos espacios tengo

contador_vocales = 0
contador_espacios = 0

for vocales in texto:
    if vocales == 'a' or vocales == 'e' or vocales == 'i' or vocales == 'o' or vocales == 'u':
        contador_vocales+=1
    print(contador_vocales)
        