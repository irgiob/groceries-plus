from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

WOOL_URL = "https://www.woolworths.com.au/shop/search/products?searchTerm="

def get_html(item, search_url):
    for word in item.split(' '):
        search_url += word + "%20"
    print(f"looking for {item} at {search_url}")

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    #chrome_options.add_experimental_option('excludeSwitches', ['enable-automation']) 
    driver = webdriver.Chrome(executable_path="./chromedriver",options=chrome_options)
    driver.get(search_url)
    #time.sleep(5)
    html = driver.page_source
    driver.close()
    driver.quit()
    return html

def get_data_woolworths(item, website_url):
    html = get_html(item,website_url)
    soup = bs(html,'html.parser')
    data = soup.find_all('div', class_='shelfProductTile-content')

    results = []
    for product in data:
        prod_data = {}
        filtered_data = list(filter(None,[i.strip() for i in product.text.splitlines() if i]))
        print(filtered_data)
        prod_data['Name'] = filtered_data[0]
        if filtered_data[2].split()[0] == 'Save':
            prod_price = '$'+''.join(filtered_data[4:7])
            prod_data['Discount'] = filtered_data[2].split()[1]
            prod_data['Quantity'] = filtered_data[8]
        else:
            prod_price = '$'+''.join(filtered_data[3:6])
            prod_data['Discount'] = None
            prod_data['Quantity'] = filtered_data[6]
        prod_data['Price'] = prod_price
        results.append(prod_data)
    return results

item = 'lipton ice lemon tea'
print(get_data_woolworths(item, WOOL_URL))