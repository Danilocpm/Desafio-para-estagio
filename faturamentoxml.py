import xml.etree.ElementTree as ET

def processar_faturamento_xml():
    try:
        # Carregar dados do arquivo XML
        tree = ET.parse('dados.xml')
        root = tree.getroot()

        valores = []
        
        # Extrair valores de faturamento
        for row in root.findall('row'):
            valor_elemento = row.find('valor')
            if valor_elemento is not None and valor_elemento.text:
                try:
                    valor = float(valor_elemento.text)
                    if valor > 0:
                        valores.append(valor)
                except ValueError:
                    print(f"Valor inválido encontrado: {valor_elemento.text}")

        if valores:
            # Menor e maior valor de faturamento
            menor_valor = min(valores)
            maior_valor = max(valores)
            
            # Cálculo da média
            media_mensal = sum(valores) / len(valores)
            
            # Dias com faturamento acima da média
            dias_acima_da_media = sum(1 for valor in valores if valor > media_mensal)
            
            return menor_valor, maior_valor, dias_acima_da_media
        else:
            return None, None, None  # Nenhum valor de faturamento positivo encontrado
    
    except ET.ParseError:
        print("Erro ao analisar o arquivo XML.")
    except FileNotFoundError:
        print("Arquivo 'dados.xml' não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

