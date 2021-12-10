a = input('Ingrese un valor para el número a: ')
b = input('Ingrese un valor para el número b: ')
a = int(a)
b = int(b)
while a >= b:
    print('El valor de b no puede ser menor o igual que a')
    b = input('Ingrese un valor para el número b: ')
    b = int(b)
print('Los números entre a y b son: ')
numero = a + 1
while numero < b:
    print(numero)
    numero = numero + 1