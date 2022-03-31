from cgi import print_arguments
from tkinter import N


n1 = int(input('digite um valor '))
n2 = int(input('digite outro valor '))
print(f'o valor da soma é: {n1 + n2} ')
print(f'o valor da subtração é: {n1 - n2}')
print(f'o valor da multiplicação é: {n1 * n2}')
print(f'o valor da divisão é: {n1 / n2:.3f}')
print(f'o valor da divisão inteira é: {n1 // n2}')
print(f'o valor da potência é: {n1 ** n2}') 