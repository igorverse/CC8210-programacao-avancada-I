'''
Faça uma função chamada media que receba três notas de um aluno como parâmetros e uma letra. 
Se a letra for A, a função deverá calcular a média aritmética das notas do aluno; 
se for P deverá calcular a média ponderada com pesos 5, 3 e 2. 
A média calculada deve ser devolvida à função principal para, então, ser impressa.

Exemplo de entrada:
2
3
4
A

Exemplo de saída:
3.0
'''

def media(n1, n2, n3, typeOfAverage):
    if typeOfAverage.upper() == 'A':
        
        return (n1 + n2 + n3) / 3
    
    if typeOfAverage.upper() == 'P':
        
        return (n1 * 5 + n2 * 3 + n3 * 2) / 10


print(media(10,9,10, 'P'))
