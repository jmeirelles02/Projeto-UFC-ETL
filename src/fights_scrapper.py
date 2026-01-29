import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def extrair_todas_lutas_final():
    try:
        df_eventos = pd.read_csv('data/ufc_eventos.csv')
    except FileNotFoundError:
        print("Erro: 'ufc_eventos.csv' não encontrado.")
        return

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    todas_lutas = []
    total_eventos = len(df_eventos)
    cinturoes_detectados = 0

    print(f"Iniciando extração final de {total_eventos} eventos...")

    for index, row in df_eventos.iterrows():
        link = row['Link']
        nome_evento = row['Evento']
        
        try:
            print(f"Processando {index + 1}/{total_eventos}: {nome_evento}")
            
            response = requests.get(link, headers=headers)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            rows = soup.find_all('tr', class_='b-fight-details__table-row')
            
            for table_row in rows:
                cols = table_row.find_all('td')
                
                if len(cols) >= 8:
                    nomes = cols[1].find_all('a')
                    if len(nomes) == 2:
                        lutador_1 = nomes[0].text.strip()
                        lutador_2 = nomes[1].text.strip()
                    else:
                        continue
                    
                    celula_peso = cols[6]
                    peso_texto = " ".join(celula_peso.get_text().split())
                    
                    tem_cinturao = 0
                    imagens = celula_peso.find_all('img')
                    for img in imagens:
                        src = img.get('src', '')
                        if 'belt' in src or 'title' in src:
                            tem_cinturao = 1
                            cinturoes_detectados += 1
                            break

                    metodo = " ".join(cols[7].get_text().split())
                    round_luta = cols[8].get_text().strip()
                    tempo = cols[9].get_text().strip()

                    todas_lutas.append({
                        'Evento': nome_evento,
                        'Lutador_1': lutador_1,
                        'Lutador_2': lutador_2,
                        'Categoria': peso_texto,
                        'Disputa_Cinturao': tem_cinturao,
                        'Metodo': metodo,
                        'Round': round_luta,
                        'Tempo': tempo
                    })
            
            time.sleep(0.5)

        except Exception as e:
            print(f"Erro no evento {nome_evento}: {e}")

    df_lutas = pd.DataFrame(todas_lutas)
    df_lutas.to_csv('ufc_lutas_completo.csv', index=False)
    
    print("-" * 30)
    print("Extração concluída com sucesso!")
    print(f"Total de disputas de cinturão identificadas via imagem: {cinturoes_detectados}")

if __name__ == "__main__":
    extrair_todas_lutas_final()