# agent/scraper.py
import requests
from bs4 import BeautifulSoup

def scrape_edital(url: str):
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "lxml")
    # Exemplo: pegar todos os links de PDF
    editais = [a["href"] for a in soup.find_all("a", href=True) if "pdf" in a["href"].lower()]

    return editais

if __name__ == "__main__":
    url = "https://www.exemplo.gov.br/editais"  # substitua por um site real
    dados = scrape_edital(url)
    print("Editais encontrados:")
    for d in dados:
        print(d)
