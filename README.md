# Webscraping com Python e Kestra

## Descrição

Esta prova de conceito (PoC) implementa um agente de webscraping em Python, com execução automatizada via Kestra.
O objetivo é validar a viabilidade técnica para raspagem de dados de editais disponíveis na internet, integrando o pipeline de dados e mantendo o código versionado em GitHub.

## Tecnologias Utilizadas

-Python 3.10+
-BeautifulSoup4 + Requests (raspagem inicial)
-Kestra (orquestração do workflow)

## Configuração do Ambiente
### 1. Criar e ativar ambiente virtual

```terminal
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 2. Instalar dependências

```terminal
pip install -r requirements.txt
```

## Executando pelo Kestra

### 1. Suba o Kestra em localhost:

```terminal
docker compose up
```

### 2. Acesse: http://localhost:8080

### 3. Importe o workflow workflows/kestra_workflow.yml.

### 4. Execute o workflow poc-webscraping e verifique a saída no console do Kestra.