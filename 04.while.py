# crie um codigo que faca a conversao de moeda do real para dolar e vice versa

# etapas da resolucao
# 1) criar uma variavel chamada cotcao
# 2) solicitar ao usuario a opcao de conversao desejada
# 3) apresentar o resultado de conversão desejada
#4) perguntar se ele seja continuar a conversão

# 1) criar uma variavel chamada cotacao
cotacao = float(input("Digite a cotação do dólar em reais: "))

while True:
    # 2) solicitar ao usuario a opcao de conversao desejada
    print("\nEscolha a opção de conversão:")
    print("1 - Real para Dólar")
    print("2 - Dólar para Real")
    opcao = input("Digite 1 ou 2: ")

    if opcao == "1":
        valor_real = float(input("Digite o valor em Reais: R$ "))
        valor_dolar = valor_real / cotacao
        # 3) apresentar o resultado de conversão desejada
        print(f"R$ {valor_real:.2f} equivalem a US$ {valor_dolar:.2f}")
    elif opcao == "2":
        valor_dolar = float(input("Digite o valor em Dólares: US$ "))
        valor_real = valor_dolar * cotacao
        # 3) apresentar o resultado de conversão desejada
        print(f"US$ {valor_dolar:.2f} equivalem a R$ {valor_real:.2f}")
    else:
        print("Opção inválida. Tente novamente.")
        continue

    # 4) perguntar se ele queira continuar a conversão
    continuar = input("Deseja fazer outra conversão? (s/n): ").strip().lower()
    if continuar != 's':
        print("Programa encerrado.")
        break
