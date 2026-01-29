import requests
from bs4 import BeautifulSoup
import pandas as pd

def extrair_lista_eventos():
    url = 'http://ufcstats.com/statistics/events/completed?page=all'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    print(f"A acessar o site: {url}...")
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar o site: {e}")
        return

    soup = BeautifulSoup(response.content, 'html.parser')

    event_rows = soup.find_all('tr', class_='b-statistics__table-row')
    event_rows = soup.find_all('tr', class_='b-statistics__table-row')

    dados_eventos = []
    for row in event_rows[2:]:
        cols = row.find_all('td')
        
        if len(cols) >= 2:
            link_tag = cols[0].find('a')
            if link_tag:
                nome_evento = link_tag.text.strip()
                link_evento = link_tag['href']
            else:
                continue

            data_evento = cols[0].find('span').text.strip()
            localizacao = cols[1].text.strip()

            dados_eventos.append({
                'Evento': nome_evento,
                'Data': data_evento,
                'Local': localizacao,
                'Link': link_evento
            })

    df = pd.DataFrame(dados_eventos)
    
    print(f"Foram encontrados {len(df)} eventos.")
    
    df.to_csv('ufc_eventos.csv', index=False)
    print("Arquivo 'ufc_eventos.csv' criado com sucesso!")

if __name__ == "__main__":
    extrair_lista_eventos()