#variables que pueden almacenar diferentes informacion

numeros_tel = ['104','105','999444555','123']


#en la colecciones de datos se pueden agregar diferentes tipos de datos dentro de sus elementos

numeros_tel.append(False)
numeros_tel.append(10.5)

print(numeros_tel)
print(numeros_tel[0])

#tambien se puede obtener un subconjunto de elementos de la lista
print(numeros_tel[1:3])
#todos los elementos desde la posicion 2
print(numeros_tel[2:])
#todos los elementos hasta la posicion <2
print(numeros_tel[:2])

#para obtener el ultimo elemento usamos valores negativos y asi como se invierte la lista
print(numeros_tel[-1])



#formas de eliminar elementos de una lista

#con el metodo POP retiramos el elemento de la lista y lo podemos almacenar en otra variable

valor_eliminado = numeros_tel.pop(0)
print(valor_eliminado)
print(numeros_tel)

#del > sirve para eliminar varibles (liberar espacio de memoria) y tambien se puede eliminar elementos de una lista

del numeros_tel[1]
print(numeros_tel)

#si se quiere limpiar completamente la lista

numeros_tel.clear()
print(numeros_tel)

ejercicio_1 = [1, 'Eduardo','de Rivero',False, 32, 20.5, [4,8,12]]

#como hago para obtener a 'de Rivero'

print(ejercicio_1[2])

#como hago para obtener desde eduardo hasta 32

print(ejercicio_1[1:5])

#como hago para obtener la penultima posicion 20.5

print(ejercicio_1[-2])

#como hago para obtener el valor 8

print(ejercicio_1[6][1])

#tuplas

#ordenada pero no son editables

#suelen ser usadas para las configuraciones de la aplicacion

meses=('enero','febrero','marzo','abril')

#no se pueden ni eliminar ni agregar nueva informacion a la tupla, solamente obtener informacion de la misma forma que las listas
#del mes[1]
# meses.append('mayo')

data = ('Roxana', 'Pedro', [1,2,6,['Juan', 'Aristoteles']])

#como hago para obtener aristoteles
print(data[2][3][1])

#diccionarios
#ordenado pero por llaves no por indices y es editable

persona ={
    'nombre': 'eduardo',
    'ciudad': 'arequipa',
    'estado': 'peruano',
    'nacionalidad': 'peruano',
    'direccion':{
        'calle': 'los girasoles',
        'numero': 180,
        'manzana': 3,
        'lote': None
    },
    'hobbies': ['programar','estudiar','montar bici']

}

print(persona['nombre'])

#agregar nuevos elementos al diccionario

persona['idiomas'] = ('español','ingles','quechua')

#editar un elemento del diccionario

persona['estado']= 'soltero'

#eliminar un elemento del diccionario

persona.pop('nacionalidad')
del persona['estado']

print(persona)

#se puede obtener las llaves del diccionario
print(persona.keys())
print(persona.values())

#obtener la calle en la que vive la persona

print(persona['direccion']['calle'])

#obtener los 2 ultimos hobbies de la persona

print(persona['hobbies'][-2:])

#set (conjuntos)
#similar 'al diccionario solo que no es ordenada

planetas = {'tierra','marte','jupiter','urano','venus'}

print(planetas)

planetas.add('pluton')
print(planetas)

#tener la informacion almacenada pero solamente para corroborar si esta o no 
print('neptuno' in planetas)

