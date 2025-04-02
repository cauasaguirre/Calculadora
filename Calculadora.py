import math
import pyfiglet

def somar(n1, n2):
    return n1 + n2

def subtrair(n1, n2):
    return n1 - n2

def multiplicar(n1, n2):
    return n1 * n2

def dividir(n1, n2):
    return n1 / n2 if n2 != 0 else 'Erro: Divisão por zero!'

def bhaskara(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        return ("A equação não possuí raizes")
    elif delta == 0:
        x = -b / (2*a)
        return (f"A equação possuí uma raiz real: x = {x:.2f} ")
    else:
        x1 = (-b + math.sqrt(delta))/2*a
        x2 = (-b - math.sqrt(delta))/2*a
        return (f"As raízes da equação são x1 = {x1:.2f}, x2 = {x2:.2f} ")

def raiz_quadrada(n):
    return math.sqrt(n) if n >= 0 else 'Inválido'

def porcentagem(n, p):
    return (n * p) / 100

def regra_de_tres(a, b, c):
    return (b * c) / a

def regra_de_tres_composta(a1, b1, a2, b2, b3):
    return (a1 * b3 * b2) / (b1 * b2)

def conjuntos(c1, c2):
    return (f"Interseção:{c1 & c2}, União:{c1 | c2}, Diferença: {c1 - c2}")


def sistemas_lineares(a1, b1, c1, a2, b2, c2):
    det = a1 * b2 - a2 * b1
    if det:
        return (c1 * b2 - b1 * c2) / det, (a1 * c2 - a2 * c1) / det
    return 'O sistema não possui solução única!'

def proporcao(a, b, d):
    return (a * d) / b

def potencia(x,y):
    return(math.pow(x,y))

def exibir_titulo():
    titulo = pyfiglet.figlet_format("Calculadora")
    print(titulo)


exibir_titulo()


def exibir_menu():
    print("=" * 55)
    opcoes = ["Somar", "Subtrair", "Multiplicar", "Dividir", "Bhaskara", "Raiz Quadrada", "Porcentagem",
              "Regra de Três", "Regra de Três Composta", "Conjuntos", "Sistemas Lineares", "Proporção", "Potência",
              "Sair"]

    largura = 55  

    for i, opcao in enumerate(opcoes, 1):

        texto_formatado = f'[{i}] {opcao}'
        print(f'\033[1;30;47m{texto_formatado.center(largura)}\033[m')

    print("=" * 55)

def main():
    while True:
        exibir_menu()
        try:
            opcao = int(input('\033[1;30;47m Digite sua opção: \033[m'))
            if opcao == 1:
                n1 = float(input('Digite o primeiro número: '))
                n2 = float(input('Digite o segundo número: '))
                print(f'O resultado da soma é: {somar(n1, n2)}')
            elif opcao == 2:
                n1 = float(input('Digite o primeiro número: '))
                n2 = float(input('Digite o segundo número: '))
                print(f'O resultado da subtração é: {subtrair(n1, n2)}')
            elif opcao == 3:
                n1 = float(input('Digite o primeiro número: '))
                n2 = float(input('Digite o segundo número: '))
                print(f'O resultado da multiplicação é: {multiplicar(n1, n2)}')
            elif opcao == 4:
                n1 = float(input('Digite o primeiro número: '))
                n2 = float(input('Digite o segundo número: '))
                print(f'O resultado da divisão é: {dividir(n1, n2)}')
            elif opcao == 5:
                a = int(input('Digite A: '))
                b = int(input('Digite B: '))
                c = int(input('Digite C: '))
                print(bhaskara(a, b, c))
            elif opcao == 6:
                n = float(input('Digite o número: '))
                print(f'O resultado da raiz quadrada é: {raiz_quadrada(n)}')
            elif opcao == 7:
                n = float(input('Digite o valor: '))
                p = float(input('Digite a porcentagem: '))
                print(f'O resultado da porcentagem é: {porcentagem(n, p)}')
            elif opcao == 8:
                a = int(input('Digite A: '))
                b = int(input('Digite B: '))
                c = int(input('Digite C: '))
                print(f'O resultado da regra de três é: {regra_de_tres(a, b, c)}')
            elif opcao == 9:
                a1 = int(input('Digite A1: '))
                b1 = int(input('Digite B1: '))
                a2 = int(input('Digite A2: '))
                b2 = int(input('Digite B2: '))
                b3 = int(input('Digite B3: '))
                print(f'O resultado da regra de três composta é: {regra_de_tres_composta(a1, b1, a2, b2, b3)}')
            elif opcao == 10:
                c1 = list(map(int, input('Digite os números do primeiro conjunto (separados por espaço): ').split()))
                c2 = list(map(int, input('Digite os números do segundo conjunto (separados por espaço): ').split()))
                c1 = set(c1)
                c2 = set(c2)
                print(f'O resultado do conjunto é: {conjuntos(c1, c2)}')
            elif opcao == 11:
                a1 = float(input('Digite a1: '))
                b1 = float(input('Digite b1: '))
                c1 = float(input('Digite c1: '))
                a2 = float(input('Digite a2: '))
                b2 = float(input('Digite b2: '))
                c2 = float(input('Digite c2: '))
                print(f'O resultado do sistema linear é: {sistemas_lineares(a1, b1, c1, a2, b2, c2)}')
            elif opcao == 12:
                a = float(input('Digite a: '))
                b = float(input('Digite b: '))
                d = float(input('Digite d: '))
                print(f'O resultado da proporção é: {proporcao(a, b, d)}')
            elif opcao == 13:
                x = float(input("Digite um número: "))
                y = float(input("Digite outro número: "))
                print(f'O resultado da potência é: {potencia(x,y)}')
            elif opcao == 14:
                print("Saindo do programa...")
                break
            else:
                print('Opção inválida!')
        except ValueError:
            print('Por favor, insira um número válido.')

if __name__ == "__main__":
    main()