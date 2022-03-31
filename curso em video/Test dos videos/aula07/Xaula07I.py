#n1 = float(input('qual o comprimento da parde?'))
#n2 = float(input('qual a altura da parede?: '))
#n3 = (n1 * n2)
#print(f'sera necessario {n3 * (2 ** 2)} de tinta para pintar a parede')

# /\ não funciono

# \/ correção - funcional
n1 = float(input('qual o comprimento da parade?: '))
n2 = float(input('qual a altura da parede?: '))
n3 = n1 * n2
print('sua parede ten a dimensão de {}x{} e sua área é de {}m².'.format(n1,n2,n3))
tinta = n3 / 2 
print('para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))

