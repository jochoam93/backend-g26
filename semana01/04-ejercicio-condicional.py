#tengo una tienda de ropa eduardo's clothes
#tengo ropa con las siguientes caracteristicas
#masculino en las tallas xl o l 
#femenino con talla l o m


#hacer un programa que recepcione el genero y la talla e indique si tiene o no tiene stock


print("Bienvenido a eduardo's clothes")

stock = {
    'masculino':['xl','l'],
    'femenino':['l','m']
}

genero = input('ingresa tu genero:').casefold()
talla = input('ingresa tu talla:').casefold()

if genero in stock:
    if talla in stock[genero]:
        print('si hay stock para: ' + genero +  ' en talla: ' + talla)
    else:
        print('no hay stock para: ' + genero + ' en talla: ' + talla)
else:
    print('Ingresar solo genero masculino o femenino')
