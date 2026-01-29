import pandas as pd
import sqlite3

def carregar_sqlite():
    print("Iniciando processo de Carga para SQLite...")

    try:
        df = pd.read_csv('data/ufc_dataset_completo.csv')
    except FileNotFoundError:
        print("Erro: 'ufc_dataset_completo.csv' não encontrado.")
        return

    conn = sqlite3.connect('data/ufc.db')
    cursor = conn.cursor()

    df.to_sql('lutas', conn, if_exists='replace', index=False)
    
    print("Dados salvos com sucesso no arquivo 'ufc.db'.")
    print("-" * 40)
    
    query = """
    SELECT Metodo, COUNT(*) as Quantidade
    FROM lutas
    GROUP BY Metodo
    ORDER BY Quantidade DESC
    LIMIT 5
    """
    
    print("Top 5 Métodos de Vitória no UFC:")
    df_resultado = pd.read_sql(query, conn)
    print(df_resultado)

    conn.close()

if __name__ == "__main__":
    carregar_sqlite()