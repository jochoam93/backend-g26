#necesito saber cuantas vocales hay en el texto y cuantos espacios tengo
texto = 'hola, mi nombre es eduardo y me gustaria aprender backend'
contador_vocales = 0
contador_espacios = 0

for caracteres in texto:
    if caracteres == 'a' or caracteres == 'e' or caracteres == 'i' or caracteres == 'o' or caracteres == 'u':
        contador_vocales= contador_vocales+1
    elif caracteres == ' ':
        contador_espacios= contador_espacios+1
print('cantidad de vocales: ', contador_vocales)
print('cantidad de espacios: ', contador_espacios)