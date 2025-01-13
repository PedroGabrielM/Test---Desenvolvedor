import json
import xml.etree.ElementTree as ET

#exercicio 1
def calcular_soma():
    indice = 13
    soma = 0
    k = 0
    while k < indice:
        k += 1
        soma += k
    return soma

#exercicio 2
def pertence_fibonacci(numero):
    a, b = 0, 1
    while b < numero:
        a, b = b, a + b
    return b == numero or numero == 0

#exercicio 3 - corecao do arquivo xml
def corrigir_xml(arquivo_xml):
    with open(arquivo_xml, 'r', encoding='utf-8') as f:
        conteudo = f.read()

    #coloca uma raiz ao redor do conteúdo existente
    conteudo_corrigido = f"<root>{conteudo}</root>"

    #salva em arquivo temporraio
    arquivo_corrigido = "corrigido.xml"
    with open(arquivo_corrigido, 'w', encoding='utf-8') as f:
        f.write(conteudo_corrigido)

    return arquivo_corrigido

#exercicio 3
def analisar_faturamento(arquivo_json, arquivo_xml):
    #corrige xml
    arquivo_corrigido = corrigir_xml(arquivo_xml)

    # le arquivo json
    with open(arquivo_json, 'r') as f:
        dados_json = json.load(f)

    # xml corrigido
    tree = ET.parse(arquivo_corrigido)
    root = tree.getroot()

    valores = [
        float(row.find('valor').text) for row in root.findall('row')
        if float(row.find('valor').text) > 0
    ] + [
        dado["valor"] for dado in dados_json if dado["valor"] > 0
    ]

    menor = min(valores)
    maior = max(valores)
    media = sum(valores) / len(valores)
    acima_media = sum(1 for valor in valores if valor > media)

    return menor, maior, acima_media

#exercicio 4
def calcular_percentual_faturamento():
    faturamento_estados = {
        "SP": 67836.43,
        "RJ": 36678.66,
        "MG": 29229.88,
        "ES": 27165.48,
        "Outros": 19849.53
    }
    total = sum(faturamento_estados.values())
    percentual = {estado: (valor / total) * 100 for estado, valor in faturamento_estados.items()}
    return percentual

#exercicio 5
def inverter_string(texto):
    invertida = ''
    for i in range(len(texto) - 1, -1, -1):
        invertida += texto[i]
    return invertida

def menu():
    while True:
        print("\n--- Menu de Opções ---")
        print("1 - Calcular soma acumulada")
        print("2 - Verificar número na sequência de Fibonacci")
        print("3 - Analisar faturamento diário")
        print("4 - Calcular percentual de faturamento por estado")
        print("5 - Inverter uma string")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print(f"\nResultado da soma acumulada: {calcular_soma()}")

        elif opcao == "2":
            numero = int(input("\nInforme um número para verificar na sequência de Fibonacci: "))
            if pertence_fibonacci(numero):
                print(f"O número {numero} pertence à sequência de Fibonacci.")
            else:
                print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")

        elif opcao == "3":
            menor, maior, acima_media = analisar_faturamento('dados.json', 'dadosxml.xml')
            if menor is not None:
                print("\nFaturamento diário:")
                print(f"  Menor valor: {menor}")
                print(f"  Maior valor: {maior}")
                print(f"  Dias acima da média: {acima_media}")

        elif opcao == "4":
            print("\nPercentual de faturamento por estado:")
            for estado, perc in calcular_percentual_faturamento().items():
                print(f"  {estado}: {perc:.2f}%")

        elif opcao == "5":
            texto = input("\nInforme uma string para inverter: ")
            print(f"String invertida: {inverter_string(texto)}")

        elif opcao == "0":
            print("\nSaindo do programa. Até mais!")
            break

        else:
            print("\nOpção inválida! Tente novamente.")

menu()