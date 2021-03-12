import csv
import requests
from bs4 import BeautifulSoup

def poluchit_html(url):
    otvet = requests.get(url)
    return otvet.text

def posled_func_csv(dannye):
    with open('spisok_note.csv', 'a') as spisok1:
        writer = csv.writer(spisok1, delimiter = '/')
        writer.writerow((dannye['klyuch'],dannye['klyuch2'], dannye['klyuch3']))

def obw_kolich_stranic(html):
    soup = BeautifulSoup(html, 'lxml')
    stranica_ul = soup.find('div', class_ = "pageToInsert").text.split()
    # total_pages = stranica_ssylka_4.find('')
    last_page = stranica_ul[-3]
    return int(last_page)

def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    product_list = soup.find('div', class_ = "catalog_main_table j-products-container").find_all('div', class_ = 'dtlist-inner-brand')
    #найти имя тов, характеристика, цена
    for i in product_list:
        try:
            imya = i.find('strong', class_ = "brand-name c-text-sm").text
        except:
            imya = ''
        try:
            harakter = i.find('span', class_ = 'goods-name c-text-sm').text
        except:
            harakter = ''
        try:
            cena = i.find('div', class_ = 'j-cataloger-price').text.strip()
        except:
            cena = ''
        # print(cena)
        itogo = {'klyuch': imya, 'klyuch2': harakter, 'klyuch3': cena}
        # print(itogo)
        posled_func_csv(itogo)


def main():
    nootebooks_url = 'https://www.wildberries.kg/catalog/elektronika/noutbuki-pereferiya/noutbuki-ultrabuki'
    page = '?page='

    pos_str = obw_kolich_stranic(poluchit_html(nootebooks_url))
    # get_page_data(poluchit_html(nootebooks_url))
    for nomer_str in range(1, pos_str+1):
        ssylka = nootebooks_url + page + str(nomer_str)
        vse = poluchit_html(ssylka)
        get_page_data(vse)
main()


