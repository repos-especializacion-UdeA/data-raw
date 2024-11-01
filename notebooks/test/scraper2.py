import requests
from bs4 import BeautifulSoup
import os

# URL del sitio web donde deseas buscar archivos .zip
url = 'https://ninapro.hevs.ch/files/DB1/Preprocessed/'

# Realizar la solicitud HTTP a la página
response = requests.get(url)
if response.status_code == 200:
    # Crear el objeto BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Crear una carpeta para guardar los archivos .zip descargados
    os.makedirs("zip_files", exist_ok=True)
    
    # Encontrar todos los enlaces que terminan en .zip
    zip_links = []
    for link in soup.find_all('a', href=True):
        href = link['href']
        if href.endswith('.zip'):
            # Asegurarse de que el enlace es absoluto o convertirlo a absoluto si es relativo
            zip_url = href if href.startswith('http') else url + href
            zip_links.append(zip_url)
            
            # Descargar el archivo .zip
            zip_response = requests.get(zip_url, stream=True)
            if zip_response.status_code == 200:
                # Nombre del archivo (tomado de la URL)
                zip_name = os.path.join("zip_files", os.path.basename(zip_url))
                
                # Guardar el archivo en chunks para manejar archivos grandes
                with open(zip_name, 'wb') as f:
                    for chunk in zip_response.iter_content(chunk_size=8192):
                        f.write(chunk)
                
                print(f"Descargado: {zip_name}")
            else:
                print(f"Error al descargar {zip_url}")
else:
    print("Error al acceder a la página:", response.status_code)