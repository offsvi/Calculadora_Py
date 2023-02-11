# Receber um número
# Receber u operador
# Receber um outro número
# Mostrar o resultado

print('Digite um número: ')
numero1 = float(input())

print('Digite um operador: ')
operador = input()

print('Digite outro número: ')
numero2 = float(input())

if operador == '+':
    resultado = numero1 + numero2
    print(resultado)
elif operador == '-':
    resultado = numero1 - numero2
    print(resultado)
elif operador == '*':
    resultado = numero1 * numero2
    print(resultado)
elif operador == '/':
    resultado = numero1 / numero2
    print(resultado)
else:
    print("Operador Incorreto. Tente de novo")

