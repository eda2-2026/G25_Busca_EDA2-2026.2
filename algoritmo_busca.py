import pdfplumber, json

# CONFIGURAÇÕES DO EDITAL ATUAL
PALAVRA_CHAVE_INICIO = "BANCODEDADOS" #Ultima palavra antes de começar a lista de candidatos sem espaço.
QTD_MINIMA_CAMPOS = 7
POSICAO_INSCRICAO = 0 #posição da incsrição no edital de divulgação de resultados (topo do edital)
POSICAO_NOME = 1 #posição do nome no edital de divulgação de resultados
POSICAO_NOTA = -1 #posição da nota no edital de divulgação de resultados
 
dados_completos = []

with pdfplumber.open("edital.pdf") as pdf:
    texto_bruto = ""
    
    # Percorre todas as páginas e junta o texto
    for pagina in pdf.pages:
        texto_da_pagina = pagina.extract_text()
        if texto_da_pagina:
            # Adiciona o texto da página atual ao bloco com um espaço
            texto_bruto += texto_da_pagina + " " 
            
    texto_continuo = texto_bruto.replace('\n', ' ')
    inicio_lista = texto_continuo.find("PALAVRA_CHAVE_INICIO")
    
    if inicio_lista != -1:
        texto_candidatos = texto_continuo[inicio_lista + 12:]
    else:
        texto_candidatos = texto_continuo 
        
    # Separa os candidatos usando a barra "/" modelo cebraspe
    lista_candidatos = texto_candidatos.split('/')
    
    for candidato in lista_candidatos:
        candidato = candidato.strip()
        
        if not candidato:
            continue
            
        # Separa os dados do candidato pela vírgula
        partes = candidato.split(',')
        
        if len(partes) >= QTD_MINIMA_CAMPOS:
            inscricao = partes[0].strip()
            nome = partes[1].strip()
            
            try:
                nota_final = float(partes[-1].strip())
                dados_completos.append({
                    "inscricao": inscricao,
                    "nome": nome,
                    "nota": nota_final
                })
            except ValueError:
                pass


with open("dados_candidatos.json", "w", encoding="utf-8") as arquivo_json:
    json.dump(dados_completos, arquivo_json, ensure_ascii=False, indent=4)

print(f"Extração concluída! {len(dados_completos)} candidatos encontrados e salvos no JSON.")
