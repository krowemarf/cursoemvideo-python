# Leia algo pelo teclado e mostre todas as suas informações
frase = input('Digite algo: ')
print(f'Contém apenas letras? {frase.isalpha()}')
print(f'Contém apenas números? {frase.isnumeric()}')
print(f'É alfanúmerico? {frase.isalnum()}')
print(f'Está todo escrito em MAIÚSCULAS? {frase.isupper()}')
print(f'Está todo escrito em minúsculas? {frase.islower()}')
print(f'Está escrito como título? {frase.istitle()}')
