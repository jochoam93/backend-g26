edad = 32
#no tenemos llaves para definir bloques de codigo
#tenemos identacion (espaciado) para indicar que ese codigo estara dentro de un bloque

if edad > 18:
    print('eres mayor de edad')
else:
    print('eres menor de edad')

print('finalizacion del if')

if edad > 18 and edad >35:
    print('puedes postular para la presidencia')
#si queremos agregar una condicional intermedia antes que ingrese al else
elif edad > 18:
    print('eres mayor de edad pero aun no puedes postular a la presidencia')
else:
    print('eres menor de edad')



numero = -1

if numero>0:
    print('numero es positivo')
elif numero == 0:
    print('numero es 0')
else:
    print('numero es negativo')

#se puede ingresar valores por la terminal

numero_ingresado= input('ingresa tu numero favorito:')

print(numero_ingresado)

print(type(numero_ingresado))

# para convertir un tipo de dato a otro

numero_ingresado_int = int(numero_ingresado)
print(type(numero_ingresado_int)) 

# > mayor , >= mayor o igual , < menor , <= menor o igual , == igual , != diferente

# ingresando el pais indicar la nacionalidad
#peru > peruano
#bolivia > boliviano
#holanda > holandes
#otro pais que no este registrado indicar que es latinoamericano

#aparte de recibir el valor lo estamos convirtiendo en minuscula para que la busqueda sea exacta
pais = input('ingresa tu pais:').casefold()
if pais == 'peru':
    print('eres peruano')
elif pais == 'bolivia':
    print('eres boliviano')
elif pais == 'holanda':
    print('eres holandes')
else:
    print('eres latinoamericano')

