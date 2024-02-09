# Este programa calcula a soma, subtração, multiplicação e divisão de dois números.

# Recebe os dois números do usuário.
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))

# Calcula a soma dos dois números.
soma = n1 + n2

# Calcula a subtração dos dois números.
subtracao = n1 - n2

# Calcula a multiplicação dos dois números.
multiplicacao = n1 * n2

# Calcula a divisão dos dois números.
divisao = n1 / n2

# Imprime os resultados das operações.
print('\nA soma entre {} + {} é igual a '.format(n1, n2))
print('O resultado é = ', soma)

print('\nA subtração entre {} - {} é igual a '.format(n1, n2))
print('O resultado é = ', subtracao)

print('\nA multiplicação entre {} * {} é igual a '.format(n1, n2))
print('O resultado é = ', multiplicacao)

print('\nA divisão entre {} / {} é igual a '.format(n1, n2))
print('O resultado é = ', divisao)