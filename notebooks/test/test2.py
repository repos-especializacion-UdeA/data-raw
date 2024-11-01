import requests,os,bs4,shutil

url='http://xkcd.com'

#making new folder
if os.path.isdir('xkcd') == True:
    shutil.rmtree('xkcd')
else:
    os.makedirs('xkcd')


#scrapiing information
while not url.endswith('#'):
    print('Downloading Page %s.....' %(url))
    res = requests.get(url)          #getting page
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text)

    comicElem = soup.select('#comic img')     #getting img tag under  comic divison
    if comicElem == []:                        #if not found print error
        print('could not find comic image')

    else:
        try:
            comicUrl = 'http:' + comicElem[0].get('src')             #getting comic url and then downloading its image
            print('Downloading image %s.....' %(comicUrl))
            res = requests.get(comicUrl)
            res.raise_for_status()

        except requests.exceptions.MissingSchema:
        #skip if not a normal image file
            prev = soup.select('a[rel="prev"]')[0]
            url = 'http://xkcd.com' + prev.get('href')
            continue

        imageFile = open(os.path.join('xkcd',os.path.basename(comicUrl)),'wb')     #write  downloaded image to hard disk
        for chunk in res.iter_content(10000):
            imageFile.write(chunk)
        imageFile.close()

        #get previous link and update url
        prev = soup.select('a[rel="prev"]')[0]
        url = "http://xkcd.com" + prev.get('href')


print('Done...')