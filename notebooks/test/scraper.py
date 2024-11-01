import requests
from bs4 import BeautifulSoup

url = "https://ninapro.hevs.ch/files/DB1/Preprocessed/"

# https://ninapro.hevs.ch/files/DB1/Preprocessed/s1.zip

# Realizar la solicitud HTTP a la página
response = requests.get(url)
if response.status_code == 200:
    # Crear el objeto BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Encontrar todos los enlaces que terminan en .zip
    zip_links = []
    for link in soup.find_all('a', href=True):
        href = link['href']
        if href.endswith('.zip'):
            # Asegurarse de que el enlace es absoluto o convertirlo a absoluto si es relativo
            zip_url = href if href.startswith('http') else url + href
            zip_links.append(zip_url)

    # Imprimir las URLs de archivos .zip encontrados
    print("URLs de archivos .zip encontrados:")
    for zip_link in zip_links:
        print(zip_link)
else:
    print("Error al acceder a la página:", response.status_code)