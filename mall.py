import requests
from bs4 import BeautifulSoup
import pandas

nama_toko = []
kategori_toko = []
lantai_toko = []

for i in range (1,21):
  konten = requests.get('https://aeonmall-bsdcity.com/shopping.php?page='+str(i)  )
    
  soup = BeautifulSoup (konten.content, 'html.parser')

  toko = soup.find_all("div","desc-shopping")
  for t in toko:
    nama = t.find("h3").get_text()
    kategori = t.find("span").get_text()
    lantai = t.find("div","tmaps").get_text()

    nama_toko.append(nama)
    kategori_toko.append(kategori)
    lantai_toko.append(lantai)
informasi_toko = {'nama':nama_toko,'kategori':kategori_toko,'lantai':lantai_toko}
df = pandas.DataFrame(informasi_toko, columns = ['nama','kategori','lantai'])
df.sort_values('lantai',axis = 0, ascending=True, inplace = True)

df.to_csv("assig1.csv",sep=',')
