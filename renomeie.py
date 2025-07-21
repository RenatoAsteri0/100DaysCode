import os
import re

# Caminho da pasta onde estão os diretórios "Day X"
CAMINHO_RAIZ = r'C:\Users\renat\Documents\pythonlearn'

# Regex para capturar o padrão "Day X"
padrao = re.compile(r'^Day (\d+)$', re.IGNORECASE)

# Lista de renomeações feitas
renomeacoes = []

for nome_antigo in os.listdir(CAMINHO_RAIZ):
    caminho_antigo = os.path.join(CAMINHO_RAIZ, nome_antigo)

    # Verifica se é diretório e bate com o padrão
    if os.path.isdir(caminho_antigo):
        match = padrao.match(nome_antigo)
        if match:
            numero = int(match.group(1))
            novo_nome = f"day_{numero:02d}"
            caminho_novo = os.path.join(CAMINHO_RAIZ, novo_nome)

            if not os.path.exists(caminho_novo):
                os.rename(caminho_antigo, caminho_novo)
                renomeacoes.append((nome_antigo, novo_nome))
            else:
                print(f"⚠️  Já existe a pasta: {novo_nome}, ignorando.")

# Mostrar relatório
if renomeacoes:
    print("✅ Pastas renomeadas com sucesso:\n")
    for antigo, novo in renomeacoes:
        print(f"🔁 {antigo}  →  {novo}")
else:
    print("⚠️  Nenhuma pasta renomeada.")
