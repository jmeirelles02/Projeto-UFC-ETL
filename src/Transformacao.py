import pandas as pd

def processar_dados():
    print("Lendo arquivos CSV...")
    df_lutas = pd.read_csv('data/ufc_lutas_completo.csv')
    df_eventos = pd.read_csv('data/ufc_eventos.csv')

    df_completo = pd.merge(df_lutas, df_eventos, on='Evento', how='left')

    df_completo['Data'] = pd.to_datetime(df_completo['Data'], errors='coerce')

    def converter_tempo_segundos(tempo_str):
        try:
            if ':' in str(tempo_str):
                minutos, segundos = map(int, tempo_str.split(':'))
                return minutos * 60 + segundos
            return 0
        except:
            return 0

    df_completo['Tempo_Segundos'] = df_completo['Tempo'].apply(converter_tempo_segundos)

    df_completo['Disputa_Cinturao'] = df_completo['Disputa_Cinturao'].fillna(0).astype(int)

    colunas_finais = [
        'Evento', 'Data', 'Local', 
        'Lutador_1', 'Lutador_2', 
        'Categoria', 
        'Disputa_Cinturao',
        'Metodo', 'Round', 'Tempo', 'Tempo_Segundos'
    ]
    
    df_final = df_completo[colunas_finais]
    df_final = df_final.sort_values(by='Data', ascending=False)

    total_cinturoes = df_final['Disputa_Cinturao'].sum()
    print(f"Total de cinturões confirmados no Dataset Final: {total_cinturoes}")

    df_final.to_csv('ufc_dataset_completo.csv', index=False)
    print("Arquivo 'ufc_dataset_completo.csv' gerado.")

if __name__ == "__main__":
    processar_dados()