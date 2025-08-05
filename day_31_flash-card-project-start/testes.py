import pandas as pd
df = pd.read_excel('backups_programados.xlsx')
itens = df.to_dict('records')
for item in itens:
    if item['Status'] != 'OK':
        print(f"[ALERTA] Procedimento: {item['Procedimento']} | Sistema: {item['Sistema']}")
        print(f"Responsável: {item['Responsável']} | Data: {item['Data Esperada']}\n")