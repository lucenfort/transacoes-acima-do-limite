def filtrar_transacoes(transacoes, limite):
    """
    Filtra as transações cujo valor absoluto seja maior que o limite especificado.

    :param transacoes: Lista de valores inteiros ou decimais representando transações financeiras.
    :param limite: Valor limite para filtrar as transações.
    :return: Lista contendo transações cujo valor absoluto seja maior que o limite.
    """
    return [transacao for transacao in transacoes if abs(transacao) > limite]


# Leitura da entrada no formato "[100, -50, 300, -150], 100"
entrada = input().strip()

# Processa a entrada para separar a lista de transações e o limite
entrada_transacoes, limite = entrada.split("],")
entrada_transacoes = entrada_transacoes.strip("[]").replace(" ", "")  # Remove colchetes e espaços
limite = float(limite.strip())  # Converte o limite para float

# Converte a string de transações para uma lista de inteiros
transacoes = [int(valor) for valor in entrada_transacoes.split(",")]

# Filtra as transações que ultrapassam o limite
resultado = filtrar_transacoes(transacoes, limite)

# Imprime o resultado no formato especificado
print(f"Transações: {resultado}")
