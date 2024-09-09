from SOMA import calcular_soma
from fibonnaci import fibonacci
from faturamentojson import processar_faturamento_json
from faturamentoxml import processar_faturamento_xml
from percentfaturamento import calcular_percentual_faturamento
from inversor import inverter_string

def exibir_menu():
    print("Escolha uma opção:")
    print("1. Calcular a SOMA")
    print("2. Fibonnaci")
    print("3.1. faturamento do dados.json")
    print("3.2. faturamento do dados.xml")
    print("4. percentual de faturamento")
    print("5. inverter string")
    print("0. Sair")

def main():
    while True:
        exibir_menu()
        escolha = input("Digite o número da opção: ")

        if escolha == '1':
            print(f"Soma dos números de 1 a 13: {calcular_soma()}")
        elif escolha == '2':
            numero = int(input("Digite um número: "))
            if fibonacci(numero):
                print(f"{numero} pertence à sequência de Fibonacci.")
            else:
                print(f"{numero} não pertence à sequência de Fibonacci.")
        elif escolha == '3.1':
            menor_valor, maior_valor, dias_acima_da_media = processar_faturamento_json()
            print(f"Menor valor: {menor_valor:.2f}")
            print(f"Maior valor: {maior_valor:.2f}")
            print(f"Dias acima da média: {dias_acima_da_media}")
        elif escolha == '3.2':
            menor_valor, maior_valor, dias_acima_da_media = processar_faturamento_xml()
            if menor_valor is not None:
                print(f"Menor valor: {menor_valor:.2f}")
                print(f"Maior valor: {maior_valor:.2f}")
                print(f"Dias acima da média: {dias_acima_da_media}")
            else:
                print("Nenhum valor de faturamento positivo foi encontrado.")
        elif escolha == '4':
            resultados = calcular_percentual_faturamento()
            for estado, percentual in resultados.items():
                print(f"{estado}: {percentual:.2f}%")
        elif escolha == '5':
            texto = input("Digite uma string: ")
            print(f"String invertida: {inverter_string(texto)}")                              
        elif escolha == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
