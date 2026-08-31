# G25_Busca_EDA2-2026.2

## Integrantes

| Matrícula | Nome |
| :--- | :--- |
| 232002664 | Giovanni Ferreira |
| 232025730 | Edson Pereira |

---

## Vídeo de Apresentação

Confira a explicação detalhada do projeto no YouTube:

👉 [Apresentação do projeto](https://youtu.be/lQCdevFDhxk)

---

## Sobre o Projeto

O objetivo do projeto é automatizar a leitura, extração, estruturação e busca de resultados em editais de concursos públicos (comum em editais no formato Cebraspe/CESPE).

Muitos editais de concursos divulgam notas em formato contínuo de texto dentro de arquivos PDF, separados por barras (`/`) e vírgulas (`,`), tornando difícil a identificação rápida da posição e classificação geral de um candidato.

### Principais Funcionalidades:
1. **Extração de Texto do PDF**: Utiliza a biblioteca `pdfplumber` para ler e consolidar as páginas do edital.
2. **Parsing e Limpeza de Dados**: Localiza a seção de interesse através de palavras-chave (`PALAVRA_CHAVE_INICIO`), separa os registros dos candidatos e extrai os campos:
   - Número de Inscrição
   - Nome do Candidato
   - Nota Final
3. **Persistência em JSON**: Salva a lista estruturada de candidatos em `dados_candidatos.json`.
4. **Ordenação e Classificação**: Ordena os candidatos de forma decrescente com base na nota final.
5. **Algoritmo de Busca**: Localiza um candidato pelo nome e retorna sua colocação no concurso.

---

## Como Executar o Projeto

### Pré-requisitos
- Python 3.8+ instalado
- Gerenciador de pacotes `pip`

### 1. Clonar o repositório
```bash
git clone https://github.com/EDA2-2026-2/G25_Busca_EDA2-2026.2.git
cd G25_Busca_EDA2-2026.2
```

### 2. Instalar as dependências
```bash
pip install -r requirements.txt
```
*(ou diretamente via `pip install pdfplumber`)*

### 3. Executar o script
```bash
python3 algoritmo_busca.py
```

---

## Exemplo de Saída

```text
Extração concluída! 101 candidatos encontrados e salvos no JSON.
O candidato Ana Beatriz Cavalcante Amorim, ficou na seguinte posição: 86º
```

---

## Estrutura do Repositório

```text
.
├── algoritmo_busca.py     # Script principal contendo a extração, ordenação e busca
├── dados_candidatos.json  # Arquivo gerado com os dados estruturados dos candidatos
├── edital.pdf             # Exemplo de edital utilizado para testes
├── edital_adv.pdf         # Exemplo adicional de edital
├── requirements.txt       # Lista de dependências do Python
└── README.md              # Documentação do projeto
```
