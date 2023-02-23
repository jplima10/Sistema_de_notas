print('Programa para calcular a media de um aluno', end='\n\n')

nome = input('Entre com o nome do aluno: \n')

nota1 = float(input("Entre com a primeira nota: 'Utilize '.' ao inves de ',' (Ex: 7.5)'\n"))

nota2 = float(input("Entre com a segunda nota: 'Utilize '.' ao inves de ',' (Ex: 7.5)'\n"))

nota3 = float(input("Entre com a terceira nota: 'Utilize '.' ao inves de ',' (Ex: 7.5)'\n"))

nota4 = float(input("Entre com a quarta nota: 'Utilize '.' ao inves de ',' (Ex: 7.5)'\n"))

nota5 = float(input("Entre com a quinta nota: 'Utilize '.' ao inves de ',' (Ex: 7.5)'\n"))

nota6 = float(input("Entre com a sexta nota: 'Utilize '.' ao inves de ',' (Ex: 7.5)'\n"))

nota7 = float(input("Entre com a setima nota: 'Utilize '.' ao inves de ',' (Ex: 7.5)'\n"))

nota8 = float(input("Entre com a oitava nota: 'Utilize '.' ao inves de ',' (Ex: 7.5)'\n"))

media = (nota1 + nota2 + nota3 + nota4 + nota5 + nota6 + nota7 + nota8) / 8
print('{0} teve media igual a: {1}'.format(nome, media))