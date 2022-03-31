nome = input ('qual o seu nome? ')
print (f'prazer em te conhcer {nome:>20}')
print (f'prazer em te conhcer {nome:<20}')
print (f'prazer em te conhcer {nome:^20}')
print (f'prazer em te conhcer {nome:=^20}')

# dependendo da forma que for colocado dentro do {} irá mudar a exibição do nome
# ex: 
#  {nome:>20} <- está indicando que o nome sera movido 20 casas pra direita '>'
#  {nome:<20} <- será movido vinte casa a esquerda  '<'
#  {nome:^20} <- o sinal de '^' servira para centralizar a palavra
# dependendo do oque você colocar após os dois pontos ':' será exibido junto com a palavra
# ex: {nome:=^20}
# =======carlos=======