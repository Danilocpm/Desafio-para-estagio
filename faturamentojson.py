import json

def processar_faturamento_json():
    try:
        # Carregar dados
        with open('dados.json') as file:
            dados = json.load(file)
        
        valores = []
        
        # Processar dados e calcular estatísticas
        for dado in dados:
            valor = dado.get('valor', 0)
            if valor > 0:
                valores.append(valor)
        
        if valores:
            menor_valor = min(valores)
            maior_valor = max(valores)
            media_mensal = sum(valores) / len(valores)
            dias_acima_da_media = sum(1 for valor in valores if valor > media_mensal)
            
            return menor_valor, maior_valor, dias_acima_da_media
        else:
            return None, None, None  # Nenhum valor de faturamento positivo encontrado
    
    except FileNotFoundError:
        print("Arquivo 'dados.json' não encontrado.")
    except json.JSONDecodeError:
        print("Erro ao decodificar o arquivo JSON.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

