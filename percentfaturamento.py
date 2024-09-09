def calcular_percentual_faturamento():
    faturamento = {
        'SP': 67836.43,
        'RJ': 36678.66,
        'MG': 29229.88,
        'ES': 27165.48,
        'Outros': 19849.53
    }

    total = sum(faturamento.values())

    resultados = {}
    for estado, valor in faturamento.items():
        percentual = (valor / total) * 100
        resultados[estado] = percentual

    return resultados

