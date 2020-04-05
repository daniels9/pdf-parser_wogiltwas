
import io
import requests
import pdf_reader as pdfr

print("Hello world")

url = 'https://www.baden-wuerttemberg.de/fileadmin/redaktion/dateien/PDF/Coronainfos/200328_CoronaVO_Konsolidierte_Fassung.pdf'

r = requests.get(url)
f = io.BytesIO(r.content)

linkList2 = ['200328_CoronaVO_Konsolidierte_Fassung.pdf', '20200402-berlin.pdf', 'lesefassung_coronavo_hessen_docx.pdf', 'Verordnung 23.3.2_meck.pdf']
linkList = ['200328_CoronaVO_Konsolidierte_Fassung.pdf']

for link in linkList2:
    #print(link)
    pdfFileObj = open('docs/'+ link, 'rb')
    pdfr.readpdf(pdfFileObj)
    pdfFileObj.close()


