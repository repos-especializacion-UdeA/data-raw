import os
import requests
from bs4 import BeautifulSoup
from zipfile import ZipFile
from io import BytesIO

"""
https://discuss.python.org/t/web-scraping-and-download-zipfiles/53988/3    
"""

# Step 1: Load the webpage
url = 'https://ninapro.hevs.ch/instructions/DB1.html'
response = requests.get(url)
response.raise_for_status()

# Step 2: Parse the page to extract download URLs
soup = BeautifulSoup(response.content, 'html.parser')
download_links = soup.find_all('a', href=True)
datasets_urls = [link['href'] for link in download_links if link['href'].endswith('.zip')]
print(datasets_urls)

# Step 3: Download the Excel files
for dataset_url in datasets_urls:
    print(dataset_url)
    dataset_response = requests.get(dataset_url)
    #dataset_response.raise_for_status()

    # Step 4: Extract the Excel file from the zip archive
    """
    with ZipFile(BytesIO(dataset_response.content)) as zip_file:
        for zip_info in zip_file.infolist():
            print(zip_info.file_size.endswith('.mat'))
            
            if zip_info.filename.endswith('.mat'):
                zip_file.extract(zip_info, path='.')
                extracted_file_path = zip_info.filename
                # Step 5: Move the file to the desired location
                new_location = os.path.join('./raw', zip_info.filename)
                os.rename(extracted_file_path, new_location)
                print(f"Moved {extracted_file_path} to {new_location}")
            """